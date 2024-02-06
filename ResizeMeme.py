from PIL import Image
import logging
import os

# Set logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='test.log', filemode='w')

def resize_and_center(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as img:
                aspect_ratio = img.width / img.height

                # Determine the new dimensions
                if aspect_ratio > 1:
                    new_width = 1080
                    new_height = int(1080 / aspect_ratio)
                else:
                    new_width = int(1080 * aspect_ratio)
                    new_height = 1080

                # Resize the image
                img = img.resize((new_width, new_height))

                # Create a 1080x1080 image
                new_img = Image.new("RGB", (1080, 1080), (255, 255, 255))

                # Center the resized image
                offset_x = (1080 - img.width) // 2
                offset_y = (1080 - img.height) // 2
                new_img.paste(img, (offset_x, offset_y))

                # Save the resized image
                new_img.save(output_path)
                logging.info(f"Resized and centered: {filename}")

if __name__ == "__main__":
    input_folder = "memes"
    output_folder = "memes2"

    logging.critical("Starting image resize and center")
    resize_and_center(input_folder, output_folder)

    logging.critical("Images resized and centered successfully.")
    print("done")