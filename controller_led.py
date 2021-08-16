"""
   Controls the led.
"""

from machine import Pin
import time
import utils_constants

r=Pin(utils_constants.R_PIN,Pin.OUT,Pin.PULL_UP)

g=Pin(utils_constants.G_PIN,Pin.OUT,Pin.PULL_UP)

b=Pin(utils_constants.B_PIN,Pin.OUT,Pin.PULL_UP)

r.on()
g.on()
b.on()

is_started = False

def on():
  is_started = True
  r.off()
  g.off()
  b.off()
  

def off():
  is_started = False
  r.on()
  g.on()
  b.on()

def rave():
    r.off()
    g.off()
    b.off()
    while True:
        for i in [r,g,b]:
            i.on()
            time.sleep(0.01)
            for j in [r,g,b]:
                j.on()
                time.sleep(0.01)
                j.off()
            i.off()