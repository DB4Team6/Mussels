
from machine import Pin
import time
import screen_controller
import constants
import stepper_motor

screen_controller.clear_screen()

screen_controller.print_new_line("Low Speed")

stepper_motor.start_motor()
stepper_motor.motor_set_power(constants.STEPPER_MOTOR_LOW_POWER)

time.sleep(5)

screen_controller.print_new_line("High Speed")

stepper_motor.motor_set_power(constants.STEPPER_MOTOR_HIGH_POWER)

time.sleep(5)

screen_controller.print_new_line("Off")

stepper_motor.stop_motor()

time.sleep(5)

# screen_controller.print_new_line("Hello!!")
# time.sleep(0.5)
# screen_controller.print_new_line("Happy to see you :)")
# time.sleep(0.5)
# screen_controller.print_new_line("Starting soon....")
# time.sleep(0.5)
# screen_controller.print_new_line("Ready??")
# time.sleep(0.5)
# screen_controller.print_new_line("GOO!!!!")
# time.sleep(0.5)

# stepper_motor.start_motor()
# stepper_motor.motor_set_power(constants.STEPPER_MOTOR_LOW_POWER)

# time.sleep(3)

# screen_controller.print_new_line("See? :)")
# time.sleep(0.5)

# screen_controller.print_new_line("We can also go faster :-)")

# stepper_motor.motor_set_power(constants.STEPPER_MOTOR_HIGH_POWER)

# time.sleep(4)


# screen_controller.print_new_line("I will kill myself in...")

# time.sleep(0.7)

# for i in [5, 4, 3, 2, 1]:
#     screen_controller.print_new_line("  " + str(i) + " seconds...")
#     time.sleep(1)


# screen_controller.print_new_line("BOOOOM!!!")
# stepper_motor.stop_motor()

# time.sleep(1)

# screen_controller.clear_screen()