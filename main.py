from machine import Pin
import time

# Managers
import manager_food
import manager_temperature
import manager_web

# Controllers
import controller_screen

button=machine.Pin(15,machine.Pin.IN,Pin.PULL_UP)

global been_pressed=False




def main():
    """
        Entry point of the app.
    """
    global been_pressed
    controller_screen.clear_screen_print_line("PUSH TO START")

    #hold here to wait for start
    while been_pressed==False:
        if button.value==0:
            been_pressed=True
    


    controller_screen.clear_screen_print_line("Starting!")

    time.sleep(1.5)

    # starting threads

    while True:
    manager_food.start_thread()
    manager_temperature.start_thread()
    manager_web.start_thread()
        while button.value==1:
            time.sleep(0.5)
    manager_food.s
    manager_temperature.start_thread()
    manager_web.start_thread()


    # wait for eternity
    while True:
        time.sleep(0.5)

if __name__ == "__main__":
    main()
