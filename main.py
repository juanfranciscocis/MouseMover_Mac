
from pynput.mouse import Controller
import time
import random
if __name__ == '__main__':
    sleep_for_1_minute = 60
    mouse = Controller()
    # move the mouse to the position
    while True:
        mouse.position = (random.randint(0, 1920), random.randint(0, 1080))
        time.sleep(sleep_for_1_minute)
