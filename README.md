# OrthoNome
Spelling correction program (French and English) using clipboard and keyboard shortcuts. Works with the OpenAI API, so you need an account and credits to obtain an API key.

## Prerequisites
- Python 3.6 or higher (tested with Python 3.14)
- Internet connection for OpenAI API
- The following Python modules:
  - `openai`: To access the OpenAI API
  - `pyperclip`: To manage the clipboard
  - `playsound` (version 1.2.2 recommended): For sound notification

## Installation on a new computer
1. Install Python from [the official website](https://www.python.org/downloads/)
   - **Important:** Check the "Add Python to PATH" option during installation

2. Install the required modules via pip:
   ```
   pip install openai pyperclip playsound==1.2.2
   ```
   - If you encounter issues with playsound, try these alternatives:
     ```
     pip install playsound==1.3.0
     ```
     or use pygame as an alternative.

3. Download all project files:
   - OrthoNome.py
   - exec.bat
   - correct.mp3
   - LICENSE (optional)
   - README.md (this file)

4. Modify the API key in OrthoNome.py:
   - Replace "xxxx" with your personal OpenAI API key

5. Create a shortcut for exec.bat and place it on your desktop

6. Access the shortcut properties to assign a key combination (e.g., Ctrl + Alt + Numpad 1)

## Troubleshooting
- If pip is not recognized, try `python -m pip` instead
- Make sure the "correct.mp3" audio file is in the same directory as the script
- Verify that your OpenAI API key is valid and has sufficient credits
