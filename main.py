
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: ruedi kneubuehler hb9fvk@gmx.net

import sys
import time
import socket
import binascii

from qsostate import State

from qsostate import Qsostate

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

# map the states to action functions          
# map the states to action functions          


action = {
    State.CQ : 'cq',
    State.DE : 'de',
    State.CALLSIGN : 'callsign',
    State.K : 'k',
    State.CHASE: 'k',
    State.OURCALLSIGN : 'ourcallsign',
    State.UR : 'ur',
    State.RST : 'rst',
    State.REPORT :'report',
    State.REPORTDE :'reportde',
    State.REPORTCALL :'reportcall',
    State.REPORTK : 'reportk',
    State.REPORTCHASE : 'reportk',
    State.BYERR : 'byerr',
    State.BYETU : 'byetu',
    State.BYE73 : 'bye73',
    State.BYEDE : 'byede',
    State.BYECALL : 'byecall',
    State.BYEEE : 'byeee',
    State.END : 'end'
}

qso = Qsostate(action)


receivers = {}



server = (SERVER_IP, UDP_PORT)
sock.bind(server)
print("Listening on " + SERVER_IP + ":" + str(UDP_PORT))
print("Python {} on {}\n".format(sys.version, sys.platform))
translator = Moppm32()
callsign = CallGenerator()

print('ready')


DEBUG = False

def log(s):
    if DEBUG:
        print(s)


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

    if  sys.platform == 'esp8266':
        roger.roger()
    rc = 0

    state = State.CQ
    
    while True:
        payload, client_address = sock.recvfrom(64)
        b = bytearray(payload)
        hexstr  = binascii.hexlify(b)
        morsecode = translator.mopptotxt(hexstr)
        tlg = morsecode.strip()
     #   print ('From: ', end ='')
     #   print( client_address)
     #   print('Text: ', end ='')
        log('<'+morsecode+'>')
        # call the designated function and update the state

# <sk> break and go to end

        if morsecode.strip() == '<sk>':
            print(':<sk> bye')
            state = State.END
        
        state = qso.run_func(state,tlg)
        log(state)
        
        if state == State.CHASE:
                
            qso.urcallsign = callsign.get_call()
#                Chaser calls activator
#                VK3XAS/P de VK3BQ VK3BQ VK3BQ K
            sendmoppstr(client_address, qso.callsignlist[0])
            sendmoppstr(client_address, 'de')        
            sendmoppstr(client_address, qso.urcallsign)
            sendmoppstr(client_address, qso.urcallsign)
            sendmoppstr(client_address, qso.urcallsign)
            sendmoppstr(client_address, 'k')
            state = State.OURCALLSIGN

#Chaser confirms receipt of his report and gives one to activator
# R R UR RST 559 559 de VK3BQ K

        if state == State.REPORTCHASE:
            
            sendmoppstr(client_address, 'r')                        
            sendmoppstr(client_address, 'r')                        
            sendmoppstr(client_address, 'ur')
            sendmoppstr(client_address, 'rst')
            rst = callsign.get_rst()
            sendmoppstr(client_address,rst )
            sendmoppstr(client_address,rst )
            sendmoppstr(client_address,rst )
            sendmoppstr(client_address, 'de')
            sendmoppstr(client_address, qso.urcallsign)
            sendmoppstr(client_address, 'k')
            state = State.BYERR

# Chaser may then send 73            
        if state == State.END:
            sendmoppstr(client_address, '73')
            state = State.CQ
        

        

if __name__=="__main__":
    main()
