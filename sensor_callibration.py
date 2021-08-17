import machine
import time
import ssd1306
import tcs34725
import si1145
from machine import I2C, Pin, PWM
import controller_screen
import utils_constants
import controller_motor
import controller_sensor as cs

#defining the RGB LED pins. The given LED colour is on when the pin is off()

r=Pin(utils_constants.R_PIN,Pin.OUT,Pin.PULL_UP)

g=Pin(utils_constants.G_PIN,Pin.OUT,Pin.PULL_UP)

b=Pin(utils_constants.B_PIN,Pin.OUT,Pin.PULL_UP)

r.on()
g.on()
b.on()

# Define rgb sensor
sensor = tcs34725.TCS34725(i2c)
sensor.integration_time(utils_constants.SENSOR_INTEGRATION_TIME) #value between 2.4 and 614.4.
sensor.gain(utils_constants.SENSOR_GAIN) #must be a value of 1, 4, 16, 60

#set upthe 

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
    #return (red, green, blue, int(r), int(g), int(b), int(clear))
    return [int(r), int(g), int(b)]

# Define I2C
i2c = I2C(scl=Pin(22), sda=Pin(23), freq=100000)
pin25=machine.Pin(25,Pin.OUT) #not sure what this does
pin25.off()
x = 0
rate = 30

# Define oled
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

def test():
    result=[]
    #turn all lights off
    r.on()
    g.on()
    b.on()
    #measure single colour:
    for i in [r,g,b]:
        i.off()
        time.sleep(1)
        print(str(i) + " on")
        test=cs.measure()
        result.append(test)
        #result.append(str(i) + " on")
        i.on()
        time.sleep(0.5)

    r.off()
    g.off()
    b.off()

    for i in [r,g,b]:
        i.on()
        time.sleep(1)
        print(str(i) + "is off, others are on")
        test=cs.measure()
        result.append(test)
        #result.append(str(i) + "off")
        i.off()
        time.sleep(0.5)
    r.off()
    g.off()
    b.off()
    time.sleep(1)
    print("all on")

    test=cs.measure()
    result.append(test)
    return(result)


def measure():
    values_list = [0,0,0]

    for i in range(utils_constants.N_RGB_MEASUREMENTS):
        temp=color_rgb_bytes_new(sensor.read(True))
        for j in range(3):
            values_list[j]=values_list[j]+temp[j]

    for k in range(3):
            values_list[k]=int(values_list[k]/utils_constants.N_RGB_MEASUREMENTS)

    #(r_value,g_value,b_value)=(r_value,g_value,b_value)/utils_constants.N_RGB_MEASUREMENTS

    # answer = 'r:{} g:{} b:{}<'.format(r_value,g_value,b_value)
    # controller_screen.print_new_line("sensor measurement:")
    # controller_screen.print_new_line(answer)
    # controller_screen.print_new_line("\n")
    print(" R: G:  B: ")
    print(values_list, end='\n')
    return values_list