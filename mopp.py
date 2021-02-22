
''' class to decode and encode mopp data sent by Morserino 32
    check out this site for more info on this matter.
    http://www.morserino.info/



'''

import math

serial = 44
speed = '0'

class Moppm32:


 # International morse code (sample)
    morse = {
        # Letters
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Punctuation
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
        "<sk>" : "...-.-"
    }

    def __encrypt(self,message):
        cipher = ''
        for letter in message:
            if letter != ' ':

                # Looks up the dictionary and adds the
                # correspponding morse code
                # along with a space to separate
                # morse codes for different characters
                cipher += self.morse[letter] + ' '
            else:
                # 1 space indicates different characters
                # and 2 indicates different words
                cipher += ' '

        return cipher


        # Function to decrypt the string
        # from morse to english
    def __decrypt(self,message):
        i = 0
        # extra space added at the end to access the
        # last morse code
        message += ' '

        decipher = ''
        citext = ''
        try:
            for letter in message:
            # checks for space
                if (letter != ' '):

                    # counter to keep track of space
                    i = 0

                    # storing morse code of a single character
                    citext += letter

                # in case of space
                else:
                    # if i = 1 that indicates a new character
                    i += 1

                    # if i = 2 that indicates a new word
                    if i == 2 :

                            # adding space to separate words
                        decipher += ' '
                    else:

                        # accessing the keys using their values (reverse of encryption)
                        decipher += list(self.morse.keys())[list(self.morse.values()).index(citext)]
                        citext = ''
        except:
            pass

        return decipher

    def hextobin(self,hexstr):

            # Code to convert hex to binary

        n = int(hexstr, 16)
        bStr = ''
        while n > 0:
            bStr = str(n % 2) + bStr
            n = n >> 1
        res = '0' + bStr
        return res

    def __zfr(self,d, chrs, pad):
        # Pads the provided string with trailing 'pad's to suit the specified 
    # 'chrs' length
    # When called, parameters are : d = string, chrs = required length of 
    # string and pad = fill characters
    # The formatted string of correct length and added pad characters is 
    # returned as string

        frmtd_str = str(d)
        while len(frmtd_str) != chrs:
        # less then required characters
            frmtd_str = frmtd_str + pad
        return(frmtd_str)

    def mopptotxt(self,hexstr):

        global speed
        binstr = self.hextobin(hexstr)
        prot = binstr[:2]

        serial = binstr[2:8]
        speed = binstr[8:14]

        length = len(binstr)
        binmcode = binstr[14:length]
        mc = ''
        t1 = ''
        for c in binmcode:
            if c == '0':
                t1 = t1 + c
            if c == '1':
                t1 = t1 + c
            if t1 == '01':
                mc = mc + '.'

                t1 = ''
            if t1 == '10':
                mc = mc + '-'
                t1 = ''
            if t1 == '00':
                mc = mc + ' '
                t1 = ''
            if t1 == '11':
                mc += ' '
                break
        rc = self.__decrypt(mc)
        return rc

    '''
     part of code from https://github.com/sp9wpn/m32_chat_server.
    '''        
    def txttomopp(self,txtstr):
        global serial
        global speed
        serial += 1
        m = '01'                              # protocol
        m += self.__zfr(serial,6,'0')
        m += speed
        for c in txtstr:
            if c == " ":
                continue                          # spaces not supported by morserino!

            for b in self.morse[c.lower()]:
                if b == '.':
                    m += '01'
                else:
                    m += '10'

            m += '00'                           # EOC
        m = m[0:-2] + '11'                    # final EOW

        m = self.__zfr(m,int(8*math.ceil(len(m)/8.0)),'0')

        res = ''

        for i in range (0, len(m), 8):
            res += m[i:i+8]
        return (res)

