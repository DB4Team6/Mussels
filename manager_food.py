"""
    This module knows how to handle food in the
    thingy, ON ANOTHER THREAD.

    For this module, we consider:
        1. The flow of the stepper motor is constant.
            We expect it to be set and be called
            STEPPER_MOTOR_FLOW.
        2. The senzor gives in one meassurement the concentration
            of algae in the water.
        3. If we want to feed the mussels a quantity Q of algae, we have to pump water for T seconds, where
            Concentration * STEPPER_MOTOR_FLOW * T = Q

    NOTE:
        1. The flow of the stepper motor is constant.
        2. There should be a syphone between the two tanks, as we
            only pump water in one direction.
"""

import _thread
import time
import controller_screen
import controller_motor

# Food quantity
FOOD_QUANTITY = 80

# Time between feeding sessions (in sec)
TIME_BETWEEN_FEEDING_SESSIONS = 500

# Motor used for food
FOOD_MOTOR = controller_motor.MOTOR_1
FOOD_MOTOR_DIRECTION = 0 

# Flow of water by the stepper motor tube when started
STEPPER_MOTOR_FLOW = 42 # TODO

# Number of seconds we run the motor before
# we measure the concentration
MEASUREMENT_TIME = 3

# maximal time we can run the pump for before hitting air in the
# mussel tank.
MAXIMAL_PUMP_TIME = 20

feeding_time_hist = []
concentration_hist = []
time_feeding_hist = []

def _compute_concentration():
    return 42
    # todo

def _perform_food_cycle():
    """
        Feed the mussels a quantity of algae.
        Process:
            1. Pump water for MEASUREMENT_TIME seconds, to be able to
                accuratly determining the concentration.
            2. Measure concentration of algae.
            3. Compute a time T we want to run the pump for.
            2. Displace water from the algae to the mussels for T seconds.
    """
    global feeding_time_hist, concentration_hist, time_feeding_hist

    # Setting the motor and starting for a few seconds
    # to get an accurate concentration
    controller_motor.direction(FOOD_MOTOR, FOOD_MOTOR_DIRECTION)
    controller_motor.start(FOOD_MOTOR) 
    time.sleep(MEASUREMENT_TIME)
    controller_motor.stop(FOOD_MOTOR)

    # Measuring the concentration and computing time to pump
    concentration = _compute_concentration()
    T = FOOD_QUANTITY / (concentration * STEPPER_MOTOR_FLOW) 

    # Logging stuff to stdout / OLED screen
    controller_screen.print_new_line("Feeding time:")
    controller_screen.print_new_line("C is " + str(concentration))
    controller_screen.print_new_line("T is " + str(T))
    print("Food Manager: Computed concentration of " + str(concentration))
    print("              and pumping time of " + str(concentration))

    # Saving results to memory
    feeding_time_hist.append(time.time())
    concentration_hist.append(concentration)
    time_feeding_hist.append(T)

    # Actually pumping stuff over
    controller_motor.start(FOOD_MOTOR)
    time.sleep(T)
    controller_motor.stop(FOOD_MOTOR)

    # Try to guess what this is doing :)
    controller_screen.print_new_line("Feeding over!")

def _manager_food_runner():
    print("Started food manager thread!")
    controller_screen.print_new_line("start foodM")

    while True:
        time.sleep(TIME_BETWEEN_FEEDING_SESSIONS)
        _perform_food_cycle()
        
def start_thread():
    """
        THIS SHOULD ONLY BE CALLED ONCE FROM THE BEGGINING OF THE MAIN FUNCTION.
    """
    _thread.start_new_thread(_manager_food_runner, ())
