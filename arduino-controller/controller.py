
#arduino test code
""" 
int datafromUser=0;
void setup() {
  pinMode( 13 , OUTPUT );
  Serial.begin(38400);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    char inByte = Serial.read(); // read the incoming data
    Serial.print(inByte);
  } 
}
"""

import inputs
import time
import _thread
import serial
from serial import *
import traceback

isDebug = False #debug mode
def initialize():
    print('Initializing...')
    try:
        for device in inputs.devices:
            print(device)
        gamepad = inputs.devices.gamepads[0]
        print('Ready...')
        return True
    except Exception as e:
        if (str)(e).find('out of range'):
            print('No controller found... closing...')
        printTrace('init',e)
        return False
        
modderJoy = 1
modderTrigger = 1


syn         = 'SYN_REPORT'   #0
btnStart    = 'BTN_START'    #START
btnSelect   = 'BTN_SELECT'   #SELECT
trgLeft     = 'ABS_Z'        #L2
btnLeft     = 'BTN_TL'       #L1
trgRight    = 'ABS_RZ'       #R2
btnRight    = 'BTN_TR'       #R1
btnA        = 'BTN_SOUTH'    #A
btnX        = 'BTN_WEST'     #X
btnY        = 'BTN_NORTH'    #Y
btnB        = 'BTN_EAST'     #B
arrowX      = 'ABS_HAT0X'    #-Left +Right
arrowY      = 'ABS_HAT0Y'    #-Up   +Down
jLeftX      = 'ABS_X'        #-Left +Right
jLeftY      = 'ABS_Y'        #-Down +Up
btnJoyLeft  = 'BTN_THUMBL'   #LEFT_Joy
jRightX     = 'ABS_RX'       #-Left +Right 
jRightY     = 'ABS_RY'       #-Down +Up
btnJoyRight = 'BTN_THUMBR'   #RIGHT_Joy


currentState = {}
btnMap = {
    btnStart    : 0 ,
    btnSelect   : 1 ,
    trgLeft     : 2 ,
    btnLeft     : 3 ,
    trgRight    : 4 ,
    btnRight    : 5 ,
    btnA        : 6 ,
    btnX        : 7 ,
    btnY        : 8 ,
    btnB        : 9 ,
    arrowX      : 10 ,
    arrowY      : 11 ,
    jLeftX      : 12 ,
    jLeftY      : 13 ,
    btnJoyLeft  : 14 ,
    jRightX     : 15 ,
    jRightY     : 16 ,
    btnJoyRight : 17 
   }

def openCon():
    con = 10
    while type(con) is int and con > 1:
        try:
            con = serial.Serial( "COM" + str(input("COM port : ")), 19200)
            print('baun : 19200')
            return con
        except Exception as e:
            printTrace('openCon',e)
            time.sleep(1)
            print('retrying...' +str(con)+' time remaining .. .')
            con -= 1 
    return False

def state(k, v):
    s = '%d,%d\n' %(btnMap[k],v)
    if isDebug:
        print(s, end = '')
    return s.encode()

def printTrace(method,e):
     print(str(e) + ' ' + method)
     if isDebug:
         traceback.print_exc()
       
def doEventK(code, state):
    '''set some thing '''
    currentState[code] = state
    if code == btnX:
         gamepad.set_vibration(1, 0, 100)
    pass

def gamepadListener():
    joy = 0
    trigger = 0
    con = openCon()
    _thread.start_new_thread(readDataTransferring,(con,))
    try:
        while 1:
            events = inputs.get_gamepad()
            for btn in events:            
                """ DO event """
                if btn.ev_type == 'Sync':
                    continue;
                else :
                    con.write(state(btn.code, btn.state))
    except Exception as e:
        printTrace('gamepadListener',e)

                    #con.write(b'123')
            
"""            elif btn.ev_type == 'Absolute':
                if btn.code[4:] in ['X','Y','RX','RY']:
                    doEventA(btn.code,btn.state)
                    joy = (joy + 1)%modderJoy
                    if joy == 0 : _thread.start_new_thread(printstate,(btn.code,btn.state))
                else :
                    doEventA(btn.code,btn.state)
                    trigger = (trigger + 1)%modderTrigger
                    if trigger == 0 : _thread.start_new_thread(printstate,(btn.code,btn.state))
                #print(btn.state)
                #states.append(btn.state)                
                #print(states)
                #del states[:]
                
            elif btn.ev_type == 'Key':
                doEventK(btn.code,btn.state)
                _thread.start_new_thread(printstate,(btn.code,btn.state))
                #print(btn.state)
"""

                    
   #### FUKIN MAIN ###
def readDataTransferring(con):
    try:
        while 1 :
            print(con.readline())
    except Exception as e:
        printTrace('readDataTransferring',e)
        
def main():
    #while 1:       
        try:
            gamepadListener()
        except Exception as e:
            printTrace('main',e)
            #break;   #remove cmt to reconnect gamepad if posible
            
        time.sleep(2)

if initialize():
    main()



