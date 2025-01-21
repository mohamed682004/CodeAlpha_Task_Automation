# CodeAlpha Task Automation: File Organizer 🚀

Welcome to the **CodeAlpha Task Automation** repository! This project is designed to help you automate the tedious task of organizing files in your directory. Whether you're a developer, data scientist, or just someone with a cluttered Downloads folder, this tool will save you time and keep your files neatly sorted.

---

## 📁 **About the Project**

This Python script automatically organizes files in a specified directory into categorized folders based on their file types. It supports a wide range of file extensions, including Python scripts, JavaScript files, images, documents, videos, and more. The script is highly customizable and easy to use.

### Key Features:
- **Automated File Sorting**: Moves files into appropriate folders based on their extensions.
- **Customizable Categories**: Add or modify file type categories to suit your needs.
- **Special Handling**: Recognizes README, LICENSE, and CHANGELOG files and sorts them into the "Documents" folder.
- **Statistics**: Provides a summary of how many files were moved to each folder.
- **Error Handling**: Gracefully handles errors and logs them for debugging.

---

## 🛠️ **How It Works**

1. **Folder Creation**: The script creates folders for different file types (e.g., Python, JavaScript, Images, etc.) if they don't already exist.
2. **File Sorting**: It scans the directory, identifies each file's type, and moves it to the corresponding folder.
3. **Special Cases**: Files like Jupyter Notebooks (`.ipynb`) are sorted into the "DataScience" folder, while README-like files go into "Documents."
4. **Summary**: After organizing, the script prints a summary of how many files were moved to each folder.

---

## 🚀 **Getting Started**

### Prerequisites
- Python 3.x
- Basic knowledge of running Python scripts.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/mohamed682004/CodeAlpha_Task_Automation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CodeAlpha_Task_Automation
   ```

### Usage
1. Open the script `file_organizer.py` and update the `target_directory` variable with the path to the directory you want to organize.
   ```python
   target_directory = "C:/Users/YourUsername/Downloads"  # Replace with your directory path
   ```
2. Run the script:
   ```bash
   python file_organizer.py
   ```
3. Sit back and watch as your files are automatically organized! 🎉

---

## 📂 **Folder Structure**

Here’s how the script organizes files:

| Folder Name   | File Extensions                                      |
|---------------|------------------------------------------------------|
| Python        | `.py`, `.pyw`, `.pyc`, `.pyo`, `.pyd`, `.ipynb`     |
| JavaScript    | `.js`, `.jsx`, `.ts`, `.tsx`, `.json`, `.vue`       |
| WebDev        | `.html`, `.css`, `.scss`, `.sass`, `.less`          |
| Java          | `.java`, `.class`, `.jar`                           |
| CSharp        | `.cs`, `.csx`, `.csproj`                            |
| DataScience   | `.ipynb`, `.csv`, `.dat`, `.db`, `.sql`             |
| Config        | `.yml`, `.yaml`, `.toml`, `.ini`, `.cfg`, `.conf`   |
| Images        | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.ico`     |
| Documents     | `.pdf`, `.doc`, `.docx`, `.txt`, `.md`, `.rst`      |
| Videos        | `.mp4`, `.avi`, `.mov`, `.mkv`                      |
| Music         | `.mp3`, `.wav`, `.flac`, `.m4a`                     |
| Archives      | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`                |
| Others        | Files that don’t match any category                 |

---

## 🎨 **Customization**

You can easily customize the script to add or remove file types and folders. Simply modify the `folders` dictionary in the `create_folders` function:

```python
folders = {
    'Python': ['.py', '.pyw', '.pyc', '.pyo', '.pyd', '.ipynb'],
    'JavaScript': ['.js', '.jsx', '.ts', '.tsx', '.json', '.vue'],
    # Add or modify categories as needed
}
```

---

## 📊 **Example Output**

```
🎯 Target Directory: C:/Users/YourUsername/Downloads
⚙️ Initializing file organization...
🚀 Starting file organization...
📦 Moved script.py to Python
📦 Moved styles.css to WebDev
📦 Moved image.png to Images
📦 Moved data.csv to DataScience
📦 Moved archive.zip to Archives

📊 Organization Summary:
  Python: 1 files
  WebDev: 1 files
  Images: 1 files
  DataScience: 1 files
  Archives: 1 files

✨ Organization complete! Your files are now properly sorted.
```

---

## 🤝 **Contributing**

Contributions are welcome! If you have ideas for improving this project, feel free to open an issue or submit a pull request. Let’s make file organization even better together!

---

## 📜 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 **Credits**

- **Author**: [Mohamed](https://github.com/mohamed682004)
- **Inspiration**: This project was created as part of the CodeAlpha internship program.

---

## 🎉 **Enjoy a Cleaner Directory!**

Say goodbye to cluttered folders and hello to organized bliss. Happy coding! 🚀
