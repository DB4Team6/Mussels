import machine
import time
from machine import Pin
pin25=machine.Pin(15,Pin.OUT)
pin25.off()
import ssd1306
import tcs34725
import si1145
from machine import I2C, Pin, PWM

color1=Pin(26,Pin.OUT,Pin.PULL_UP)
blue=color1
color2=Pin(25,Pin.OUT,Pin.PULL_UP)
blue.off()
blue.on()
green=color2
color3=Pin(4,Pin.OUT,Pin.PULL_UP)
color3.on()
red=color3


def color_rgb_bytes_new(color_raw):
    """Read the RGB color detected by the sensor.  Returns a 3-tuple of
    red, green, blue component values as bytes (0-255).
    """
    r, g, b, clear = color_raw
    # Avoid divide by zero errors ... if clear = 0 return black
    if clear == 0:
        return (0, 0, 0)
    red   = int(pow((int((r/clear) * 256) / 255), 2.5) * 255)
    green = int(pow((int((g/clear) * 256) / 255), 2.5) * 255)
    blue  = int(pow((int((b/clear) * 256) / 255), 2.5) * 255)
    # Handle possible 8-bit overflow
    if red > 255:
        red = 255
    if green > 255:
        green = 255
    if blue > 255:
        blue = 255
    return (red, green, blue, int(r), int(g), int(b), int(clear))





# Define I2C
i2c = I2C(scl=Pin(22), sda=Pin(23), freq=100000)
pin25=machine.Pin(25,Pin.OUT)
pin25.off()
x = 0
rate = 30

# Define oled
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

# Define rgb sensor
sensor = tcs34725.TCS34725(i2c)
sensor.integration_time(10) #value between 2.4 and 614.4.
sensor.gain(16) #must be a value of 1, 4, 16, 60



def measure():
    
    for i in range(20):
        r,g,b = color_rgb_bytes(sensor.read(True))
        time.sleep(0.2)
        oled.fill(0)
        oled.text('R: {}'.format(r), 0, 8)
        oled.text('G: {}'.format(g), 0, 16)
        oled.text('B: {}'.format(b), 0, 24)
        oled.show()
    answer = '>r:{} g:{} b:{}<'.format(r, g, b)
    print(answer, end='\n')