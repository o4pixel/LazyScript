import os
import subprocess
import platform
import json

# Load user configuration
CONFIG_FILE = "lazyscript_config.json"
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def open_apps(apps):
    """Opens a list of applications based on the OS."""
    os_type = platform.system()
    for app in apps:
        try:
            if os_type == "Windows":
                subprocess.Popen(["start", "", app], shell=True)
            elif os_type == "Darwin":  # macOS
                subprocess.Popen(["open", "-a", app])
            else:  # Linux
                subprocess.Popen([app])
            print(f"Opened: {app}")
        except Exception as e:
            print(f"Failed to open {app}: {e}")

def organize_files(directory):
    """Organizes files in the given directory into folders by extension."""
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            ext = file.split(".")[-1] if "." in file else "others"
            ext_folder = os.path.join(directory, ext.upper())
            os.makedirs(ext_folder, exist_ok=True)
            os.rename(file_path, os.path.join(ext_folder, file))
    print("Files organized successfully.")

def shutdown_timer(minutes):
    """Schedules a system shutdown in given minutes."""
    os_type = platform.system()
    seconds = minutes * 60
    if os_type == "Windows":
        os.system(f"shutdown /s /t {seconds}")
    elif os_type == "Darwin" or os_type == "Linux":
        os.system(f"shutdown -h +{minutes}")
    print(f"Shutdown scheduled in {minutes} minutes.")

def set_reminder(message, time_seconds):
    """Sets a reminder after a given number of seconds."""
    print(f"Reminder set for {time_seconds} seconds: {message}")
    import time
    time.sleep(time_seconds)
    print(f"REMINDER: {message}")

def configure_task(task_name, commands):
    """Saves a new task configuration."""
    config = load_config()
    config[task_name] = commands
    save_config(config)
    print(f"Task '{task_name}' saved successfully!")

def execute_task(task_name):
    """Executes a saved task."""
    config = load_config()
    if task_name in config:
        for command in config[task_name]:
            subprocess.Popen(command, shell=True)
        print(f"Executed task: {task_name}")
    else:
        print("Task not found.")

def main():
    print("LazyScript - Automate Your Daily Tasks!")
    while True:
        print("\nOptions:")
        print("1. Open Apps")
        print("2. Organize Files")
        print("3. Schedule Shutdown")
        print("4. Set Reminder")
        print("5. Configure Custom Task")
        print("6. Execute Custom Task")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            apps = input("Enter app names separated by commas: ").split(",")
            open_apps([app.strip() for app in apps])
        elif choice == "2":
            directory = input("Enter directory path: ")
            organize_files(directory)
        elif choice == "3":
            minutes = int(input("Enter minutes until shutdown: "))
            shutdown_timer(minutes)
        elif choice == "4":
            message = input("Enter reminder message: ")
            time_seconds = int(input("Enter time in seconds: "))
            set_reminder(message, time_seconds)
        elif choice == "5":
            task_name = input("Enter task name: ")
            commands = input("Enter commands separated by commas: ").split(",")
            configure_task(task_name, [cmd.strip() for cmd in commands])
        elif choice == "6":
            task_name = input("Enter task name: ")
            execute_task(task_name)
        elif choice == "7":
            print("Exiting LazyScript!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
