# Instagram Auto-Posting Bot with Random Captions and Hashtags

This script is designed as an automation tool for generating and posting memes on Instagram with random captions and hashtags. Utilizing the PyAutoGUI library, it allows precise control over mouse and keyboard actions to seamlessly interact with the Instagram website.

## Prerequisites
Before running the script, ensure the following prerequisites are met:
- The `memes` folder should be located in the same directory as this file and should contain meme images.
- The `emailKYLE.py` script should be located in the same directory as this file.
- Ensure all the directories are correct in all scripts.

## Setup
- Install the required libraries:
```
pip install pyautogui
```
- Adjust the script to reflect the correct screen coordinates for mouse actions.
- Ensure the meme folder contains a variety of meme images.

## Usage
Run the script, and it will perform the following actions:
- Open Instagram in a web browser.
- Open the post creation menu.
- Select a random meme from the meme folder.
- Load the selected meme.
- Write a random caption for the meme.
- Add random hashtags to the caption.
- Post the meme on Instagram.
- Include a disclaimer in the post indicating it was made and uploaded by a Python bot.
The script logs its actions and errors to a log file named `auto.log`.

### Note 
This script is for educational purposes only. Use responsibly and ensure compliance with Instagram's terms of service. The user is responsible for any actions taken using this script.
