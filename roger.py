import machine
import time

LED_PIN = 2  # D4
led = machine.Pin(LED_PIN, machine.Pin.OUT)


def dot():
    led.off()
    time.sleep(0.15)
    led.on()
    time.sleep(0.15)

def dash():
    led.off()
    time.sleep(0.45)
    led.on()
    time.sleep(0.15)
    



def roger():
    led.off()
    dot()
    dash()
    dot()

def blink3():
    dot()
    dot()
    dot()
    dash()
    dash()

def blink4():
    dot()
    dot()
    dot()
    dot()
    dash()


def blink5():
    dot()
    dot()
    dot()
    dot()
    dot()

def blink6():
    dash()
    dot()
    dot()
    dot()
    dot()

def blink7():
    dash()
    dash()
    dot()
    dot()
    dot()

def blink8():
    dash()
    dash()
    dash()
    dot()
    dot()

def blink(i):
    if i == 3:
        blink3()
    elif i == 4:
        blink4()
    elif i == 5:
        blink5()
    elif i == 6:
        blink6()
    elif i == 7:
        blink7()
    elif i == 8:
        blink8
