#by ThanhNguyen
#lastupdate 1-6
import requests
import concurrent.futures
import time
import re

class Checker:
    def __init__(self):
        self.url = "http://www.uceprotect.net/en/rblcheck.php"
        self.br = requests.Session()
        self.headers = {
            "Host": "www.uceprotect.net",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "http://www.uceprotect.net/en/rblcheck.php",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "54",
            "Origin": "http://www.uceprotect.net",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0"
            }


    def getPayload(self,url):
        payload = "whattocheck=IP&ipr=103.119.84.0&subchannel="
        try:
            res = self.br.get(url)
            tmp = re.findall('<input type=hidden name=subchannel value=".*">',res.text)
            tmp = tmp[0].replace('<input type=hidden name=subchannel value="','')
            tmp = tmp.replace('">','')
            payload += tmp
            print(payload)
            return payload
        except Exception as e :
            print('{}\n'.format(e),end='')
        

#test param

#file= "C:\\Users\\nct28\\Desktop\\new.html"
#with open(file, 'r') as content_file:
#    response = content_file.read()


    def run(self):
        response = self.br.post(self.url,headers=self.headers,data=self.getPayload(self.url)) #done
        response = response.text

        level1= re.findall('<tr><td class=.*><img src=.*>'
                           +' <strong>103.119.84.0</strong></td>'
                           +'<td .*><b>.*</b></td><td .*><b>.*</b></td>',response)
        tmp = level1[0].replace('<tr><td class=db><img src="/flags/vn.gif"> <strong>','IP : ')
        tmp = tmp.replace('</strong></td><td class=db align=center bgcolor=lightGreen','\n - Status : ')
        tmp = tmp.replace('><b>','')
        tmp = tmp.replace('<td class=db align=center bgcolor=','\n -  Listingrisk : ')
        tmp = tmp.replace('<br>',' ')
        tmp = tmp.replace('</b></td>','')
        ret = "LEVEL 1 - " + tmp

        level2= re.findall('<tr><td class=.*><font><strong><img src=.*> <img src=.*> 103.119.84.0/22</strong></font></td>.*</td></tr>',response)
        
        tmp = level2[0].replace("<tr><td class=db><font><strong><img src='../img/k/same.gif'> <img src=\"/flags/vn.gif\">",'IP : ')
        tmp = tmp.replace('</strong></font></td><td class=db bgcolor=lightgreen','\n - Status ')
        tmp = tmp.replace('align=center><strong>',' ')
        tmp = tmp.replace('</strong></a></td><td class=db><center>','\n -  Level 1 listed in last 7 days : ')
        tmp = tmp.replace('</center></td><td class=db><center>','\n -  Level 2 Escalation limit : ')
        tmp = tmp.replace('</center></td><td class=db align=center>Not available</td></tr><tr><td class=db colspan=5></td></tr>','')
        ret+= "\nLEVEL 2 - " + tmp

        level3= re.findall('<strong>.*'+
                           '</strong></td><td class=db bgcolor=.*'+
                           'align=center>.*'+
                           '</td><td class=db><center>.*'+
                           '</center></td><td class=db valign=middle align=center><table><tr><td class=db><center>.*'+
                           '</td><td> </tr></table></center></td><td class=db><center>.*'+
                           '</center></td><td class=db><table align=center border=0 class=db><tr><td class=db><td class=db align=center>.*'+
                           '</td></tr></table></td></tr>',response)
#                           '</strong></td><td class=db><center>.*'+
#                          '</center></td><td class=db valign=middle align=center><table><tr><td class=db><center>.*'+
#                           '</td><td> <img src=.*> </tr></table></center></td><td class=db><center>.*'
#                           '</center></td><td class=db><table align=center border=0 class=db><tr><td class=db><td class=db align=center>.*'+
#                           '</td></tr></table></td></tr>',response

        tmp = level3[0].replace("align=center>",'')
        tmp = tmp.replace('</strong></td><td class=db bgcolor=','\n - Status : ')
        tmp = tmp.replace('<strong>','AS : ')
        tmp = tmp.replace('</td><td> </tr></table></center></td><td class=db><center>', '\n -  Level 3 Escalation limit : ')
        tmp = tmp.replace('</td><td class=db><center>','\n -  Total IP\'s : ')
        tmp = tmp.replace('</center></td><td class=db valign=middle <table><tr><td class=db><center>','\n -  Level 1 listed spammers in last 7 days  : ')
#    tmp = tmp.replace('</td><td> <img src=../img/s/down.gif> </tr></table><td class=db><center>', '\n - Level 3 Escalation limit ')        
        tmp = tmp.replace('</center></td><td class=db><table align=center border=0 class=db><tr><td class=db><td class=db','\n -  Problems : ')
        tmp = tmp.replace('</td></tr></table></td></tr>', '\n END.')
        tmp = tmp.replace('<br>',' ')
        ret += "\nLEVEL 3 - " + tmp
        return ret
    def find(ex , s):
        ret = re.findall(ex, s)
        return ret
        
