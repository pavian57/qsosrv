# Simple Morserino-32 QSO Server by hb9fvk (ruedi)

This is a small program in Micropython on esp8266 to run a kind of qso server for Morserino-32. https://github.com/oe1wkl/Morserino-32

i used VS Code with PyMakr to Upload Code to a esp8266 Wemos mini D1. Adjust your Wifi Settings. Start your Morserino, send 'hi' and it will send you back a random callsign , followed with ur rst and 3 times a report. 

I will add more features from time to time.

qso follows the rules of: https://www.emdrc.com.au/basics-of-a-cw-qso/

you: Morserino

he: qsosrv

you: cq cq de **yourcallsign** k


he: **yourcallsign** de **hiscallsign**  **hiscallsign** **hiscallsign** k


you: **hiscallsign** ur rst **hisrst** **hisrst** de **yourcallsign**


he: r r ur rst **yourst** **yourst**  **yourst** de **hiscallsign** k


you: rr tu 73 de **yourcallsign** ee


entering **sk** goes back to step 0




You're invited to help out with this small project.

73 de hb9fvk (ruedi)

