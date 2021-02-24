from random import *

class CallGenerator():

    
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #0-25 
    numbers = ['1','2','3','4','5','6','7','8','9','n']
    #0-9
    allchars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    #0-35

   

    def __randrange(self,start, stop=None):
        global bits
        global pwr2
        if stop is None:
            stop = start
            start = 0
        upper = stop - start
        bits = 0
        pwr2 = 1
        while upper > pwr2:
            pwr2 <<= 1
            bits += 1
        while True:
            r = getrandbits(bits)
            if r < upper:
                break
        return r + start

    """a simple and easy to use password generator"""
    def __init__(self):
        self.call_length = 3

    def set_call_length(self,size):
        self.call_length = size

    def get_rst(self):
        cs = ''
        cs = self.numbers[self.__randrange(0,4) ]
        for i in range(2):
            cs += self.numbers[self.__randrange(0,9) ]
        return cs


    def get_call(self):
        cs = ''
        cs = self.chars[self.__randrange(0,25) ]
        for i in range(self.call_length-1):
            cs += self.allchars [self.__randrange(0,35) ]
        return cs 
        

