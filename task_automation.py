import os
import shutil
from pathlib import Path

def create_folders(directory):
    """Create folders for different file types if they don't exist"""
    folders = {
        'Python': ['.py', '.pyw', '.pyc', '.pyo', '.pyd', '.ipynb'],
        'JavaScript': ['.js', '.jsx', '.ts', '.tsx', '.json', '.vue'],
        'WebDev': ['.html', '.css', '.scss', '.sass', '.less'],
        'Java': ['.java', '.class', '.jar'],
        'CSharp': ['.cs', '.csx', '.csproj'],
        'DataScience': ['.ipynb', '.csv', '.dat', '.db', '.sql'],
        'Config': ['.yml', '.yaml', '.toml', '.ini', '.cfg', '.conf'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.md', '.rst'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Music': ['.mp3', '.wav', '.flac', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Others': []
    }
    
    # Create folders if they don't exist
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    return folders

def get_folder_for_file(filename, folders):
    """Determine the appropriate folder for a file based on its extension"""
    file_ext = os.path.splitext(filename)[1].lower()
    
    # Special handling for Jupyter notebooks
    if file_ext == '.ipynb':
        return 'DataScience'
    
    # Check file extension against all folder types
    for folder, extensions in folders.items():
        if file_ext in extensions:
            return folder
    
    # Handle special naming patterns
    filename_lower = filename.lower()
    if any(name in filename_lower for name in ['readme', 'license', 'changelog']):
        return 'Documents'
    
    return 'Others'

def organize_files(directory):
    """Organize files into appropriate folders based on their types"""
    folders = create_folders(directory)
    
    # Counter for statistics
    stats = {folder: 0 for folder in folders}
    
    print("🚀 Starting file organization...")
    
    # Get all files in the directory
    for file in os.listdir(directory):
        source = os.path.join(directory, file)
        
        # Skip if it's a directory
        if os.path.isdir(source):
            continue
            
        # Determine destination folder
        destination_folder = get_folder_for_file(file, folders)
        destination = os.path.join(directory, destination_folder, file)
        
        try:
            shutil.move(source, destination)
            stats[destination_folder] += 1
            print(f"📦 Moved {file} to {destination_folder}")
        except Exception as e:
            print(f"❌ Error moving {file}: {str(e)}")
    
    # Print summary
    print("\n📊 Organization Summary:")
    for folder, count in stats.items():
        if count > 0:
            print(f"  {folder}: {count} files")

# Example usage
if __name__ == "__main__":
    # Replace this with your directory path
    target_directory = "C:/Users/YourUsername/Downloads"  
    print(f"🎯 Target Directory: {target_directory}")
    print("⚙️ Initializing file organization...")
    organize_files(target_directory)
    print("\n✨ Organization complete! Your files are now properly sorted.")
