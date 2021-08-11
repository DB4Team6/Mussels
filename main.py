from machine import Pin
import time

# Controllers
import screen_controller
import cooling_controller
import led_controller
import motor_controller

# Constants
import constants

# Managers
import food_manager
import temperature_manager

def main():
    """
        Entry point of the app.
    """
    screen_controller.clear_screen_print_line("Starting...")
    
    # Starting additional threads.
    motor_controller.start_thread()
    screen_controller.print_new_line("Start job...")

    while True:
        food_manager.step()
        temperature_manager.step()

    # Ending threads - TBD if usefull.
    screen_controller.print_new_line("Job ended.")
    screen_controller.print_new_line("Stopping...")
    motor_controller.stop_thread()


if __name__ == "__main__":
    main()
