"""
   Controls the cooling unit.
"""

from machine import Pin
from time import sleep
import utils_constants as constants

_relay = Pin(constants.COOLER_PIN, Pin.OUT)
_relay.value(0)
is_started = False

def start():
  is_started = True
  _relay.value(1)

def stop():
  is_started = False
  _relay.value(0)

