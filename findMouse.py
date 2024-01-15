import time
import pyautogui



def findMouse():
    # find screen size
    print(pyautogui.size())
    time.sleep(4)

    # find mouse position
    print(pyautogui.position())

findMouse()

