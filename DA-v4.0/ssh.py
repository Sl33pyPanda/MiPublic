import paramiko
import time
from logger import log

class sshSession:
    def __init__(self, site, port, user, password):
        self.host = site
        self.port = port
        self.username = user
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.username, self.password)

    def getShell(self):
        self.channel = self.ssh.invoke_shell()
        out = self.channel.recv(9999)
        print(out.decode(),end='')
        return self.channel
    def exec(self,commands):
        sudoer = False
        out = ''
        for c in commands:
            self.channel.send(c + '\n')                    
            while not self.channel.recv_ready():
                time.sleep(0.1)
            re = self.channel.recv(9999).decode()
            if '[sudo]' in re:
                self.channel.send(self.password+'\n')
                time.sleep(1)
            out += re

        time.sleep(0.1)
        re = self.channel.recv(9999).decode()
        out+=re
        return out

    def checkBackups(self):
        commands = ['cd /home/admin/admin_backups',
                    'sudo ls -la']
        out = self.exec(commands)
        tmp = []
        for line in out.split('\r\n'):
            try:
                tmp.append(list(filter(lambda x : x!= '',list(line.split(' '))))[8])
            except Exception as e :
                if not 'index out of range' in str(e):
                    log(e, 'checkBackups', self.host )
        return tmp[2:]

    def exit(self):
        self.ssh.close() 