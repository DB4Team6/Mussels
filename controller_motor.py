"""
    Controls the 2 stepper motors.
"""

import _thread
import time
import utils_constants as constants
from machine import Pin, PWM 
# import screen_controller

MOTOR_1 = 0
MOTOR_2 = 1

motor_is_running = [False, False]
direction = [0, 0]

_freq = constants.STEPPER_MOTOR_PWM_FREQ
_pin = [
    PWM(Pin(constants.STEPPER_MOTOR_1_STEP_PIN)),
    PWM(Pin(constants.STEPPER_MOTOR_2_STEP_PIN))
]

_direction_pin = [
    Pin(constants.STEPPER_MOTOR_1_STEP_PIN_DIR, Pin.OUT),
    Pin(constants.STEPPER_MOTOR_2_STEP_PIN_DIR, Pin.OUT)
]

# Set initial value of pins to avoid problems
_direction_pin[0](0)
_direction_pin[1](0)
#_pin[0].value(0)
#_pin[1].value(0)

def _check(motor):
    if motor != 0 and motor != 1:
        print("Invalid motor!")

def start(motor):
    """
        Starts a motor.
    """
    _check(motor)
    motor_is_running[motor] = True
    _pin[motor].freq(_freq)
    _pin[motor].duty(100)

def stop(motor):
    """
        Stops a motor.
    """
    _check(motor)
    motor_is_running[motor] = False
    _pin[motor].duty(0)

def set_direction(motor, dir: int):
    """
    This function sets the direction of the motor to i.
    1: clockwise
    0: counter-clockwise
    """
    global direction
    _check(motor)
    if dir != 0 and dir != 1:
        print("Wrong input for direction!!")
        return
    direction[motor] = dir
    _direction_pin[motor](dir)