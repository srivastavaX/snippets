
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode
import threading
import time

mouse = MouseController()

clicking = False
exit_flag = False

def clicker():
    global clicking, exit_flag
    while not exit_flag:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.025)   # adjust click speed here
        else:
            time.sleep(0.01)

def on_press(key):
    global clicking, exit_flag

    if isinstance(key, KeyCode):
        if key.char == 'a':      # start clicking
            clicking = True
            print("Clicking started.")

        elif key.char == 'w':    # stop clicking
            clicking = False
            print("Clicking stopped.")

        elif key.char == 'q':    # optional: quit the script
            clicking = False
            exit_flag = True
            print("Exiting...")
            exit()

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=on_press) as listener:
    listener.join()
