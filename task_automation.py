import os
import shutil
from pathlib import Path

def create_folders(directory):
    """Create folders for different file types if they don't exist"""
    folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Others': []
    }
    
    for folder in folders:
        if not os.path.exists(os.path.join(directory, folder)):
            os.makedirs(os.path.join(directory, folder))
    
    return folders

def organize_files(directory):
    """Organize files into appropriate folders based on their extensions"""
    folders = create_folders(directory)
    
    # Get all files in the directory
    for file in os.listdir(directory):
        # Skip if it's a directory
        if os.path.isdir(os.path.join(directory, file)):
            continue
            
        # Get the file extension
        file_ext = os.path.splitext(file)[1].lower()
        
        # Find the appropriate folder for the file
        destination_folder = 'Others'
        for folder, extensions in folders.items():
            if file_ext in extensions:
                destination_folder = folder
                break
        
        # Move the file
        source = os.path.join(directory, file)
        destination = os.path.join(directory, destination_folder, file)
        
        try:
            shutil.move(source, destination)
            print(f"Moved {file} to {destination_folder}")
        except Exception as e:
            print(f"Error moving {file}: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace this with your directory path
    target_directory = "/home/omran-xy/Downloads"
    organize_files(target_directory)