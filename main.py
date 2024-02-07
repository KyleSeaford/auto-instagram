import pyautogui as pg 
import time
import logging
import webbrowser
import os
import random

from email import sendlogtokyle

# set logging 
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='test.log', filemode='w')

# set the wait time for the program
wait = 1 
short_wait = wait / 2


def openApp():
    # step 0 - open instagram
    webbrowser.open('https://www.instagram.com/')
    time.sleep(wait)
    pg.screenshot("screenshots/step0.png")
    logging.info("step0 done - instagram opened")
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
        logging.info(f"step4 done - Selected meme: {random_meme_name}")
        ChoseMeme(random_meme_name)


def ChoseMeme(random_meme_name):
    # step 5 - get to address bar
    pg.hotkey('ctrl', 'l')                                           # jump to address bar
    logging.info(f"step5 done - address bar selected")
    time.sleep(short_wait)
    pg.screenshot(f"screenshots/step5.png")
    time.sleep(wait)
 
    # step 6 - type address
    pg.typewrite("I:\\CODE\\auto-instergram\\memes")                 # types the address of where the memes are stored, different for each computer
    pg.press("enter")
    logging.info('step6 done - address typed and entered')
    time.sleep(short_wait)
    pg.screenshot("screenshots/step6.png")
    time.sleep(wait)

    # step 7 - select meme
    for i in range(5):
        time.sleep(short_wait)
        pg.press("tab")                                             # navigates from the address bar to the file name bar                      

    logging.info(f"step7 done - tabbed to file name bar")
    time.sleep(short_wait)
    pg.screenshot(f"screenshots/step7.png")
    time.sleep(wait)

    # step 8 - load meme
    pg.typewrite(random_meme_name)                                  # types the name of the meme
    pg.press("enter")
    logging.info('step8 done - meme loaded')
    pg.screenshot("screenshots/step8.png")

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
        "Bug squashed, another arises", 
        "Risking it all with an update", 
        "Break? Just switch code types", 
        "Not a bug, a feature!", 
        "When your code finally works on the first try!", 
        "That moment you realize it's not a bug, just a feature", 
        "Me, when I see a semicolon missing :o", 
        "Sleep is for the weak; debugging is for the strong",
        "When you finally fix that bug that's been bugging you for days",
        "Coding is 10% writing code and 90% fixing bugs",
        "When you finally understand recursion. Mind. Blown.",
        "My code isn't messy; it's just creatively organized!",
        "Sleep? I'll do that after this next commit.",
        "Coffee: Fueling developers since the beginning of time.",
        "I don't always test my code, but when I do, I do it in production.",
        "When you're coding and you realize you've been talking to yourself for the past 20 minutes.",
        "what do you mean, 'it works on my machine'?",
        "how did this ever work?",
        "I'm not anti-social; I'm just not user friendly.",
        "I'm not lazy; I'm just on my energy saving mode.",
        "Debugging: The art of finding a needle in a haystack"
        "Code, coffee, repeat: The developer's mantra",
        "In the world of coding, patience is a virtue",
        "When in doubt, print it out: The coder's way",
        "404: Sleep not found. Please debug and try again",
        "Coding: Where the impossible becomes possible",
        "The best error message is the one that never shows up",
        "To err is human, to debug divine",
        "Code like a butterfly, test like a bee",
        "In the kingdom of code, the debugger is king",
        "The only thing we have to fear is uncaught exceptions",
        "Coding is thinking, not typing",
        "The code is dark and full of errors",
        "Keep calm and trust the debugger",
        "Code it, break it, fix it, repeat",
        "The closer you look, the less you see: The mystery of code",
        "Coding: Where every character counts",
        "May the source be with you: The coder's blessing",
        "In the quest for perfection, we debug endlessly",
        "Code: It's not a bug, it's an undocumented feature",
        "Embracing the beauty of data chaos",
        "Plot twist: Data speaks for itself",
        "Visualizing the invisible: Data magic",
        "In data we trust, in visualizations we marvel",
        "Unveiling patterns, one data point at a time",
        "When numbers become art: The power of visualization",
        "Data whispers, visualizations shout",
        "Lost in the scatter: Finding meaning in the chaos",
        "A symphony of data points: Visualizing harmony",
        "Where data and design dance together",
        "The art of storytelling through data visualizations",
        "Decoding the data: A visual journey",
        "From raw data to visual poetry",
        "Data dreams in technicolor: The magic of visualization",
        "When dots connect: The power of visual narratives",
        "Data alchemy: Turning numbers into gold",
        "The language of data: Spoken in visuals",
        "Unveiling the hidden: The art of data revelation",
        "When data takes center stage: The visual spotlight",
        "In the realm of visual insights: Where data comes to life"

    ]
    
    hashtags = [
        "#CodeHumor", "#GeekHumor", "#TechJokes", "#DevLife", 
        "#ProgrammerLife", "#ProgrammingHumor", "#ProgrammingJokes", 
        "#ProgrammerHumor", "#SoftwareDeveloper", "#SoftwareEngineer", 
        "#SoftwareDevelopment", "#SoftwareEngineerLife", "#SoftwareEngineerProblems", 
        "#SoftwareEngineerHumor", "#SoftwareEng" ,"#SoftwareEngineering", 
        "#programming", "#joke", "#funny", "#coding", "#programmer", "#developer",         
        "#codinglife", "#webdeveloper", "#webdevelopment", 
        "#webdev", "#webdesign", "#webdesigner", "#webdesigning", 
        "#webdesignlife", "#webdesignerlife", "#webdesigners", 
        "#webdesignerslife", "#webdesignersofinstagram", "#webdesignersofinsta", 
        "#webdesignersoftheworld", "#webdesignersoftheworld", "#webdesignersoftheworldunite",
        "#computer", "#computers", "#computerscience", "#computersciencestudent",
        "#python", "#pythonprogramming", "#pythonprogramminglanguage", "#pythonprogrammer",
        "#code", "#coder", "#codingisfun", "#codingpics", "#c", "#csharp", "#csharpdeveloper",
        "#meme", "#memes", "#memesdaily", "#memes4days", "#memes4life", "#memes4ever", "#memes4u"
    ]

    random_caption = random.choice(captions)
    random_hashtags = [random.choice(hashtags) for _ in range(1, 4)]
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
        pg.screenshot(f"screenshots/step15_{i}.png")
        time.sleep(wait)

    # Press Enter to write the disclaimer on a new line
    pg.press("enter")
    
    # step16 - Write the disclaimer
    pg.typewrite("This post was made and uploaded by a python bot :D")
    logging.info("step16 done - disclaimer written")
    pg.screenshot("screenshots/step16.png")


# step17 - post the meme
def postMeme():
    clickbutton(17)

"""
TO DO:
- DRY = don't repeat yourself!!!!
"""

def main_sequence():
    openApp()
    Step123()
    meme()
    edit()
    WriteCaption()
    postMeme()
    logging.info("All steps done - meme posted")
    sendlogtokyle()
    
    

main_sequence()