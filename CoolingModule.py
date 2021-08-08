from machine import Pin
from time import sleep

# ESP32 GPIO 33
relay = Pin(33, Pin.OUT)

while True:
  # RELAY ON
  relay.value(0)
  sleep(10)
  # RELAY OFF
  relay.value(1)
  sleep(10)


from machine import Pin
import time

pin27 = Pin(27, Pin.OUT)


while True:
  pin27.value(1)
  time.sleep(0.001)
  pin27.value(0)
  time.sleep(0.001)