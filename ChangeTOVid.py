import os
from moviepy.editor import ImageClip

def create_videos(image_folder, output_folder, duration):
    for filename in os.listdir(image_folder):
        if filename.endswith(".png"):  # Check if the file is a PNG image
            image_path = os.path.join(image_folder, filename)
            output_video = os.path.join(output_folder, filename[:-4] + ".mp4")  # Change .png to .mp4
            clip = ImageClip(image_path, duration=duration)
            clip.write_videofile(output_video, fps=24)  # 24 frames per second
    print("All videos created successfully.")

# Usage
create_videos("memes", "new_memes", 3)  # Creates a 3-second long video for each image