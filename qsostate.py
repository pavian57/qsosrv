import roger

tlg = ''
tmp1 = ''
tmp2 = ''
tmp3 = ''
callsign1 = ''
callsign2 = ''
ourcallsign = ''
r1 = ''
r2 = ''
rst1 = ''
rst2 = ''
rst3 = ''

def state0():
    global tlg
    global tmp1
    print('0')
    print('tmp1: '+tmp1)
    if tmp1 == '':
        tmp1= tlg.strip()
        print ("cq1: "+tmp1)
        return state0
    else:
        if tmp1 == tlg.strip():
            print ("cq2: "+tlg.strip())
            roger.roger()
            tmp1 = ''
            return state1
        return state0
     

def state1():
    global tlg
    if tlg.strip() == 'de':
        print ("de: "+tlg.strip())
        roger.roger()
        return state2
    return state1    

def state2():
    global tlg
    global callsign1
    global callsign2
    
    # delay and decision path to simulate some application logic
    if callsign1 == '':
        callsign1 = tlg.strip()
        print ("callsign1: "+callsign1)
        return state2
    else:
        if callsign1 == tlg.strip():
            callsign2 = tlg.strip() 
            print ("callsign2: "+callsign2)
            roger.roger()
            return state3
        return state2
    
  
def state3():
   # chaser VK3XAS/P de VK3BQ VK3BQ VK3BQ K
    roger.roger()
    return state4
    

'''Activator replies with a report for the chaser
VK3BQ ur rst 579 579 579 DE VK3XAS/P K '''

def state4(): 
    print ("ourcallsign: "+tlg.strip())
    #our callsign okay
    roger.roger()
    return state5

def state5():
    print('ur: '+tlg.strip())
    # ur
    roger.roger()
    return state6

def state6():
    global tlg
    if tlg.strip() == 'rst':
        print ("rst: "+tlg.strip())
        roger.roger()

        return state7    
    return state6


def state7():
    global tlg
    global tmp1
    print ('tmp1: '+tmp1)
    if tmp1 == '':
        tmp1 = tlg.strip()
        print ("rst1: "+tlg.strip())
        return state7
    else:
        if tmp1 == tlg.strip():
            print ("rst2: "+tlg.strip() )
            roger.roger()
            return state8
        return state7
    return state7
    
def state8():
    global tlg
    if tlg.strip() == 'de':
        print ("de: "+tlg.strip())
        tmp1 = ''
        roger.roger()
        return state9
    return state8
    

def state9():
    global tlg
    global callsign1

    if tlg.strip() == callsign1:
        print ("callsign: "+tlg.strip())
        roger.roger()
        return state10
    return state9

def state10():
    roger.roger()
    return state11

def state11():
    if tlg.strip() == 'rr':
        print ("rr: "+tlg.strip())
        roger.roger()
        return state12
    return state11

def state12():
    if tlg.strip() == 'tu':
        print ("tu: "+tlg.strip())
        roger.roger()
        return state13
    return state12

def state13():
    if tlg.strip() == '73':
        print ("73: "+tlg.strip())
        roger.roger()
        return state14
    return state13

def state14():
    if tlg.strip() == 'de':
        print ("de: "+tlg.strip())
        roger.roger()
        return state15
    return state14

def state15():
    global tlg
    global callsign1
    if tlg.strip() == callsign1:
        print ("callsign: "+tlg.strip())
        roger.roger()
        return state16
    return state15


def state16():
    return state0
    

'''RR TU 73 de VK3XAS/P EE '''
def state20():   #<sk>
    global tmp1
    roger.roger()
    roger.roger()
    tmp1 = ''
    return state0
    
