import os

from datetime import *
from colorama import init
init(convert=True)

def read(result):
    f = open("abcxyz.txt", "r")
    for line in f:
        result.append(line)
    f.close()
def write(result, mode = 'a'):
    today = date.today() 
    logfile = 'log\\' + today.strftime("%d-%b") + '.txt'
    try:
        f = open(logfile, mode)
        f.close()
    except Exception as e :
        if "No such file or directory" in str(e):
            os.mkdir('log')
       
    f = open(logfile, mode)
    for line in result:
        f.write(line + "\n")
    f.close()
def log(event, func ,site = "", subFunc = ""):
    now = str(datetime.now()) + ' ' + site + ' at ' + str(func) + ' while ' + str(subFunc) + ' '
    lines = list(map(lambda x : now + x,list(str(event).split('\n'))))
    write(lines)
