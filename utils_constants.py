"""
    Constants (mainly pins) used in the project.
"""

# Deprecated. Only using high power.
STEPPER_MOTOR_LOW_POWER = 50
STEPPER_MOTOR_PWM_FREQ = 400
STEPPER_MOTOR_CLOCK_DIR = 1

## Stepper Motor 1
STEPPER_MOTOR_1_STEP_PIN = 12
STEPPER_MOTOR_1_STEP_PIN_DIR = 13

## Stepper Motor 2
STEPPER_MOTOR_2_STEP_PIN = 27
STEPPER_MOTOR_2_STEP_PIN_DIR = 33

## Cooler Pin 
COOLER_PIN = 14

#Temperature offset to account for experimental data
TEMP_OFFSET = -3.5

## RGB Sensor 
SENSOR_INTEGRATION_TIME = 100   #value between 2.4 and 614.4.
SENSOR_GAIN = 60    #must be a value of 1, 4, 16, 60
N_RGB_MEASUREMENTS = 10

## RGB LED Pins
R_PIN = 4

G_PIN = 25

B_PIN = 26

## Thermometer Pin
TEMP_PIN = 32

def compute_time(t):
    hours = int(t / 3600)
    minutes = int((t - hours * 3600) / 60)
    seconds = int((t - hours * 3600) % 60)
    return str(hours) + ":" + str(minutes) + ":" + str(seconds)

