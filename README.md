# LazyScript - Automate Your Daily Tasks

LazyScript is a lightweight and efficient automation tool that streamlines daily tasks by allowing users to open apps, organize files, set reminders, schedule shutdowns, and create custom automation tasks with ease.

## Features

✅ Open multiple applications with one command\
✅ Organize files into folders based on extensions\
✅ Schedule system shutdown\
✅ Set reminders with a delay\
✅ Create and execute custom automation tasks

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/o4pixel/LazyScript.git
   cd LazyScript
   ```
2. **Run the script:**
   ```sh
   python lazyscript.py
   ```

## Usage

When you run the script, you'll see a menu with options:

1️⃣ **Open Apps** – Enter app names separated by commas (e.g., `chrome, vscode`).\
2️⃣ **Organize Files** – Enter a directory path to sort files by type.\
3️⃣ **Schedule Shutdown** – Set a shutdown timer in minutes.\
4️⃣ **Set Reminder** – Create a reminder with a message and time delay.\
5️⃣ **Configure Custom Task** – Save a custom automation task.\
6️⃣ **Execute Custom Task** – Run a previously saved task.\
7️⃣ **Exit** – Close the script.

## Example Usage

- To open Chrome and VS Code:
  ```
  Enter choice: 1
  Enter app names: chrome, vscode
  ```
- To organize files in a folder:
  ```
  Enter choice: 2
  Enter directory path: C:\Users\YourName\Downloads
  ```
- To create a task to open Notepad:
  ```
  Enter choice: 5
  Enter task name: quick_notes
  Enter commands: notepad.exe
  ```
- To execute a saved task:
  ```
  Enter choice: 6
  Enter task name: quick_notes
  ```

## License

This project is licensed under the MIT License.

