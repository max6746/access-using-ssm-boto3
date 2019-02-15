import boto3, time, sys

#Recursive function to check the status
#Returns after Success or Failed
def check_status(commandId, instanceId):
    client = boto3.client('ssm')
    response2 = client.get_command_invocation(
            CommandId=commandId,
            InstanceId=instanceId
        )
    resp = response2['StatusDetails']
    if resp != 'Success':
        print(resp)
        time.sleep(5)
        check_status(commandId,instanceId)
    print("Output: {0}".format(response2['StandardOutputContent']))
    return resp

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

    print(status)
    return commandId

#Call func to check status
def main():
    instanceId = 'i-066328aa95bec1ca8'
    for index in range(1,len(sys.argv)):
        commandId = command_func(str(sys.argv[index]), instanceId)
        status = check_status(commandId,instanceId)
        if status == "Success":
            print('Success Main')
        elif status == "Failed":
            print('Failed')
        else:
            print('Status: {0}'.format(status))

if __name__ == '__main__':
    main()
