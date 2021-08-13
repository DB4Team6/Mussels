"""
    Controls the 2 stepper motors.
"""

import _thread
import time
import constants
from machine import Pin
# import screen_controller

MOTOR_1 = 0
MOTOR_2 = 1

motor_is_running = [False, False]
direction = [0, 0]

_thread_is_running = False
_has_to_stop = False
_power = constants.STEPPER_MOTOR_HIGH_POWER
_pin = [
    Pin(constants.STEPPER_MOTOR_1_STEP_PIN, Pin.OUT),
    Pin(constants.STEPPER_MOTOR_2_STEP_PIN, Pin.OUT)
]

_direction_pin = [
    Pin(constants.STEPPER_MOTOR_1_STEP_PIN_DIR, Pin.OUT),
    Pin(constants.STEPPER_MOTOR_2_STEP_PIN_DIR, Pin.OUT)
]

# Set initial value of pins to avoid problems
_direction_pin[0](0)
_direction_pin[1](0)
_pin[0].value(0)
_pin[1].value(0)

def _stepper_motor_runner():
    global _thread_is_running, _has_to_stop
    global _pin, motor_is_running
    print("Motor Controller Thread Started Successfully!")

    while True:
        if _has_to_stop:
            _thread_is_running = False
            _has_to_stop = False
            print("Motor Controller Thread Ended Successfully!")
            return
        for _ in range(20):
            if motor_is_running[0]:
                _pin[0].value(1)
            if motor_is_running[1]:
                _pin[1].value(1)

            time.sleep(constants.STEPPER_MOTOR_HIGH_POWER)
            
            if motor_is_running[0]:
                _pin[0].value(0)
            if motor_is_running[1]:
                _pin[1].value(0)
            time.sleep(constants.STEPPER_MOTOR_HIGH_POWER)

def _check(motor):
    if motor != 0 and motor != 1:
        print("Invalid motor!")

def start(motor):
    """
        Starts a motor.
    """
    _check(motor)
    motor_is_running[motor] = True

def stop(motor):
    """
        Stops a motor.
    """
    _check(motor)
    motor_is_running[motor] = False


def start_thread():
    """
        THIS SHOULD ONLY BE CALLED ONCE FROM THE BEGGINING OF THE MAIN FUNCTION.
    """
    global _thread_is_running
    if _thread_is_running:
        print("WARNING: Tried to start a thread already started!!")
        return
    _thread.start_new_thread(_stepper_motor_runner, ())
    _thread_is_running = True
    screen_controller.print_new_line("M thread +")


def stop_thread():
    """
        THIS SHOULD ONLY BE CALLED ONCE FROM THE END OF THE MAIN FUNCTION.
    """
    global _thread_is_running, _has_to_stop

    if not _thread_is_running:
        print("WARNING: Tried to stop a thread not running!")
        return

    _has_to_stop = True
    screen_controller.print_new_line("M thread -")


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