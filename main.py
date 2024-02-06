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
short_wait = 0.5


def openApp():
    # step 0 - open instagram
    webbrowser.open('https://www.instagram.com/')
    time.sleep(wait)
    pg.screenshot("screenshots/step0.png")
    time.sleep(wait)

def clickbutton(n):
    step1 = pg.locateOnScreen(f"steps/step{n}.png")
    pg.click(step1)
    logging.info(f"step{n} done")
    time.sleep(short_wait)
    pg.screenshot(f"screenshots/step{n}.png")
    time.sleep(wait)
    pass


# this does step 1, 2 and 3, fast and easy

def Step123():
    for i in range(1, 4):                                     
        clickbutton(i)

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
    # step 5 - get to address bar
    pg.hotkey('ctrl', 'l')                                           # jump to address bar
    logging.info(f"step5 done")
    time.sleep(short_wait)
    pg.screenshot(f"screenshots/step5.png")
    time.sleep(wait)
 
    # step 6 - type address
    pg.typewrite("I:\\CODE\\auto-instergram\\memes")                 # types the address of where the memes are stored, different for each computer
    pg.press("enter")
    logging.info('step6 done')
    time.sleep(short_wait)
    pg.screenshot("screenshots/step6.png")
    time.sleep(wait)

    # step 7 - select meme
    for i in range(5):
        time.sleep(short_wait)
        pg.press("tab")                                             # navigates from the address bar to the file name bar                      

    logging.info(f"step7 done")
    time.sleep(short_wait)
    pg.screenshot(f"screenshots/step7.png")
    time.sleep(wait)

    # step 8 - load meme
    pg.typewrite(random_meme_name)                                  # types the name of the meme
    pg.press("enter")
    logging.info('step8 done')
    pg.screenshot("screenshots/step8.png")

 
def edit():
    clickbutton(9)
    clickbutton(10)
    clickbutton(11)
    clickbutton(12)



"""
TO DO:
- DRY = don't repeat yourself!!!!
- make step3 work, comment on what and why it is not working next to it     - done/working
- find the correct locate images for step5 and step6                        - done/working
- test new functions and make sure they work                                -
- continue with the rest of the steps                                       -
- if i make all the images 1:1 i don't need to use clickbutton() for 11, 12 - testing      
"""

def main_sequence():
    #openApp()
    #Step123()
    #meme()
    time.sleep(4)
    edit()
    

main_sequence()