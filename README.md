# Simple Morserino-32 QSO Server by hb9fvk (ruedi)

This is a small program in Micropython on esp8266 to run a kind of qso server for Morserino-32. https://github.com/oe1wkl/Morserino-32

i used VS Code with PyMakr to Upload Code to a esp8266 Wemos mini D1. Adjust your Wifi Settings. Start your Morserino in WifiTrx and follow the procedure below. The qsosrv sends back a random callsign, lenght=3 at the moment, you may change by your own, or send a number **i >= 3 or i >=8** before sending **cq**. 

I will add more features from time to time.

qso follows the rules of: https://www.emdrc.com.au/basics-of-a-cw-qso/

you: Morserino

he: qsosrv

you: cq **sota** cq **sota** cq **sota** de **yourcallsign** **yourcallsign** **yourcallsign** k

**sota** ist optional

he: **yourcallsign** de **hiscallsign**  **hiscallsign** **hiscallsign** k


you: **hiscallsign** ur rst **hisrst** **hisrst** **hisrst** de **yourcallsign**


he: r r ur rst **yourst** **yourst**  **yourst** de **hiscallsign** k


you: rr tu 73 de **yourcallsign** ee


entering **sk** goes back to step 0


on a esp8266 **qsosrv** blinks after every step **.-.** **roger**. 

It runs on Linux(tested on Raspberry Pi 4), Windows (Python 3.9 on Windows 10) and last but not least on a esp8266 with Micropython, this allows you to be portable with Morserino and esp8266.

You're invited to help out with this small project.

73 de hb9fvk (ruedi)

