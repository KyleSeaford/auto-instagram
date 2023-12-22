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
    time.sleep(2)

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
    time.sleep(0.5)
    pg.moveTo(936, 674, duration = 0)
    pg.click()
    pg.moveTo(702, 43, duration = 0)
    time.sleep(0.5)
    pg.click()
    pg.typewrite("C:\\Users\\xbox\\Desktop\\nerd\\python\\memes")
    pg.press("enter")
    pg.moveTo(318, 982, duration = 0)
    pg.click()
    time.sleep(0.5)
    pg.typewrite(random_meme_name)
    time.sleep(0.5)
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
    time.sleep(0.5)
    pg.click()
    
    # Write the hashtag2
    time.sleep(0.5)
    pg.typewrite(f"{random_hashtag2}")
    pg.moveTo(1211, 552, duration=0)
    time.sleep(0.5)
    pg.click()

    # Write the hashtag3
    time.sleep(0.5)
    pg.typewrite(f"{random_hashtag3}")
    pg.moveTo(1211, 552, duration=0)
    time.sleep(0.5)
    pg.click()

    # Write the disclaimer
    time.sleep(0.5)
    pg.press("enter")
    pg.typewrite(f"This post was made and uploaded by a python bot :D")

#post meme
def postMeme():
    pg.moveTo(1422, 227, duration=0)
#    pg.click()

    #close window
    time.sleep(1)
    pg.moveTo(1875, 148, duration=0)
    pg.click()
    pg.moveTo(1895, 16, duration=0)
    pg.click()


#testing code
'''
confirm = questionString("Do you want to post a meme? (y/n)", "y")
if confirm == "y":
    print("Starting...")
    openInstagram()
    print("Instagram opened")
    OpenPost()
    print("Post opened")
    confirm = questionString("Do you want to post? (y/n)", "y")
    if confirm == "y":
        meme()
        print("Meme selected")
        confirm = questionString("Do you want to post this meme? (y/n)", "y")
        if confirm == "y":
            lodeMeme()
            print("Meme loaded")
            confirm = questionString("Do you want to write a caption? (y/n)", "y")
            if confirm == "y":
                print("Writing caption...")
                WriteCaption()
                print("Caption written")
                confirm = questionString("Do you want to post the meme? (y/n)", "y")
                if confirm == "y":
                    postMeme()
                    print("Meme posted")
                    exit()
                else:
                    exit()
            else:
                exit()  
        else:
            exit()
    else:
        exit()
else:
    exit()
'''

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

#main loop, repeats every 24 hours
while True:
    current_time = datetime.datetime.now().time()
    print(f"Current time: {current_time}")
    target_time = datetime.time(10, 30)  #execution time
    print(f"Target time: {target_time}")

    if current_time >= target_time:
        print("Time matches")
        print("Starting...")
        main_sequence()
        
        # Calculate the time difference until the next day
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        next_run = datetime.datetime.combine(tomorrow.date(), target_time)
        sleep_time = (next_run - datetime.datetime.now()).total_seconds()

        # Sleep until the next run
        print(f"Sleeping for {sleep_time} seconds")
        time.sleep(sleep_time)

    else:
        # Sleep for a short time and check again
        print(f"the current time is {current_time}")
        print(f"the target time is {target_time}")
        print("Sleeping for 30 mins...")
        time.sleep(1800)  # Check every 30 mins
