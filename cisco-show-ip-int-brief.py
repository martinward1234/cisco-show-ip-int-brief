import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.16.1.69', port=22, username='python', password='python')

stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
output = stdout.readlines()
print ('\n'.join(output))
