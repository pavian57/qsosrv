
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: ruedi kneubuehler hb9fvk@gmx.net

import sys
import time
import socket
import binascii
import qsostate


from  mopp import Moppm32

from callsign import CallGenerator

if  sys.platform == 'esp8266':

    import roger

    from wifi_manager import WifiManager

    WifiManager.setup_network()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_IP = "0.0.0.0"
UDP_PORT = 7373
CLIENT_TIMEOUT = 300
MAX_CLIENTS = 10
KEEPALIVE = 10
DEBUG = 1

receivers = {}



server = (SERVER_IP, UDP_PORT)
sock.bind(server)
print("Listening on " + SERVER_IP + ":" + str(UDP_PORT))
print("Python {} on {}\n".format(sys.version, sys.platform))
translator = Moppm32()
callsign = CallGenerator()
state = qsostate.state0
rufzeichen = ''

print('ready')

'''
easier code int(value,2) does not work with micropython
'''
def sendmoppstr(adr, txtstr):
        sendstr = translator.txttomopp(txtstr)
        splits = [sendstr[x:x + 8] for x in range(0, len(sendstr), 8)]
        frame = bytearray()
        for split in splits:
                value = 0
                t = len(split)
                for i in range (t): 
                        value *= 2   # // double the result so far
                        if split[i] == '1':
                                value +=1 #++; //add 1 if needed
                frame.append(value)  #
        time.sleep(0.2)
        sock.sendto(frame,adr)



def main():

    state = qsostate.state0
    if  sys.platform == 'esp8266':
        roger.roger()
    rc = 0
    while True:
        payload, client_address = sock.recvfrom(64)
#        print(payload)
        b = bytearray(payload)
        hexstr  = binascii.hexlify(b)
        morsecode = translator.mopptotxt(hexstr)
     #   print ('From: ', end ='')
     #   print( client_address)
     #   print('Text: ', end ='')
        print(morsecode)
#        print(state)

        if morsecode.strip() == '<sk>':
                state = qsostate.state20()
        
        if state == qsostate.state0:
                if (morsecode.isdigit()):
                        i = int(morsecode)
                        if i >= 3 or i >=8:
                                callsign.set_call_length(i)
                                if  sys.platform == 'esp8266':
                                    roger.blink(i)
                                        
                   


        if state == qsostate.state0:
                print(state)
                
                if morsecode.strip() == 'cq':
                        qsostate.tlg = morsecode.strip()
                        state = qsostate.state0()   
                        morsecode = '' 
                        
        elif state == qsostate.state1:
                print(state)
                
                if morsecode.strip() == 'de':
                        
                        qsostate.tlg =  morsecode.strip()            
                        state = qsostate.state1()
                        morsecode = ''
                       
        elif state == qsostate.state2:
                print(state)
                
                print (len(morsecode.strip()))
                if len(morsecode) > 3: 
                        qsostate.tlg =  morsecode.strip()            # 1. call
                        state = qsostate.state2()
                        morsecode = ''
                                

        elif state == qsostate.state3:
                print(state)
                
                if morsecode.strip() == 'k':
                        print ("k: "+morsecode.strip())
                        call = callsign.get_call()
                        qsostate.ourcallsign = call
        #                Chaser calls activator
        #                VK3XAS/P de VK3BQ VK3BQ VK3BQ K
                        sendmoppstr(client_address, qsostate.callsign1)
                        qsostate.ourcallsign = call
                        sendmoppstr(client_address, 'de')        
                        sendmoppstr(client_address, call)
                        sendmoppstr(client_address, call)
                        sendmoppstr(client_address, call)
                        sendmoppstr(client_address, 'k')
                        state = qsostate.state3()

        elif state == qsostate.state4:
                print(state)
                if qsostate.ourcallsign == morsecode.strip():
                        qsostate.tlg =  morsecode.strip()  
                        state = qsostate.state4()

                
                      
        elif state == qsostate.state5:    # ur
                print(state)
                if morsecode.strip() == 'ur':   
                        qsostate.tlg =  morsecode.strip()  
                        state = qsostate.state5()

        elif state == qsostate.state6:   # rst             
                print(state)
                qsostate.tlg =  morsecode.strip()
                state = qsostate.state6()
                
        elif state == qsostate.state7:   # 599             
                print(state)
                if len(morsecode) == 3: 
                        qsostate.tlg =  morsecode.strip()
                        state = qsostate.state7()
        
        elif state == qsostate.state8:   # de
                print(state)
                qsostate.tlg =  morsecode.strip()
                state = qsostate.state8()
        
        elif state == qsostate.state9:   # callsign
                print(state)
                qsostate.tlg =  morsecode.strip()
                state = qsostate.state9()

        elif state == qsostate.state10:   # k
                print(state)
                if morsecode.strip() == 'k':
                        print ("k: "+morsecode.strip())
#                        state = qsostate.state9()
                        sendmoppstr(client_address, 'r')                        
                        sendmoppstr(client_address, 'r')                        
                        sendmoppstr(client_address, 'ur')
                        sendmoppstr(client_address, 'rst')
                        rst = callsign.get_rst()
                        sendmoppstr(client_address,rst )
                        sendmoppstr(client_address,rst )
#                        sendmoppstr(client_address,rst )
                        sendmoppstr(client_address, 'de')
                        sendmoppstr(client_address, qsostate.ourcallsign)
                        sendmoppstr(client_address, 'k')
                        state = qsostate.state10()

        elif state == qsostate.state11:   # 
                print(state)
                if morsecode.strip() == 'rr':   
                        qsostate.tlg =  morsecode.strip()  
                        state = qsostate.state11()

        
        elif state == qsostate.state12:   # 
                print(state)
                if morsecode.strip() == 'tu':   
                        qsostate.tlg =  morsecode.strip()  
                        state = qsostate.state12()


        elif state == qsostate.state13:   # 
                print(state)
                if morsecode.strip() == '73':   
                        qsostate.tlg =  morsecode.strip()  
                        state = qsostate.state13()

        elif state == qsostate.state14:   # 
                print(state)
                if morsecode.strip() == 'de':   
                        qsostate.tlg =  morsecode.strip()  
                        state = qsostate.state14()

        elif state == qsostate.state15:   # 
                print(state)
               
                qsostate.tlg =  morsecode.strip()  
                state = qsostate.state15()

        elif state == qsostate.state16:   # 
                print(state)
                if morsecode.strip() == 'ee':   
                        print ("ee: "+morsecode.strip())
                        if  sys.platform == 'esp8266':
                            roger.roger()
                        qsostate.tmp1 = ''  
                        sendmoppstr(client_address, '73')
                        state = qsostate.state16()
        
        



if __name__=="__main__":
    main()
