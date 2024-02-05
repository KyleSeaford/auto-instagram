import pyautogui as pg 
import time
import logging
import webbrowser

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='test.log', filemode='w')

wait = 2 



def openApp():
    webbrowser.open('https://www.youtube.com/')
    time.sleep(wait)
    #pg.screenshot("screenshots/1.png")
    #time.sleep(wait)

def button():
    step1 = pg.locateOnScreen("python.png")
    print(step1)
    pg.click(step1)

openApp()
button()