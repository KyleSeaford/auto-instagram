import pyautogui as pg 
import time
import logging
import webbrowser
import os
import random


logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='test.log', filemode='w')

wait = 2 



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
    pg.screenshot("screenshots/step1.png")
    time.sleep(wait)

    # step3 - select from computer
    step3 = pg.locateOnScreen("steps/step3.png")
    pg.click(step3)
    logging.info('step3 done')
    pg.screenshot("screenshots/step1.png")
    time.sleep(wait)
 

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
        logging.info(f"Step 4 - Selected meme: {random_meme_name}")
        ChoseMeme(random_meme_name)

# step5 - select meme
def ChoseMeme(random_meme_name):
    print(random_meme_name)


#openApp()
#button()
meme()
