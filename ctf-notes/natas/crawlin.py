from threading import Thread
import requests
from requests.auth import HTTPBasicAuth
import time
import re

def craw(crawlin):
    global result
    global count
    print('crawlin on {} \n'.format(crawlin), end ='' )
    res = browser.get(crawlin)
    ret = re.findall('<a rel="nofollow" target="_blank" href=".*</a>', res.text)    
    for site in ret:
        site = site.split('"')
        site = site[5]
        site = site.replace("http://","")
        result.append(site)
    count += 1
    print("done {} \n".format(count) , end='')
        
url = input("nhap link : ")

browser = requests.Session()

pages = int(input("nhap so trang : "))
result = []

def read(result):
    f = open("sites.txt", "r")
    for line in f:
        result.append(line)
    f.close()
def write(result):    
    f = open("sites.txt", "w")
    for line in result:
        f.write(line + "\n")
    f.close()

count = 0
for i in range(0,pages):
    Thread(target=craw, args={url +"?page=" str(i + 1)}).start()
while(count != pages):
    time.sleep(2)
write(result)
print("All done")





