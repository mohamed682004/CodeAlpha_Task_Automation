# 🤖 Task Automation with Python

## 📂 File Organization Made Simple

A smart Python script that brings order to chaos by automatically organizing your messy folders! Part of my internship projects at CodeAlpha.

### ✨ Features

- **Automatic File Sorting**: Intelligently sorts files based on their types
- **Custom Categories**: Organizes files into dedicated folders:
  - 📸 Images (.jpg, .jpeg, .png, .gif)
  - 📄 Documents (.pdf, .doc, .docx, .txt)
  - 🎥 Videos (.mp4, .avi, .mov)
  - 🎵 Music (.mp3, .wav, .flac)
  - 📦 Others (for everything else)
- **Safe Operation**: Preserves original files while organizing
- **Progress Tracking**: Keeps you informed with console updates

### 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohamed682004/CodeAlpha_Task_Automation.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd CodeAlpha_Task_Automation
   ```

3. **Run the script**
   ```python
   python file_organizer.py
   ```

### 💡 How to Use

1. Open the script in your favorite editor
2. Replace the `target_directory` with your folder path:
   ```python
   target_directory = "YOUR/PATH/HERE"
   ```
3. Run the script and watch your files organize themselves!

### ⚙️ Customization

Want to add more file types or categories? Simply modify the `folders` dictionary:
```python
folders = {
    'YourCategory': ['.extension1', '.extension2'],
    # Add more categories here
}
```

### 🛠️ Requirements

- Python 3.x
- Standard Python libraries (os, shutil, pathlib)

### 📝 Project Structure

```
CodeAlpha_Task_Automation/
│
├── file_organizer.py    # Main script
└── README.md           # Project documentation
```

### 🤝 Contributing

Feel free to fork, improve, and make pull requests. Let's make file organization even better together!

### 📜 License

This project is open source and available under the [MIT License](LICENSE).

### 👨‍💻 Author

Mohamed - CodeAlpha Intern
