# access-using-ssm-boto3
Running commands on ec2 instance using SSM. 
## Command
`python3 boto3-ssm.py "sudo yum update -y" "sudo yum install -y httpd" "sudo service httpd start"`

## Output
```
root@MAYANK:~/Flux7/ssm/access-using-ssm-boto3# python3 boto3-ssm.py "yum update -y" "yum install -y httpd" "service httpd start"
********************
Command: 'yum update -y'
Output: Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
No packages marked for update

Status: Success

********************
Command: 'yum install -y httpd'
Output: Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
Resolving Dependencies
--> Running transaction check
---> Package httpd.x86_64 0:2.4.37-1.amzn2.0.1 will be installed
--> Processing Dependency: mod_http2 for package: httpd-2.4.37-1.amzn2.0.1.x86_64
--> Running transaction check
---> Package mod_http2.x86_64 0:1.11.1-1.amzn2 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package         Arch         Version                    Repository        Size
================================================================================
Installing:
 httpd           x86_64       2.4.37-1.amzn2.0.1         amzn2-core       1.3 M
Installing for dependencies:
 mod_http2       x86_64       1.11.1-1.amzn2             amzn2-core       150 k

Transaction Summary
================================================================================
Install  1 Package (+1 Dependent package)

Total download size: 1.5 M
Installed size: 4.4 M
Downloading packages:
--------------------------------------------------------------------------------
Total                                              7.9 MB/s | 1.5 MB  00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : httpd-2.4.37-1.amzn2.0.1.x86_64                              1/2
  Installing : mod_http2-1.11.1-1.amzn2.x86_64                              2/2
  Verifying  : mod_http2-1.11.1-1.amzn2.x86_64                              1/2
  Verifying  : httpd-2.4.37-1.amzn2.0.1.x86_64                              2/2

Installed:
  httpd.x86_64 0:2.4.37-1.amzn2.0.1

Dependency Installed:
  mod_http2.x86_64 0:1.11.1-1.amzn2

Complete!

Status: Success

********************
Command: 'service httpd start'
Output:
Status: Success
```
