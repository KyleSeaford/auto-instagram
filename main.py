import pyautogui as pg 
import time
import logging
import webbrowser
import os
import random

# set logging 
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='test.log', filemode='w')

# set the wait time for the program
wait = 1 



def openApp():
    # step 0 - open instagram
    webbrowser.open('https://www.instagram.com/')
    time.sleep(wait)
    pg.screenshot("screenshots/step0.png")
    time.sleep(wait)

def button():
    # step1 - create post button
    step1 = pg.locateOnScreen("steps/step1.png")
    pg.click(step1)
    logging.info('step1 done')
    pg.screenshot("screenshots/step1.png")
    time.sleep(wait)

    # step2 - select post
    step2 = pg.locateOnScreen("steps/step2.png")
    pg.click(step2)
    logging.info('step2 done')
    pg.screenshot("screenshots/step2.png")
    time.sleep(wait)

    # step3 - select from computer
    # this did not work, need to find a better way to do this. button image is probably bad                            
    step3 = pg.locateOnScreen("steps/step3.png")
    pg.click(step3)
    logging.info('step3 done')
    pg.screenshot("screenshots/step3.png")
    time.sleep(wait)
 

# I can't remember why step4 has 2 different functions, but is dose! :)

# step4 - select a random meme
def select_random_meme(folder_path):
    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        logging.error("No meme images found in the folder.")
        return None
    
    random_meme = random.choice(image_files)
    return random_meme

# step4.5 - select meme
def meme():
    meme_folder_path = "memes"

    random_meme_name = select_random_meme(meme_folder_path)
    if random_meme_name:
        logging.info(f"step4 - Selected meme: {random_meme_name}")
        ChoseMeme(random_meme_name)

# not tested below this point, need to have the correct locate images (step5, step6)

def ChoseMeme(random_meme_name):
    # step 5 - type address
    step5 = pg.locateOnScreen("steps/step5.png")
    pg.click(step5)
    pg.screenshot("screenshots/.png")                               # find address bar
    time.sleep(wait)
    
    pg.typewrite("C:\\Users\\win10_64\\Desktop\\memes")             # types the address of where the memes are stored
    pg.press("enter")
    logging.info('step5 done - typed address')
    time.sleep(wait)

    # step 6 - select meme
    step6 = pg.locateOnScreen("steps/step6.png")                    # bar at bottom of window
    pg.click(step6)
    logging.info('step6 done- bar at bottom of window')
    pg.screenshot("screenshots/step6.png")
    time.sleep(wait)
    pg.typewrite(random_meme_name)                                  # types the name of the meme
    pg.press("enter")
    logging.info('step6_5 done - meme selected')
    pg.screenshot("screenshots/step6_5.png")




"""
TO DO:
- make step3 work, comment on what and why it is not working next to it
- find the correct locate images for step5 and step6
- test new functions and make sure they work
- continue with the rest of the steps
"""

def main_sequence():
    openApp()
    button()
    #meme()
    

main_sequence()