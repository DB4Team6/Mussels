import machine
import time
import ssd1306
import tcs34725
import si1145
from machine import I2C, Pin, PWM
import controller_screen
import utils_constants
import controller_motor
import controller_led

# Define I2C
i2c = I2C(scl=Pin(22), sda=Pin(23), freq=100000)

# Define rgb sensor
sensor = tcs34725.TCS34725(i2c)
sensor.integration_time(utils_constants.SENSOR_INTEGRATION_TIME) #value between 2.4 and 614.4.
sensor.gain(utils_constants.SENSOR_GAIN) #must be a value of 1, 4, 16, 60




def color_rgb_bytes_new(color_raw):
  
    r, g, b, clear = color_raw
 
    #return (red, green, blue, int(r), int(g), int(b), int(clear))
    return [int(r), int(g), int(b)]

def measure():

    controller_led.on()

    values_list = [0,0,0]

    for i in range(utils_constants.N_RGB_MEASUREMENTS):
        temp = color_rgb_bytes_new(sensor.read(True))
        for j in range(3):
            values_list[j] = values_list[j]+temp[j]

    for k in range(3):
            values_list[k] = int(values_list[k] / utils_constants.N_RGB_MEASUREMENTS)

    # (r_value,g_value,b_value)=(r_value,g_value,b_value)/utils_constants.N_RGB_MEASUREMENTS

    # answer = 'r:{}\n g:{}\n b:{}\n '.format(values_list[0], values_list[1], values_list[2])

    controller_screen.print_new_line("RGB results:")

    controller_screen.print_new_line("R:" + str(values_list[0]))
    controller_screen.print_new_line("G:" + str(values_list[1]))
    controller_screen.print_new_line("B:" + str(values_list[2]))

    controller_screen.print_new_line(" ")

    print(" R: G:  B: ")
    print(values_list, end='\n')
    return values_list