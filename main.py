
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: ruedi kneubuehler hb9fvk@gmx.net

import sys
import socket
import binascii
import qsostate
import roger

from  mopp import Moppm32

from callsign import CallGenerator

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
        sock.sendto(frame,adr)



def main():

    state = qsostate.state0
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
     #   print(morsecode)
        print(state)
        
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
                
                if len(morsecode) > 2: 
                        if len(morsecode) > 2 and  morsecode.strip() != '':
                                qsostate.tlg =  morsecode.strip()            # 1. call
                                state = qsostate.state2()
                                morsecode = ''
                                

        elif state == qsostate.state3:
                print(state)
                
                if morsecode.strip() == 'k':
#                        qsostate.tlg =  morsecode.strip()            # k
#                        state = qsostate.state3()
                        morsecode = ''
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
                        state = qsostate.state4()

                
                      
        elif state == qsostate.state5:    # ur
                print(state)
                if morsecode.strip() == 'ur':   
                        state = qsostate.state5()

        elif state == qsostate.state6:   # rst             
                print(state)
                qsostate.tlg =  morsecode.strip()
                state = qsostate.state6()
                
        elif state == qsostate.state7:   # rst             
                print(state)
                qsostate.tlg =  morsecode.strip()
                state = qsostate.state6()
        
        elif state == qsostate.state8:   # hiscakk
                print(state)
                qsostate.tlg =  morsecode.strip()
                state = qsostate.state6()
        
        elif state == qsostate.state9:   # k
                print(state)
                if morsecode.strip() == 'k':
                        state = qsostate.state6()
                        sendmoppstr(client_address, 'r')                        
                        sendmoppstr(client_address, 'r')                        
                        sendmoppstr(client_address, 'ur')
                        sendmoppstr(client_address, 'rst')
                        rst = callsign.get_rst()
                        sendmoppstr(client_address,rst )
                        sendmoppstr(client_address,rst )
#                        sendmoppstr(client_address,rst )
                        sendmoppstr(client_address, 'de')
                        sendmoppstr(client_address, qsostate.callsign1)
                        sendmoppstr(client_address, 'k')

                '''

                Chaser calls activator
                VK3XAS/P de VK3BQ VK3BQ VK3BQ K

                Activator replies with a report for the chaser
                VK3BQ ur rst 579 579 579 DE VK3XAS/P K
                if morsecode.strip() != '':
                        qsostate.tlg =  morsecode.strip()            # k
                        state = qsostate.state1()
                        morsecode = ''

                if morsecode.strip() == 'k':
                '''        
'''                         
                        call = callsign.get_call()
                        sendmoppstr(client_address, call)
                        sendmoppstr(client_address, call)

                        sendmoppstr(client_address, 'ur')
                        sendmoppstr(client_address, 'rst')
                        rst = callsign.get_rst()
                        sendmoppstr(client_address,rst )
                        sendmoppstr(client_address,rst )
                        sendmoppstr(client_address,rst )
                        sendmoppstr(client_address,'73' )
                        state = qsostate.state3()
        

'''

if __name__=="__main__":
    main()
