# made by ThanhNguyen
print("Initial may take times")
import os
import requests, base64
import time, concurrent.futures, getpass
import re
from datetime import *
from checker import Checker
from ssh import sshSession
from logger import log
from colors import paint, warn


usr = ''
pas = ''
Policy= paint("Only Ips in whitelist are allowed to login", 'f_purple', True)
PatchNote = ("-" +
paint("---------UPDATE NOTE Ver4.0\n","f_green")+
paint("Ver 4.0\n","f_cyan")+
paint("    + Using input credential\n","f_red",True)+
paint("    + Add Option - Reinput credential\n","f_green",True)+
paint("    + Add Check spam level UCE protect\n","f_red",True)+
paint("    + Add ssh backup checker \n","f_red",True)+
paint("Ver 4.1\n","f_cyan")+
paint("    + Add colors and functions\n","f_green",True)+
paint("    + Add mail error detect\n","f_green",True)+
paint("Ver 4.2\n","f_cyan")+
paint("    + Update Mail error detect, now show destination address\n","f_green",True)+
paint("    + Add log unknow mail error\n","f_green",True)+
paint("Ver 4.3\n","f_cyan")+
paint("    + Add Update note /view\n","f_green",True)+
paint("    + Add Option - mark all tickets as read\n","f_green",True)+
paint("Ver 4.4\n","f_cyan")+
paint("    + Now release as executable application\n","f_red",True)+
paint("    + Fix login bug\n","f_green",True)+
paint("    + Fix mark as read bug\n","f_green",True)+
paint("    + Colored note\n","f_green",True)+
paint("Ver 4.5\n","f_cyan")+
paint("    + Adding policy\n","f_red",True)+
paint("    + Fix not login bug\n","f_green",True)+             
paint("    + Fix input func\n","f_green",True)+
paint("Ver 4.6\n","f_cyan")+
paint("    + Recode the mailqueue log check\n","f_yellow",True)+
paint("    + Fix 3 mailqueue bug\n","f_green",True)+
paint("    + Fix ASN migrate problem\n","f_green",True)
             )
# list of sites 
sites = ['https://example:port/'  
         ]
# list of logged sites 
logged = {'https://example:port/'         :False,  # 0
         }

actions = {'login': 'CMD_LOGIN',
           'tickets': 'CMD_TICKET',
           'users': 'CMD_ALL_USER_SHOW',
           'sysinfo': 'CMD_SYSTEM_INFO',
           'services': 'CMD_SHOW_SERVICES',
           'mail': 'CMD_MAIL_QUEUE',
           'ps': 'CMD_PROCESS_MONITOR',
           'stats': 'CMD_ADMIN_STATS',
           'customBuild': 'CMD_PLUGINS_ADMIN/custombuild/index.html',
           'license': 'CMD_LICENSE'
           }










def signin():
    global usr, pas
    try:
        print(paint('--- Please enter Credential to login program prevent leaking cre ---', 'b_green'))
        usr = input("username : ")
        pas = getpass.getpass()
        return 'referer=%2F&username={}&password={}&json=yes'.format(usr, pas)
    except Exception as e:
        log(e, 'singin')


def mkHeader(site):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
               'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.5',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Origin': site,
               'Referer': site,
               'Upgrade-Insecure-Requests': '1'
               }
    return headers


def login(site):
    global br
    r = br.post(site + actions['login'], headers=mkHeader(site), data=cre2)
    try:
        if r.json()["success"] == "yes":
            print(paint("--login success--", 'f_green'))
            logged[site] = True
        else:
            print(paint("--loginfailed--", 'b_red'))
            logged[site] = False
    except Exception:
        print(paint("--loginfailed--", 'b_red'))
        logged[site] = False


def findError(json, site):
    try:
        if json["success"] == "no":
            log(json["error"], site)
            print(paint("=Logged out due to unexpected error","f_red"))
            logged[site] = False
            return 0
    except Exception as ex:
        pass
    
def menuInput(menu):
    try :
        print(menu,end='')
        choice = input()
        li = ' '.join(list(map(str,list('1 2 3 4 5 6 7 8 9 10 11 12 13 14'.split(' '))[:menu.count('\n')-1])))
        if str(choice) in str(li) and not choice == '':
            return choice
    except Exception as e:
         log(exception, func, "")
    return -1 

def trimSite(site):
    host = site.replace('https://', '')
    host = host.replace('http://', '')
    host = host.replace(':{port}/', '')
    return host


def removeNonsenseTickets(site):
    # POST data:select2=000000389&read=Mark+as+read&action=multiple&sorting=sort1%3D-1 # mark as read
    # POST data:subject_select=3&subject=Brute-Force+Attack+detected+in+service+log&when=all&delete_messages_days=1&delete=Delete&action=clear
    # POST data:subject_select=4&subject=is+currently+down&when=all&delete_messages_days=1&delete=Delete&action=clear
    global br
    a = br.post(site + actions['tickets'] + '?json=yes', headers=mkHeader(site),
                data="subject_select=3&subject=Brute-Force+Attack+detected+in+service+log&when=all&delete_messages_days=1&delete=Delete&action=clear")
    b = br.post(site + actions['tickets'] + '?json=yes', headers=mkHeader(site),
                data="subject_select=4&subject=is+currently+down&when=all&delete_messages_days=1&delete=Delete&action=clear")

def seenTickets(site):
    #select[range]=[id]&read=Mark+as+read&action=multiple&sorting=sort1%3D-1
    global br
    r = br.get(site + actions['tickets'] + '?json=yes', headers=mkHeader(site))
    findError(r.json(), site)
    if int(r.json()["messages"]["info"]['rows']) == 0:
        print('--There is no message to view---')
        return 0
    data = ""
    for mess in range(int(r.json()["messages"]["info"]["rows"])):
        data += "select{}={}&".format(str(mess),r.json()["messages"][str(mess)]["message"])
    data += "read=Mark+as+read&action=multiple&sorting=sort1%3D-1"
    br.post(site + actions['tickets']+"?json=yes",data=data, headers=mkHeader(site))
    printTickets(site)
    
def printTickets(site):
    removeNonsenseTickets(site)
    global br
    r = br.get(site + actions['tickets'] + '?json=yes', headers=mkHeader(site))
    findError(r.json(), site)
    h = "{:<5} | {:<19} | {} \t".format("isNew", "Time", "Subject")
    if int(r.json()["messages"]["info"]['rows']) == 0:
        print('--There is no message to view---')
        return 0
    print(h)
    print('=' * 60)
    for mess in range(int(r.json()["messages"]["info"]["rows"]) - 1, -1, -1):
        row = "{:<5} | {} | {} \t".format(r.json()["messages"][str(mess)]["new"],
                                          datetime.fromtimestamp(int(r.json()["messages"][str(mess)]["last_message"])),
                                          # r.json()["messages"][str(mess)]["message"], # message id
                                          r.json()["messages"][str(mess)]["subject"])
        if 'are now ready' in row or 'has been updated' in row:
            print(paint(row, 'f_green'))
        elif 'getting old' in row:
            print(paint(row, 'f_yellow'))
        elif 'error' in row:
            print(paint(row, 'f_red'))
        elif 'Warning' in row:
            print(paint(row, 'b_red'))

    print('-' * 60)


def printUsers(site):
    global br
    r = br.get(site + actions['users'] + '?json=yes', headers=mkHeader(site))
    findError(r.json(), site)
    h = "{:<12} | {:<15} | {:<15} \t".format("user", "Bandwidth", "Disk Usage")
    print(h)
    print('=' * 60)
    for mess in range(int(r.json()["info"]["rows"])):
        if r.json()[str(mess)]["username"]["is_user"] == "yes":
            quota = float(r.json()[str(mess)]["quota"]["usage"]) if "unlimited" in r.json()[str(mess)]["quota"][
                "limit"] else 100 * float(r.json()[str(mess)]["quota"]["usage"]) / float(
                r.json()[str(mess)]["quota"]["limit"])
            banwidth = float(r.json()[str(mess)]["bandwidth"]["usage"]) if "unlimited" in \
                                                                           r.json()[str(mess)]["bandwidth"][
                                                                               "limit"] else 100 * float(
                r.json()[str(mess)]["bandwidth"]["usage"]) / float(r.json()[str(mess)]["bandwidth"]["limit"])
            row = "{:<12} | {:<22}    | {:<22}    \t".format(r.json()[str(mess)]["username"]["value"],
                                                             paint("{:.4f}/Unli".format(banwidth),
                                                                   'f_green') if banwidth > 100 else warn(banwidth,
                                                                                                          "{:.4f}%".format(
                                                                                                              banwidth)),
                                                             paint("{:.4f}/Unli".format(quota),
                                                                   'f_green') if quota > 100 else warn(quota,
                                                                                                       "{:.4f}%".format(
                                                                                                           quota)))
            print(row)
    print('-' * 60)


def mailQueue(site):
    # #No - not updated error code 
    loopError = {"#01": "OverQuotaTemp",
                 "(-44)": "451 Internal resource temporarily unavailable",
                 "(-46)": "454 Transient reject by behaviour spam",
                 "(110)": "Connection timed out",
                 "(-51)": "retry time not yet reached for any host",
                 "(-52)": "retry time not reached",
                 "(-53)": "retry time not reached for any host",
                 "(-1)": "host lookup did not complete",
                 "(32)": "Broken pipe",
                 "(-18)": "closed connection in response",
                 "(111)": "Connection refused",
                 "(113)": "No route to host"}
    r = br.get(site + actions['mail'] + '?json=yes', headers=mkHeader(site))
    findError(r.json(), site)

    for mess in range(int(r.json()["table"]["info"]["rows"])):
        if not "<>" in r.json()["table"][str(mess)]["sender"]:
            print("-ID= " + r.json()["table"][str(mess)]["id"] + " --- " + str(
                int(r.json()["table"][str(mess)]["time"]) / 3600) + "h")
            temp = br.get(site + actions['mail'] + '?json=yes&id=' + r.json()["table"][str(mess)]["id"],
                          headers=mkHeader(site))
            tempLogList = list(set(map(lambda x: " ".join(list(x.split(" "))[2:]), list(temp.json()['logs'].split("\n")))))
            loop = dict()
            unknow = []
            
            logList = []
            errorList = list(loopError.keys())
            for i in tempLogList:
                success = False
                if 'Received' in i or 'succeeded' in i or i == "":
                    success = True
                if not success:
                    logList.append(i)

            for er in errorList:
                mailList = ""
                for i in logList:
                    if er not in loop.keys():
                        if er in i or loopError[er] in i:
                            loop[er] = str(i.split(" ")[0])
                        elif er not in i and loopError[er] not in i and i not in unknow:
                            confirm = True
                            for error in list(loopError.keys()):
                                if error in i or loopError[error] in i:
                                    confirm = False
                            if confirm:
                                unknow.append(i)
                                line = paint('#Unknow log line : ', 'f_red') + paint(i, 'f_yellow')
                                print(line)                        
                                log('Unknow log : ' + i, func , site , 'checking log line')
                    else :
                        mail = str(i.split(" ")[0])
                        if '@' in mail and mail not in mailList:
                            mailList += mail + ', '
                if er in loop.keys():
                    if mailList != "" and '@' not in loop[er]:
                        loop[er] = mailList[:-2]
                    print(paint("{} {} ({})".format(er,loopError[er],loop[er])  ,'f_yellow'))

            
            """
            for er in list(loopError.keys()):
                for i in tArray:
                    sucess = False
                    if 'Received' in i or 'transport succeeded' in i or i == "":
                        sucess = True
                    elif er not in loop:
                        if er in i :
                            loop.append(er)                            
                            ex = er + ' ' + loopError[er] 
                        elif loopError[er] in i:
                            loop.append(er)
                            ex = er + ' ' + loopError[er] 
                    elif er not in i and loopError[er] not in i and i not in unknow:
                        confirm = True
                        for error in list(loopError.keys()):
                            if error in i or loopError[error] in i:
                                confirm = False
                        if confirm:
                            unknow.append(i)
                            line = paint('#Unknow log line : ', 'f_red') + paint(i, 'f_yellow')
                            print(line)                        
                            log('Unknow log : ' + i, func , site , 'checking log line')
                    else:
                        pass                
                    if not sucess:
                        mail = str(i.split(" ")[0])
                        if '@' in mail and mail not in mailList:
                            mailList.append(mail)
            try:
                t = ""
                for mail in mailList:
                    if len(mailList) == 1:
                        t = mail
                    else:
                        t += mail+', '
                t= '('+t[:-2]+')'
                print(paint(ex + '  ' + t ,'f_yellow'))
            except Exception as e :
                log(e, func, site)
            """
                   

def printStats(site):
    r = br.get(site + actions['stats'] + '?json=yes', headers=mkHeader(site))
    head = "{:25} | {:14}  | {:12}   | {:5} | {}  \t".format("Filesystem", "Used", "Available", "Capacity",
                                                             "Mounted on")
    print(head)
    findError(r.json(), site)
    for mess in range(int(r.json()["disk"]["info"]["rows"])):
        if "root" in r.json()["disk"][str(mess)]["Filesystem"] or "/dev" in r.json()["disk"][str(mess)]["Filesystem"]:
            a = paint("Unlimited", 'f_green') if r.json()["disk"][str(mess)]["Available"] == "unlimited" else float(
                r.json()["disk"][str(mess)]["Available"]) / 1048576
            row = "{:25} | {:10.4f} GB   | {:10.4f} GB  | {:18} | {}  \t".format(
                r.json()["disk"][str(mess)]["Filesystem"],
                float(r.json()["disk"][str(mess)]["Used"]) / 1048576,
                a,
                warn(r.json()["disk"][str(mess)]["Capacity"]),
                r.json()["disk"][str(mess)]["Mounted on"])
            if int(r.json()["disk"][str(mess)]["Capacity"].replace('%', '')) > 80:
                row += "\t Limit Warning"
            print(row)


def printService(site):
    global br
    r = br.get(site + actions['services'] + '?json=yes', headers=mkHeader(site))
    head = "{:15} | {:7} | {:6} | {}  \t".format("Name", "Memory", "Status", "Pids")
    print(head)
    findError(r.json(), site)
    for service in list(r.json()["memory"].keys()):
        pids = ''
        percentage = "{:17}".format(paint('0.00', 'f_blue'))
        if not r.json()["memory"][service] == "":
            percentage = warn(float(r.json()["memory"][service]) / 15.01, r.json()["memory"][service])
        if service in r.json()["pids"].keys():
            pids = ", ".join(r.json()["pids"][service])
        row = "{:15} | {:8} | {:6} | {}  \t".format(service,
                                                    percentage,
                                                    r.json()["status"][service],
                                                    pids)
        print(row)


def printLicense(site):
    r = br.get(site + actions['license'] + '?json=yes', headers=mkHeader(site))
    findError(r.json(), site)
    row = "Current DA Ver : {}\nIp : {}\nName : {}\nOS name : {}\nLicense remain : {}\nRelease DA Ver : {}".format(
        r.json()["version"],
        r.json()["ip"],
        r.json()["name"],
        r.json()["os_name"],
        r.json()["remaining"],
        r.json()["currentversion"])
    print(row)


def updateLicense(site):
    r = br.get(site + actions['license'] + '?json=yes&update=license', headers=mkHeader(site))
    findError(r.json(), site)
    if r.json()["success"] == "Update queued":
        print("License update success.")
    else:
        print(paint("License update Failed.", 'f_red', True))
        log(r.json()["result"], site)
    r = br.get(site + actions['license'] + '?json=yes&update=program', headers=mkHeader(site))
    if not "You already have the most recent version of the program" in r.json()["result"]:
        print("DA update success.")
    else:
        print(paint("DA update Failed.", 'f_red', True))
        log(r.json()["result"], func, site)


def checkSpam():
    checker = Checker()
    result = checker.run()
    print(result)


def checkBackups(site):
    commands = ['cd /home/admin/admin_backups',
                'sudo ls -la']
    session = sshSession(trimSite(site), 22, usr, pas)
    session.getShell()
    backups = session.checkBackups()
    for backup in backups:
        print(backup)
    session.exit()

def option():
    global cre2
    OptionSwitcher = {"1": signin}
    choice = menuInput("=== OPTION ===\n"+
                       "1.Re-enter credential\n" +
                       "2.Mark as read all tickets\n" +
                       "Choice : ")
    if choice == "1":
        cre2 = signin()
        for site in sites:
            print("- - - - - - - " + paint(site, 'f_purple', True) + " - - - - - - - - -")
            login(site)
    if choice == "2":
        for site in sites:
            print("- - - - - - - " + paint(site, 'f_purple', True) + " - - - - - - - - -")
            seenTickets(site)

def policyCheck():
    whitelist = base64.b64decode(b'MTE1Ljc1LjE5MS40NCAxODIuMjQ4LjI0My4yMTE=').decode()
    ip = br.get("http://ifconfig.me/ip").text
    if ip in whitelist:
        return True
    else:
        return False


#cre2 = 'referer=%2F&username=&password=&json=yes'
def main():
    global cre2
    cre2 = signin()
    func = login
    for site in sites:
        print("- - - - - - - " + paint(site, 'f_purple', True) + " - - - - - - - - -")
        login(site)

    switcher = {"1": printTickets,
                    "2": printUsers,
                    "3": printStats,
                    "4": mailQueue,
                    "5": printService,
                    "6": printLicense,
                    "7": updateLicense,
                    "8": checkSpam,
                    "9": checkBackups,
                    "10": login}

    while True:
        choice = menuInput(paint("-----------menu----------\n", 'f_cyan') +            
                           "1.Print Ticket/ Message\n" +
                           "2.Print Users usage \n" +
                           "3.Print System Stats\n" +
                           "4.Print Mail Queue\n" +
                           "5.Print Services usage\n" +
                           "6.Print DA License\n" +
                           "7.Update DA License\n" +
                           "8.Check Spam Level\n" +
                           "9.Check Backups via ssh \n" +
                           "10.Re-login\n"
                           "11.Option\n"
                           "Choice : ")
        if choice == -1 :
            print(paint("Invalid Choice","f_red"))
        elif choice == "11":
            option()
        elif choice == "8":
            checkSpam()
        else:
            func = switcher.get(choice, "Invalid Choice")
            for site in sites:
                print("- - - - - - - " + paint(site, 'f_purple', True) + " - - - - - - - - -")
                if logged[site] == True or choice == "10":
                    try:
                        func(site)
                    except Exception as exception:
                        log(exception, func, site)
                else :
                    print(paint("Not Logged in","f_yellow"))
# END of main func ---------------------------------------------------------------------------------------
def uselessFunc():
    pass
br = requests.Session()
func = uselessFunc
cre2=""
print(Policy)
print(paint("-"*60, 'b_yellow', True))
print(PatchNote)


    
try:
    debug = False
    if debug:
        print('-----------debug mode is enabled --- ')
        usr=''
        pas=''
        cre2='referer=%2F&username={}&password={}&json=yes'.format(usr, pas)
        site = sites[10]
        if not policyCheck():
                main()
        else:
                print(paint("Your ip is not allowed to use this program", 'f_red', True))
    else :
        if policyCheck():
            main()
        else:
            print(paint("Your ip is not allowed to use this program", 'f_red', True))
except Exception as e:
    log(e, func, "--frame--")
