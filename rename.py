import os

def rename_files(directory):
    for count, filename in enumerate(os.listdir(directory), start=1):
        # Split the filename into name and extension
        name, extension = os.path.splitext(filename)
        # Create new name
        new_name = f"{count}{extension}"
        # Create full paths
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)
        # Rename the file
        os.rename(src, dst)

# Usage
rename_files("memes")