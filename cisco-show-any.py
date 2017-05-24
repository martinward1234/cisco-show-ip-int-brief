#!/usr/bin/python

# A script to ssh into a cisco device, and run any command specified
# by the sysadmin by setting the command in the variable

import paramiko
import cmd
import time
import sys

# VARIABLES THAT NEED CHANGED
ip = '172.16.1.69'
username = 'python'
password = 'python'
UserInput = 'show ip route'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username=username, password=password)
(print) ("SSH connection established, please wait for output...")
time.sleep(0.5)
(print) ("Running Command", UserInput)

stdin, stdout, stderr = ssh.exec_command(UserInput)
output = stdout.readlines()
print ('\n'.join(output))



ssh.close()
