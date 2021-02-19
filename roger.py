import machine
import time

LED_PIN = 2  # D4
led = machine.Pin(LED_PIN, machine.Pin.OUT)


def dot():
    led.on()
    led.off()
    time.sleep(0.5)
    led.on()
    time.sleep(0.5)

def dash():
    led.on()
    led.off()
    time.sleep(1.5)
    led.on()
    time.sleep(0.5)



def roger():
    led.off()
    dot()
    dash()
    dot()