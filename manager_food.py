"""
    This module knows how to handle food in the
    thingy, ON ANOTHER THREAD.

    For this module, we consider:
        1. The speed of the stepper motor is constant.
            We expect it to be set and be called
            STEPPER_MOTOR_FLOW.
        2. The senzor gives in one meassurement the concentration
            of algae in the water.
        3. If we want to feed the mussels a quantity Q of algae, we have to pump water for T seconds, where
            Concentration * STEPPER_MOTOR_FLOW * T = Q
        4. Pump water back to the algae tank for T seconds 

    NOTE:
        1. The flow of the stepper motor is constant.
        2. The water that is pumped from the algae tank to the mussles
            will be pumped back to the algae after a constant number of seconds
"""

import _thread
import time
import controller_screen
import controller_motor
import controller_sensor
import utils_constants
import math_model


# Time between feeding sessions (in sec)
TIME_BETWEEN_FEEDING_SESSIONS = 720 #720 #!!!!!!!!!!!!!!!!!!!!!!

# Motor used for food
FOOD_MOTOR = controller_motor.MOTOR_1
FOOD_MOTOR_DIRECTION = 0 
INVERSE_DIRECTION = 1

# Flow of water by the stepper motor tube when started 
STEPPER_MOTOR_FLOW = 1.408 # ml/s

# Number of seconds we run the motor before
# we measure the concentration
MEASUREMENT_TIME = 5

# Remaining tube time
TUBE_TIME = 1.6

# Rest Time
BACK_TIME = 300  #!!!!!!!!!!!!

# maximal time we can run the pump for before hitting air in the
# mussel tank.
# MAXIMAL_PUMP_TIME = 100

# feeding_time_hist = []
# concentration_hist = []
# time_feeding_hist = []

def _compute_concentration():
    list_of_values=controller_sensor.measure()  

    RGB_sum=sum(list_of_values)

    concentration = - 44.39278 * RGB_sum + 747477.69782

    return concentration #cells/ml
    # todo

# Food quantity
FOOD_QUANTITY = math_model.feed_amount(_compute_concentration())

#initialize txt log
feeding_history = open("feeding_history.txt",'a')
feeding_history.write("Time, Concentration, Food quantity (ml), Feeding time")
feeding_history.close()


def _perform_food_cycle():
    
    
    global feeding_time_hist, concentration_hist, time_feeding_hist

    # Setting the motor and starting for a few seconds
    # to get an accurate concentration
    controller_motor.set_direction(FOOD_MOTOR, FOOD_MOTOR_DIRECTION)
    controller_motor.start(FOOD_MOTOR) 
    time.sleep(MEASUREMENT_TIME)
    controller_motor.stop(FOOD_MOTOR)

    # Measuring the concentration and computing time to pump
    concentration = _compute_concentration()
    T = math_model.feed_amount(concentration) / STEPPER_MOTOR_FLOW

    # Logging stuff to stdout / OLED screen
    controller_screen.print_new_line("Feeding time:")
    controller_screen.print_new_line("C is " + str(concentration))
    controller_screen.print_new_line("T is " + str(T))
    print("Food Manager: Computed concentration of " + str(concentration))
    print("              and pumping time of " + str(concentration))

    # # Saving results to memory
    # feeding_time_hist.append(time.time())
    # concentration_hist.append(concentration)
    # time_feeding_hist.append(T)

    
    controller_motor.start(FOOD_MOTOR)
    time.sleep(TUBE_TIME)
    controller_motor.stop(FOOD_MOTOR)

    time.sleep(1)

    # Actually pumping stuff over
    controller_motor.start(FOOD_MOTOR)
    time.sleep(T)
    controller_motor.stop(FOOD_MOTOR)

    
    

    # Try to guess what this is doing :)

    feeding_history = open("feeding_history.txt",'a')
    feeding_history.write(str(utils_constants.compute_time(time.time()))+','+
                          str(concentration)+',' +
                          str(FOOD_QUANTITY)+',' +
                          str(T)+'\n')
    feeding_history.close()



    controller_screen.print_new_line("Feeding over!")

    time.sleep(BACK_TIME)
    controller_screen.print_new_line("RUN IT BACK!")
    controller_motor.set_direction(FOOD_MOTOR, INVERSE_DIRECTION)
    controller_motor.start(FOOD_MOTOR)
    time.sleep(T + TUBE_TIME + MEASUREMENT_TIME)
    controller_motor.stop(FOOD_MOTOR)


def _manager_food_runner():
    print("Started food manager thread!")
    controller_screen.print_new_line("Start food!")

    while True:
        time.sleep(TIME_BETWEEN_FEEDING_SESSIONS)
        _perform_food_cycle()
        
def start_thread():
    """
        THIS SHOULD ONLY BE CALLED ONCE FROM THE BEGGINING OF THE MAIN FUNCTION.
    """
    _thread.start_new_thread(_manager_food_runner, ())




