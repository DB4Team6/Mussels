"""
   Controls the led.
"""

from machine import Pin
from time import sleep
import utils_constants as constants

_led = Pin(constants.LED_PIN, Pin.OUT)
_led.value(0)
is_started = False

def start():
  is_started = True
  _led.value(1)

def stop():
  is_started = False
  _led.value(0)
