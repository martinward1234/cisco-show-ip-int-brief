#!/usr/bin/python

# A script to ssh into a cisco device, set the terminal length
# such that paging is turned off, then run commands.
# the results go into 'resp', then are displayed.
# Tweak to your hearts content!

import paramiko
import cmd
import time
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.16.1.69', username='python', password='python')
(print) ("SSH connection established, please wait for output...")

stdin, stdout, stderr = ssh.exec_command('enable')
stdin.write('python\n')
stdin.flush()
# stdin, stdout, stderr = ssh.exec_command('show run')
output = stdout.readlines()
print ('\n'.join(output))
ssh.close()
