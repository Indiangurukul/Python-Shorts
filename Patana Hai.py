import pyautogui as pa
import time

time.sleep(1)

for x in range(0,1000):
    if x<1000:
        pa.write("I Love You")
        pa.press("enter")
