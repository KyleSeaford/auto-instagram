# this is now the script for a different account, so i can get paid dodgy ad money from the memes i post, it will be on a different vm on the server
# on the server ive had to change some of the script due to the locateOnScreen not working, so i had to change it to clickbutton
# it is still more officiant than the previous version, but not what i wanted.

# https://www.instagram.com/gigglegen/ is the account


import pyautogui as pg 
import time
import logging
import webbrowser
import os
import random

#from email import sendlogtokyle

# set logging 
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='AutoIg2.log', filemode='w')

# set the wait time for the program
wait = 1 
short_wait = wait / 2


def openApp():
    # step 0 - open instagram
    webbrowser.open('https://www.instagram.com/')
    time.sleep(wait)
    pg.screenshot("screenshots2/step0.png")
    logging.info("step0 done - instagram opened")
    time.sleep(wait)

def clickbutton(n):
    step1 = pg.locateOnScreen(f"steps/step{n}.png")
    pg.click(step1)
    logging.info(f"step{n} done")
    time.sleep(short_wait)
    pg.screenshot(f"screenshots2/step{n}.png")
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
    
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg' , '.mp4'))]
    
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
        logging.info(f"step4 done - Selected meme: {random_meme_name}")
        ChoseMeme(random_meme_name)


def ChoseMeme(random_meme_name):
    # step 5 - get to address bar
    pg.hotkey('ctrl', 'l')                                           # jump to address bar
    logging.info(f"step5 done - address bar selected")
    time.sleep(short_wait)
    pg.screenshot(f"screenshots2/step5.png")
    time.sleep(wait)
 
    # step 6 - type address
    pg.typewrite("I:\\CODE\\auto-instergram\\meme account 2\\memes")                 # types the address of where the memes are stored, different for each computer
    pg.press("enter")
    logging.info('step6 done - address typed and entered')
    time.sleep(short_wait)
    pg.screenshot("screenshots2/step6.png")
    time.sleep(wait)

    # step 7 - select meme
    for i in range(5):
        time.sleep(short_wait)
        pg.press("tab")                                             # navigates from the address bar to the file name bar                      

    logging.info(f"step7 done - tabbed to file name bar")
    time.sleep(short_wait)
    pg.screenshot(f"screenshots2/step7.png")
    time.sleep(wait)

    # step 8 - load meme
    pg.typewrite(random_meme_name)                                  # types the name of the meme
    pg.press("enter")
    logging.info('step8 done - meme loaded')
    pg.screenshot("screenshots2/step8.png")

# step 9 - click next and take too caption writing
# im not sure what step9 is doing, but it works so i don't want to mess with it. i might just be dumb and not counting properly
# step10 is no cropping
# step11 is no filter
def edit():
    for i in range(10, 12):
        clickbutton(i)


# step 12 - write caption
def WriteCaption():
    captions = [
        "When life gives you lemons, make memes.",
        "I didn't choose the meme life, the meme life chose me.",
        "Memes are the only thing keeping me sane during quarantine.",
        "If you can't handle me at my meme-iest, you don't deserve me at my dreamiest.",
        "In memes we trust.",
        "Life is short, make it meme-worthy.",
        "I live my life one meme at a time.",
        "Memes: because sometimes words just aren't enough.",
        "Keep calm and meme on.",
        "Memes are my love language.", 
        "Memes are my therapy.",
        "Memes are my spirit animal.",
        "When you're down, meme harder.",
        "Memes are my happy place.",
        "how do you do, fellow kids?",
        "I'm just here for the memes.",
        "committing tax fraud, but make it a meme.",
        "I'm a simple person, I see a meme, I laugh.",
        "meme number 342"
        "go like my last post or I'll cry",
        "go like my last post or else",
        "follow me or I'll cry",
        "follow me or else",
        "I'm a bot, but I'm a cool bot",
        "ill eat your toes if you don't follow me",
        "Memes are cheaper than therapy.",
        "Living in a meme-eat-meme world.",
        "My spirit animal is a meme.",
        "Memes speak louder than words.",
        "Life update: currently holding it together with a single meme.",
        "I followed my heart and it led me to memes.",
        "Why be moody when you can share memes?",
        "Memes are just inside jokes with the internet.",
        "I have a PhD in meme-ology.",
        "In a world full of trends, I want to remain a classic meme.",
        "Memes are the glue that holds the internet together.",
        "I'm not addicted to memes, we're just in a committed relationship.",
        "Memes make the world go round.",
        "I'm just a girl, standing in front of a meme, asking it to make her laugh.",
        "Memes are my favorite form of self-expression."
        "im going to find you",
        "im in your walls", 
        "im in your computer",
        "im in your phone",
        "im in your memes",
        "you are the meme"
    ]
    
    hashtags = [
        "#love", "#instagood", "#fashion", "#instagram", "#photooftheday", "#art", "#photography", "#beautiful",
        "#nature", "#picoftheday", "#travel", "#happy", "#cute", "#instadaily", "#style", "#tbt", "#repost", "#followme",
        "#summer", "#reels", "#like4like", "#beauty", "#fitness", "#food", "#instalike", "#followforfollow", "#lifestyle",
        "#reelsinstagram", "#reelitfeelit", "#igreels", "#trendingreels", "#instareels", "#reelvideo", "#reelsvideo",
        "#reelsviral", "#funnyreels", "#birthdayreels", "#stories", "#instastory", "#storiesinstagram", "#instagramstories",
        "#littlestoriesofmylife", "#video", "#reelvideo", "#MEMES", "#memesdaily", "#memes", "#memesrlife", "#memes4ever",
        "#memes2good", "#memes4life", "#funnymemes", "#memes4ever", "#follow", "#me", "#selfie", "#friends", "#girl", "#fun", 
        "#smile", "#family", "#igers", "#tagsforlikes", "#follow4follow", "#nofilter", "#life", "#amazing", "#instamood"
    ]
    

    # step12 - Choose a random caption and hashtags
    random_caption = random.choice(captions)

    random_hashtags = set()
    while len(random_hashtags) < 6:
        hashtag = random.choice(hashtags)
        random_hashtags.add(hashtag)
        logging.info("step12 done - Chosen caption and hashtags")

    # step13 - click caption box
    clickbutton(13)

    # step 14 - Write the caption
    pg.typewrite(f"{random_caption}")
    logging.info(f"step14 done - {random_caption}")
    time.sleep(wait)

    # Press Enter to write the hashtag on a new line
    pg.press("enter")

    # step15 - Write the hashtags
    for i, hashtag in enumerate(random_hashtags, 1):
        pg.typewrite(f"{hashtag} ")
        logging.info(f"step15{i} done - {hashtag}")
        pg.screenshot(f"screenshots2/step15_{i}.png")
        time.sleep(wait)

    # Press Enter to write the disclaimer on a new line
    pg.press("enter")
    
    # step16 - Write the disclaimer
    pg.typewrite("This post was made and uploaded by a python bot :D")
    logging.info("step16 done - disclaimer written")
    pg.screenshot("screenshots2/step16.png")


# step17 - post the meme
def postMeme():
    clickbutton(17)

"""
TO DO:
- DRY = don't repeat yourself!!!!

- make new vm for this account, clone the other one  - done
- on vm download the memes - done
- on vm add thing to bookmark bar - done 

- new memes https://github.com/Pumpkintitan/Le-Monke/tree/master/memes download and put in memes folder
- make sure to change the folder path in the code 
- memes to 1080x1080 (ResizeMeme.py) make sure to change the folder path 
- convert pngs to mp4s (ChangeTOVid.py) make sure to change the folder path 

- set a task to run at same time as other account - done 

- while server on, convert pngs to mp4s on other account -- done
"""

def main_sequence():
    try:
        openApp()
        Step123()
        meme()
        edit()
        WriteCaption()
        #postMeme()
        logging.info("All steps done - meme posted")
        #sendlogtokyle()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    
    
    
main_sequence()