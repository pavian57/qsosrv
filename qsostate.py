import sys
if  sys.platform == 'esp8266':  
    import roger

class State:
        CQ = 1
        DE = 5
        CALLSIGN = 7
        K	= 9
        PSE = 10
        CHASE = 11
        OURCALLSIGN	= 13
    
        UR	= 15
        RST	= 17
        REPORT = 19
        REPORTDE = 21
        REPORTCALL = 23
        REPORTK = 25
        REPORTCHASE = 27
    
        BYERR = 29
        BYETU = 31
        BYE73 = 33
        BYEDE = 35
        BYECALL = 37
        BYEEE = 39
        END = 41
    
        SK = 100

    

    
    
    
    

class Qsostate:

    cqlist = []
    sotalist = []
    callsignlist = []
    tmplist = []
    urcallsign = ''
    lencall = 5
    numberofcq = 3
    sota = 0

    
    def __init__(self, functions):
        self.functions = functions

    def is_number(self,n):
        try:
            float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`,
                   # it'll raise `ValueError` exception
        except ValueError:
            return False
        return True


    def check_rst(self,rst):            
        if self.is_number(rst[0]):            
            if self.is_number(rst[1]) or str(rst[1]) == 'n':
                if self.is_number(rst[2]) or str(rst[2]) == 'n':                  
                    return True
        return False
    
# define some action functions
    def cq(self,tlg):

        if tlg == 'cq':
            print(":cq")
            self.cqlist.append(tlg)
        if tlg == 'sota':
            print(":sota")
            self.sota = 1
            self.sotalist.append(tlg)
        if self.sota == 1:
            if len(self.cqlist) >= self.numberofcq and len(self.sotalist) >= self.numberofcq:
                if  sys.platform == 'esp8266': roger.roger()
                return State.DE
            return State.CQ
        elif len(self.cqlist) >= self.numberofcq:
            if  sys.platform == 'esp8266': roger.roger()
            return State.DE
        return State.CQ
    

    def de(self,tlg):
        if tlg == 'de':
            print(":de")
            # return the next state
            if  sys.platform == 'esp8266': roger.roger()
            return State.CALLSIGN
        return State.DE

    def callsign(self,tlg):
        if len(tlg) >= self.lencall:
            if len(self.callsignlist) == 0:
                print(':'+tlg)
                self.callsignlist.append(tlg)
            elif tlg == self.callsignlist[0]:
                print(':'+tlg)
                self.callsignlist.append(tlg)
        if len(self.callsignlist) >= self.numberofcq:
                # return the next state
            if  sys.platform == 'esp8266': roger.roger()
            return State.PSE
        return State.CALLSIGN

    def pse(self,tlg):
        if tlg == 'pse':
            print(":pse")
            # return the next state
            if  sys.platform == 'esp8266': roger.roger()
            return State.K
        return State.PSE
       
    def k(self,tlg):
        if tlg == 'k':
            print(":k")
            if  sys.platform == 'esp8266': roger.roger()
            return State.CHASE
        return State.K
    
    def ourcallsign(self,tlg):
        if tlg == self.urcallsign:
            print(':'+str(self.urcallsign))
            if  sys.platform == 'esp8266': roger.roger()
            return State.UR
        return State.OURCALLSIGN
    
    def ur(self,tlg):
        if tlg == 'ur':
            print(':ur')
            if  sys.platform == 'esp8266': roger.roger()
            return State.RST
        return State.UR


    def rst(self,tlg):
        if tlg == 'rst':
            print(':rst')
            if  sys.platform == 'esp8266': roger.roger()
            return State.REPORT
        return State.RST
        
    def report(self,tlg):
        if len(tlg) >= 3:
            if self.check_rst(tlg): 
                self.tmplist.append(tlg)
                print(':'+tlg)
                if len(self.tmplist) >= self.numberofcq:
                # return the next state
                    if  sys.platform == 'esp8266': roger.roger()
                    return State.REPORTDE            
        return State.REPORT
    
    def reportde(self,tlg):
        if tlg == 'de':
            print(":de")
            # return the next state
            if  sys.platform == 'esp8266': roger.roger()
            return State.REPORTCALL
        return State.REPORTDE


    def reportcall(self,tlg):
        if tlg == self.callsignlist[0]:
            print(':'+str(self.callsignlist[0]))
            if  sys.platform == 'esp8266': roger.roger()
            return State.REPORTK
        return State.REPORTCALL        
    

    def reportk(self,tlg):
        if tlg == 'k':
            print(":k")
            if  sys.platform == 'esp8266': roger.roger()
            return State.REPORTCHASE
        return State.REPORTK
        
    def byerr(self,tlg):
        if tlg == 'rr':
            print(":rr")
            if  sys.platform == 'esp8266': roger.roger()
            # return the next state
            return State.BYETU
        return State.BYERR
        
    def byetu(self,tlg):
        if tlg == 'tu':
            print(":tu")
            if  sys.platform == 'esp8266': roger.roger()
            # return the next state
            return State.BYE73
        return State.BYETU
    
    
    def bye73(self,tlg):
        if tlg == '73':
            print(":73")
            # return the next state
            if  sys.platform == 'esp8266': roger.roger()
            return State.BYEDE
        return State.BYE73
        
    
    def byede(self,tlg):
        if tlg == 'de':
            print(":de")
            if  sys.platform == 'esp8266': roger.roger()
            # return the next state
            return State.BYECALL
        return State.BYEDE
        
    def byecall(self,tlg):
        if tlg == self.callsignlist[0]:
            print(':'+str(self.callsignlist[0]))
            if  sys.platform == 'esp8266': roger.roger()
            return State.BYEEE
        return State.BYECALL
        
    def byeee(self,tlg):
        if tlg == 'ee':
            print(":ee")
            if  sys.platform == 'esp8266': roger.roger()
            return State.END
        return State.BYEEE
    
    def end(self, tlg):
        self.cqlist = []
        self.callsignlist = []
        self.tmplist = []
        urcallsign = ''            
        return State.END
        



  
    
    


    def run_func(self, func_key, *args, **kwargs):
        func_name = self.functions.get(func_key)
        if func_name and hasattr(self, func_name):
            return getattr(self, func_name)(*args, **kwargs)
        else:
            return None
