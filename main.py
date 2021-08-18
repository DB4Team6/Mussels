from machine import Pin
import time

# Managers
import manager_food
import manager_temperature
import manager_web

# Controllers
import controller_screen

def main():
    """
        Entry point of the app.
    """
    controller_screen.clear_screen_print_line("Starting...")
    
    # starting threads
    manager_food.start_thread()
    manager_temperature.start_thread()
    manager_web.start_thread()

    # wait for eternity
    time.sleep(1e9)

if __name__ == "__main__":
    main()