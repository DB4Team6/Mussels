import machine
import time
pin = machine.Pin(13, machine.Pin.OUT)
def blink():
    while 1:
        pin.on()
        time.sleep(1)
        pin.off()
        time.sleep(1)
blink()