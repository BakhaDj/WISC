import paramiko
import pandas as pd

df = pd.DataFrame({'Имя':[], "Статус":[]})


hostname = '84.201.131.151' 
myuser   = 'host-service'
mySSHK   = 'C:\\Users\\Legion\\.ssh\\id_ed25519.pub'
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=myuser, key_filename=mySSHK)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cd site && sqlite3 dbs "select * from Users;"')
stdout=ssh_stdout.readlines()
ssh.close()

for string in stdout:
    df.loc[ len(df.index )] = string.split('|')[1:]

df.to_excel('Список.xlsx')
