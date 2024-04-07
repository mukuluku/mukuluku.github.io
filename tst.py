import shutil
import os

def copy_zip_files(source_dir, destination_dir):
    try:
        # List all files in the source directory
        files = os.listdir(source_dir)
        for file in files:
            if file.endswith(".zip"):
                source_file = os.path.join(source_dir, file)
                shutil.copy(source_file, destination_dir)
                print(f"File '{file}' copied successfully to {destination_dir}")
    except Exception as e:
        print(f"Error copying files: {e}")

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the script's location
source_dir = os.path.join(script_dir, "repo", "zips", "repository.mukuluku")
destination_dir = os.path.join(script_dir, "repo")

# Copy zip files
copy_zip_files(source_dir, destination_dir)
