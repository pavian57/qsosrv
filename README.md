# Simple Morserino-32 QSO Server by hb9fvk (ruedi)

This is a small program in Python/MicroPython that creates a QSO server for the [Morserio-32](https://www.morserino.info/).

It can be used to train realistic QSOs with the [Morserio-32](https://www.morserino.info/).

The QSO follows the rules of https://www.emdrc.com.au/basics-of-a-cw-qso/.
The qsosrv application sends back a random callsign. The length of the callsign is currently set to 5 characters. This can be changed by sending a number **i >= 3 or i >=8** before sending **cq** (TBD, wording still unclear). 

```
you: Morserino
he: qsosrv
you: cq **sota** cq **sota** cq **sota** de **yourcallsign** **yourcallsign** **yourcallsign** k
```
**sota** ist optional
```
he: **yourcallsign** de **hiscallsign**  **hiscallsign** **hiscallsign** k
you: **hiscallsign** ur rst **hisrst** **hisrst** **hisrst** de **yourcallsign**
he: r r ur rst **yourst** **yourst**  **yourst** de **hiscallsign** k
you: rr tu 73 de **yourcallsign** ee
```

Entering `**sk**` goes back to the first step.
On an ESP8266 **qsosrv** blinks after every step **.-.** **roger**. 


## Requirements
It runs on Linux (tested on Raspberry Pi 4), Windows (Python 3.9 on Windows 10), and last but not least on an ESP8266 with Micropython, this allows you to be portable with the Morserino and an ESP8266.

**Software**
- Python 3.x (?) or MicroPython

**Hardware**
- Morserino-32 with firmware > nn.zz
- ESP8266 Microcontroller or any Linux/Windows/OSX machine

## Installation

First, you have to fetch the source code from GitHub. 

`git clone https://github.com/mfhepp/qsosrv.git`

You can also download a ZIP file from Github

`Code -> Download ZIP`

and unzip it.

### Linux / Raspberry Pi
Make sure a Python interpreter > version 3.x. is installed. This is the default on Raspbian. If unsure, see e.g. [this page](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux).

```
cd qsosrv
python main.py
```

### Windows

### OSX
Make sure a Python interpreter > version 3.x is installed. If unsure, see e.g. [this page](https://opensource.com/article/19/5/python-3-default-mac). A simple and clean way is installing the [Anaconda package](https://www.anaconda.com/products/individual]).

```
cd qsosrv
python main.py
```

### ESP8266 / MicroPython
I used VS Code with PyMakr to Upload Code to a esp8266 Wemos mini D1. After successfully uploading the code to the ESP8266, simply reset the device.

## Set-up

1. Connect the ESP8266, Raspberry Pi or your computer with the Morserino (TBD: How exactly?)
2. Adjust your Wifi Settings.
3. Update the configuration as needed (TBD). 
3. Start your Morserino in WifiTrx and follow the procedure below (TBD). 

## Future Improvements
I will add more features from time to time.
Next step will be adding a small oled display.

## Contact and Community
- [Morserion-32 on GitHub](https://github.com/oe1wkl/Morserino-32)
- [Morserino User Group](https://morserino.groups.io/g/main)
- [Morserino Mailing List (powered by MailChimp)](https://morserino.us12.list-manage.com/subscribe?u=0d5ec4ca254b61e7b1d5a4cee&id=a3025f6948)



73 de hb9fvk (ruedi)

