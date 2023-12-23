import pyautogui as pg
import time
import webbrowser
import os
import random
import datetime

#defaultAnswer
def questionString(question, defaultAnswer):
    answer = input(f"{question} [{defaultAnswer}]")
    if answer == "":
        answer = defaultAnswer
    return answer 

#open instagram
def openInstagram():
    webbrowser.open('https://www.instagram.com/')
    time.sleep(5)

#open post
def OpenPost():
    pg.moveTo(99, 598, duration = 0)
    pg.click()
    pg.moveTo(129, 634, duration = 0)
    pg.click()

#select meme
def select_random_meme(folder_path):
    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print("No meme images found in the folder.")
        return None
    
    random_meme = random.choice(image_files)
    return random_meme

#select meme
def meme():
    meme_folder_path = "memes"

    random_meme_name = select_random_meme(meme_folder_path)
    if random_meme_name:
        print(f"Selected meme: {random_meme_name}")
        ChoseMeme(random_meme_name)

#chose meme
def ChoseMeme(random_meme_name):
    time.sleep(1)
    pg.moveTo(936, 674, duration = 0)
    pg.click()
    pg.moveTo(702, 43, duration = 0)
    time.sleep(1)
    pg.click()
    pg.typewrite("C:\\Users\\win10_64\\Desktop\\auto-main\\memes")
    pg.press("enter")
    pg.moveTo(318, 982, duration = 0)
    pg.click()
    time.sleep(1)
    pg.typewrite(random_meme_name)
    time.sleep(1)
    pg.press("enter")

#load meme
def lodeMeme():
    pg.moveTo(634, 917, duration = 0)
    pg.click()
    pg.moveTo(675, 716, duration = 0)
    pg.click()
    pg.moveTo(1269, 232, duration = 0)
    pg.click()
    time.sleep(0.5)
    pg.moveTo(1441, 228, duration = 0)
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
        "Coding is 10% writing code and 90% fixing bugs"
        "When you finally understand recursion. Mind. Blown."
        "My code isn't messy; it's just creatively organized!"
        "Sleep? I'll do that after this next commit."
        "Coffee: Fueling developers since the beginning of time."
    ]
    
    hashtags = [
        "#CodeHumor", "#GeekHumor", "#TechJokes", "#DevLife", 
        "#ProgrammerLife", "#ProgrammingHumor", "#ProgrammingJokes", 
        "#ProgrammerHumor", "#SoftwareDeveloper", "#SoftwareEngineer", 
        "#SoftwareDevelopment", "#SoftwareEngineerLife", "#SoftwareEngineerProblems", 
        "#SoftwareEngineerHumor", "#SoftwareEng" ,"#SoftwareEngineering", "#programming", "joke"
    ]

    random_caption = random.choice(captions)
    random_hashtag = random.choice(hashtags)
    random_hashtag2 = random.choice(hashtags)
    random_hashtag3 = random.choice(hashtags)

    # Write the caption
    pg.moveTo(1211, 327, duration=0)
    pg.click()
    pg.typewrite(f"{random_caption} ")
    time.sleep(1)

    # Write the hashtag
    pg.press("enter")
    pg.typewrite(f"{random_hashtag}")
    pg.moveTo(1211, 552, duration=0)
    time.sleep(1.5)
    pg.click()
    
    # Write the hashtag2
    time.sleep(1)
    pg.typewrite(f"{random_hashtag2}")
    pg.moveTo(1211, 552, duration=0)
    time.sleep(1.5)
    pg.click()

    # Write the hashtag3
    time.sleep(1)
    pg.typewrite(f"{random_hashtag3}")
    pg.moveTo(1211, 552, duration=0)
    time.sleep(1.5)
    pg.click()

    # Write the disclaimer
    time.sleep(1)
    pg.moveTo(1262, 429, duration=0)
    time.sleep(0.5)
    pg.press("enter")
    pg.typewrite(f"This post was made and uploaded by a python bot :D")

#post meme
def postMeme():
    pg.moveTo(1422, 227, duration=0)
    pg.click()

    #close window
    time.sleep(1)
    pg.moveTo(1875, 148, duration=0)
    pg.click()
    pg.moveTo(1895, 16, duration=0)
    pg.click()

#main code
def main_sequence():
    openInstagram()
    print("Instagram opened")
    time.sleep(1)
    OpenPost()
    print("Post opened")
    time.sleep(1)
    meme()
    print("Meme selected")
    time.sleep(1)
    lodeMeme()
    print("Meme loaded")
    time.sleep(1)
    WriteCaption()
    print("Caption written")
    time.sleep(1)
    postMeme()
    print("Meme posted")


main_sequence()