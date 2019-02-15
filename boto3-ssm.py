import boto3, time, sys

#Returns Output and Status of the Command executed
def check_status(commandId, instanceId):
    client = boto3.client('ssm')
    response2 = client.get_command_invocation(
            CommandId=commandId,
            InstanceId=instanceId
        )
    status = response2['StatusDetails']
    output = response2['StandardOutputContent']
    return status, output;


#Function to exec command and return the command ID
def command_func(comm, instanceId):
    client = boto3.client('ssm')
    response = client.send_command(
        InstanceIds=[instanceId],
        DocumentName='AWS-RunShellScript',
        TimeoutSeconds=600,
        Comment="Testing SSM from boto3",
        Parameters={
            'commands': [
                 str(comm)
            ]
        },
        MaxConcurrency='1',
        MaxErrors='1',
    )
    status = response['Command']['StatusDetails']
    commandId = response['Command']['CommandId']
    return commandId


def main():
    instanceId = 'i-066328aa95bec1ca8'
    for index in range(1,len(sys.argv)):
        print("********************")
        print("Command: '{0}'".format(sys.argv[index]))
        commandId = command_func(str(sys.argv[index]), instanceId)
        status, output = check_status(commandId,instanceId)
        #Loop until the terminating state
        while (
                status == "Pending" or status == "InProgress" or
                status == "Delayed"):
            time.sleep(5)
            status, output = check_status(commandId,instanceId)
        print("Output: {0}".format(output))
        print("Status: {0}\n".format(status))


if __name__ == '__main__':
    main()
