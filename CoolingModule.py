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