"""
    This module knows how to handle temperature in the
    thingy, ON ANOTHER THREAD.

"""

import _thread
import controller_screen
import controller_motor
import utils_read_temp
import time

# Temperature we want to get to
TARGET_TEMP = 18

# Motor we use
TEMP_MOTOR = controller_motor.MOTOR_2

temperature_histoy = []
smooth_temperature_history = []

# Time between temperature measurements
TIME_BETWEEN_TEMP_MEASUREMENTS = 5

# PID constants
KP = 3
KI = 0.1 
KD = 0.1

# PID Variables
total_error = 0
last_error = 24

#take a measurement
def _get_measurement_and_update_temp():
    """
        Gets the current water temeperature and updates the history.
        Stolen from [here](https://www.teachmemicro.com/arduino-pid-control-tutorial/).
    """
    global temperature_histoy, smooth_temperature_history
    global total_error, last_error

    # Measure the actual temperature
    temperature = utils_read_temp.read_temp()

    # Compute PID thingy
    error = temperature - last_error
    total_error += error * TIME_BETWEEN_TEMP_MEASUREMENTS
    rate_error = (error - last_error) / TIME_BETWEEN_TEMP_MEASUREMENTS

    # Compute PID output
    output = KP * error + KI * total_error + KD * rate_error

    last_error = error

    # Update the history
    temperature_histoy.append(temperature)
    smooth_temperature_history.append(output)

    # Log the measurement
    controller_screen.print_new_line("Check Temp:")
    controller_screen.print_new_line(" Seen: " + str(temperature))
    controller_screen.print_new_line(" Comp: " + str(output))
    print("Temperature Manager: read temperature of " + str(temperature))
    print("                     PID output is " + str(output))

    # Return the computed temperature
    return output


def _manager_temperature_runner():
    print("Started temperature manager thread!")
    controller_screen.print_new_line("Start temp!")
    is_cooling = False

    while True:
        computed_temp = _get_measurement_and_update_temp()

        if computed_temp > TARGET_TEMP:
            # Start cooling
            controller_motor.set_direction(TEMP_MOTOR, 1)
            controller_motor.start(TEMP_MOTOR)
            if not is_cooling:
                controller_screen.print_new_line("Start cooling!")
                print("Started cooling!")
                is_cooling = True
        else:
            # Stop cooling
            controller_motor.stop(TEMP_MOTOR)
            if is_cooling:
                controller_screen.print_new_line("Stop cooling!")
                print("Stopped cooling!")
                is_cooling = False

        time.sleep(TIME_BETWEEN_TEMP_MEASUREMENTS)


def start_thread():
    """
        THIS SHOULD ONLY BE CALLED ONCE FROM THE BEGGINING OF THE MAIN FUNCTION.
    """
    _thread.start_new_thread(_manager_temperature_runner, ())
