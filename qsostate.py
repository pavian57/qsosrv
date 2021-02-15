
tlg = ''
tmp1 = ''
tmp2 = ''
tmp3 = ''
callsign1 = ''
callsign2 = ''
r1 = ''
r2 = ''
rst1 = ''
rst2 = ''
rst3 = ''

def state0():
    global tlg
    global tmp1
    
    
    if tmp1 == '':
        tmp1= tlg.strip()
        print ("cq1: "+tmp1)
        return state0
    else:
        if tmp1 == tlg.strip():
            print ("cq2: "+tlg.strip() )
            return state1
        return state0
     

def state1():
    global tlg
    if tlg.strip() == 'de':
        print ("de: "+tlg.strip())
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
            return state3
        return state2
    
  
def state3():
    print('state3')
    return state4
    

'''Chaser confirms receipt of his report and gives one to activator
R R UR RST 559 559 de VK3BQ K '''

def state4():
    print('state4')
    global tlg
    global r1
    global r2
    
    if r1 == '':
        if tlg.strip() == 'r':
            r1 = tlg.strip()
            tmp2 = ''
            print ("r1: "+r1)        
            return state4
    elif tlg.strip() == 'r':
        print ("r2: "+ tlg.strip())
        return state4
    
    if tlg.strip() == 'ur':
        print ("ur: "+ tlg.strip())
        return state5
    return state4
        
def state5():
    global tlg
    if tlg.strip() == 'rst':
        print ("rst")
        return state6    
    return state5


def state6():
    global tlg
    global tmp1
    print (tlg)
    print (tmp1)
    
    if tmp1 == '':
        tmp1 = tlg.strip()
        print ("rst1: "+tlg.strip())
        return state6
    else:
        if tmp1 == tlg.strip():
            print ("rst2: "+tlg.strip() )
            return state7
        return state6
    
def state7():
    
    return state7
    


