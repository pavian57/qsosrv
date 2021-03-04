
class State:
        CQ = 1
        DE = 5
        CALLSIGN = 7
        K	= 9
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
    lencall = 3
    sota = 0

    
    def __init__(self, functions):
        self.functions = functions
    
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
            if len(self.cqlist) >= self.lencall and len(self.sotalist) >= self.lencall:
                return State.DE
            return State.CQ
        elif len(self.cqlist) >= self.lencall:
            return State.DE
        return State.CQ
    

    def de(self,tlg):
        if tlg == 'de':
            print(":de")
            # return the next state
            return State.CALLSIGN
        return State.DE

    def callsign(self,tlg):
        if len(tlg) >= self.lencall:
            if len(self.callsignlist) == 0:
                self.callsignlist.append(tlg)
            elif tlg == self.callsignlist[0]:
                print(':'+tlg)
                self.callsignlist.append(tlg)
        if len(self.callsignlist) >= self.lencall:
                # return the next state
            return State.K
        return State.CALLSIGN
       
    def k(self,tlg):
        if tlg == 'k':
            print(":k")
            return State.CHASE
        return State.K
    
    def ourcallsign(self,tlg):
        if tlg == self.urcallsign:
            print(':'+str(self.urcallsign))
            return State.UR
        return State.OURCALLSIGN
    
    def ur(self,tlg):
        if tlg == 'ur':
            print(':ur')
            return State.RST
        return State.UR


    def rst(self,tlg):
        if tlg == 'rst':
            print(':rst')
            return State.REPORT
        return State.RST
        
    def report(self,tlg):
        if len(tlg) >= 3:
            self.tmplist.append(tlg)
            print(':'+tlg)
        if len(self.tmplist) >= 1:
                # return the next state
            return State.REPORTDE
        return State.REPORT
    
    def reportde(self,tlg):
        if tlg == 'de':
            print(":de")
            # return the next state
            return State.REPORTCALL
        return State.REPORTDE


    def reportcall(self,tlg):
        if tlg == self.callsignlist[0]:
            print(':'+str(self.callsignlist[0]))
            return State.REPORTK
        return State.REPORTCALL        
    

    def reportk(self,tlg):
        if tlg == 'k':
            print(":k")
            return State.REPORTCHASE
        return State.REPORTK
        
    def byerr(self,tlg):
        if tlg == 'rr':
            print(":rr")
            # return the next state
            return State.BYETU
        return State.BYEUR
        
    def byetu(self,tlg):
        if tlg == 'tu':
            print(":tu")
            # return the next state
            return State.BYE73
        return State.BYETU
    
    
    def bye73(self,tlg):
        if tlg == '73':
            print(":73")
            # return the next state
            return State.BYEDE
        return State.BYE73
        
    
    def byede(self,tlg):
        if tlg == 'de':
            print(":de")
            # return the next state
            return State.BYECALL
        return State.BYEDE
        
    def byecall(self,tlg):
        if tlg == self.callsignlist[0]:
            print(':'+str(self.callsignlist[0]))
            return State.BYEEE
        return State.BYECALL
        
    def byeee(self,tlg):
        if tlg == 'ee':
            print(":ee")
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
