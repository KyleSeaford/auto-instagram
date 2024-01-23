import pyautogui as pg
import time
import webbrowser
import os
import random
import datetime
import logging


wait = 5

logging.basicConfig(level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='Z:\\logs\\auto.log', filemode='w')

#defaultAnswer
def questionString(question, defaultAnswer):
    answer = input(f"{question} [{defaultAnswer}]")
    if answer == "":
        answer = defaultAnswer
    return answer 

#open instagram
def openInstagram():
    webbrowser.open('https://www.instagram.com/')
    time.sleep(wait)

#open post
def OpenPost():
    pg.moveTo(99, 598, duration = 1)
    pg.click()
    pg.moveTo(129, 634, duration = 1)
    pg.click()

#select meme
def select_random_meme(folder_path):
    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        logging.error("No meme images found in the folder.")
        return None
    
    random_meme = random.choice(image_files)
    return random_meme

#select meme
def meme():
    meme_folder_path = "memes"

    random_meme_name = select_random_meme(meme_folder_path)
    if random_meme_name:
        logging.info(f"Selected meme: {random_meme_name}")
        ChoseMeme(random_meme_name)

#chose meme
def ChoseMeme(random_meme_name):
    time.sleep(wait)
    pg.moveTo(936, 674, duration = 1)
    pg.click()
    pg.moveTo(702, 43, duration = 1)
    time.sleep(wait)
    pg.click()
    pg.typewrite("C:\\Users\\xbox\\Desktop\\nerd\\python\\memes")
    pg.press("enter")
    pg.moveTo(318, 982, duration = 1)
    pg.click()
    time.sleep(wait)
    pg.typewrite(random_meme_name)
    time.sleep(wait)
    pg.press("enter")

#load meme
def lodeMeme():
    pg.moveTo(634, 917, duration = 1)
    pg.click()
    pg.moveTo(675, 716, duration = 1)
    pg.click()
    pg.moveTo(1269, 232, duration = 1)
    pg.click()
    time.sleep(0.5)
    pg.moveTo(1441, 228, duration = 1)
    pg.click()

#write caption
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
        "I'm not lazy; I'm just on my energy saving mode."
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
        "#webdesignersoftheworld", "#webdesignersoftheworld", "#webdesignersoftheworldunite"
    ]

    random_caption = random.choice(captions)
    random_hashtag = random.choice(hashtags)
    random_hashtag2 = random.choice(hashtags)
    random_hashtag3 = random.choice(hashtags)

    logging.info("Choosing caption and hashtags")
    # Write the caption
    pg.moveTo(1211, 327, duration=1)
    pg.click()
    pg.typewrite(f"{random_caption}")
    logging.info({random_caption})
    time.sleep(wait)

    # Write the hashtag
    pg.press("enter")
    pg.typewrite(f"{random_hashtag}")
    logging.info({random_hashtag})
    pg.moveTo(1211, 552, duration=1)
    time.sleep(wait)
    pg.click()
    
    # Write the hashtag2
    time.sleep(wait)
    pg.typewrite(f"{random_hashtag2}")
    logging.info({random_hashtag2})
    pg.moveTo(1211, 552, duration=1)
    time.sleep(wait)
    pg.click()

    # Write the hashtag3
    time.sleep(wait)
    pg.typewrite(f"{random_hashtag3}")
    logging.info({random_hashtag3})
    pg.moveTo(1211, 552, duration=1)
    time.sleep(wait)
    pg.click()

    # Write the disclaimer
    time.sleep(wait)
    pg.moveTo(1262, 429, duration=1)
    time.sleep(wait)
    pg.press("enter")
    pg.typewrite(f"This post was made and uploaded by a python bot :D")

#post meme
def postMeme():
    #pg.moveTo(1422, 227, duration=1)
    pg.click()

    #close window
    time.sleep(wait)
    pg.moveTo(1875, 148, duration=1)
    time.sleep(wait)
    pg.click()
    pg.moveTo(1895, 16, duration=1)
    time.sleep(wait)
    pg.click()

#main code
def main_sequence():
    openInstagram()
    logging.info("Instagram opened")
    time.sleep(wait)
    OpenPost()
    logging.info("Post menu opened")
    time.sleep(wait)
    meme()
    logging.info("Meme selected")
    time.sleep(wait)
    lodeMeme()
    logging.info("Meme loaded") 
    time.sleep(wait)
    WriteCaption()
    logging.info("Caption written")
    time.sleep(wait)
    postMeme()
    logging.info("Meme posted")
    logging.critical("Script ended")


logging.info("Script running at " + str(datetime.datetime.now()))
logging.info(f"The screen size is: {pg.size()}")
main_sequence()