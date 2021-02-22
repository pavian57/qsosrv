import machine
import time

LED_PIN = 2  # D4
led = machine.Pin(LED_PIN, machine.Pin.OUT)


def dot():
    led.on()
    led.off()
    time.sleep(0.3)
    led.on()
    time.sleep(0.3)

def dash():
    led.on()
    led.off()
    time.sleep(0.9)
    led.on()
    time.sleep(0.3)



def roger():
    led.off()
    dot()
    dash()
    dot()