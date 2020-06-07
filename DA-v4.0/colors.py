from colorama import init
init(convert=True)

colors= {'f_black'  : 30,         'f_red'    : 31,         'f_green'  : 32,
             'f_yellow' : 33,         'f_blue'   : 34,         'f_purple' : 35,
             'f_cyan'   : 36,         'f_white'  : 37,         'f_reset'  : 39,
             'b_black'  : 40,         'b_red'    : 41,         'b_green'  : 42,
             'b_yellow' : 43,         'b_blue'   : 44,         'b_purple' : 45,
             'b_cyan'   : 46,         'b_white'  : 47,         'b_reset'  : 49} # +60
 

def paint(text, c, light = False):
    tmp = 60 if light else 0
    if 'f_' in c:
        return '\x1b[{}m'.format(colors[c]+tmp) + str(text) + '\x1b[{}m'.format(colors['f_reset'])
    if 'b_' in c:
        return '\x1b[{}m'.format(colors[c]+tmp) + str(text) + '\x1b[{}m'.format(colors['b_reset'])
    log('Paint failed : ' + text + " | " + c + " " + str(light) , func = paint)

def warn(percent,text = ""):
    if text == "" :
        text = percent
    p=percent
    if not str(type(percent)) == "<class 'float'>":    
        try:
            p = float(percent.replace('%',''))
        except Exception as e:
            log('Convert failed : ' + str(p) , func = warn)
    color = ''
    if p < 20 :
        color = 'f_cyan'
    elif p < 80:
        color = 'f_green'
    elif p < 90:
        color = 'f_yellow'
    elif p <= 99:
        color = 'f_red'
    else:
        color = 'b_red'
    return paint(text,color)    
    
