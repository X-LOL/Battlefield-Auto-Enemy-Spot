from pynput import keyboard
import time

while True:
 keyboard.Controller().press('q')
 time.sleep(0.1)
 keyboard.Controller().release('q')
 time.sleep(0.1)