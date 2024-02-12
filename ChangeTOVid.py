import os
import logging
import numpy as np
from moviepy.editor import ImageSequenceClip
from PIL import Image

def convert_png_to_mp4(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img = img.convert("RGB")
            img_array = np.array(img)

            clip = ImageSequenceClip(
                [img_array],
                fps=1
            )

            output_path = os.path.join(
                output_folder,
                f"{os.path.splitext(filename)[0]}.mp4"
            )

            clip.write_videofile(
                output_path,
                codec='libx264',
                audio=False
            )

            logging.info(f"Converted {filename} to {output_path}")

        else:
            logging.debug(f"Skipped {filename} (not a PNG)")

if __name__ == "__main__":
    input_folder = "memes"
    output_folder = "new_memes"

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='resize.log',
        filemode='w'
    )

    logging.critical("Starting PNG to MP4 conversion")
    convert_png_to_mp4(input_folder, output_folder)
    logging.critical("PNG to MP4 conversion completed successfully")
    print("done")