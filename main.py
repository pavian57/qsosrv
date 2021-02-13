
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: ruedi kneubuehler hb9fvk@gmx.net

import sys
import socket
import binascii

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

print('ready')



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


    while True:
        payload, client_address = sock.recvfrom(64)
        print(payload)
        b = bytearray(payload)
        hexstr  = binascii.hexlify(b)
#        hexstr = payload.hex()
        print(hexstr)

        morsecode = translator.mopptotxt(hexstr)
        print ('From: ', end ='')
        print( client_address)
        print('Text: ', end ='')
        print(morsecode)
        if morsecode.strip() == 'hi':
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
        

if __name__=="__main__":
    main()
