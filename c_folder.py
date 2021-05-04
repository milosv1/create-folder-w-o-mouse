#Objective of this is to create a simple script to create folders without use of mouse.
import sys
import platform
import os
from pynput import keyboard
import datetime


get_platform = sys.platform
#checks the key combo -> tab + n
KEY_COMBO = {keyboard.Key.tab, keyboard.KeyCode.from_char('n')}
current = set()
date_now = datetime.datetime.now()


def c_folder_windows(key):
    if sys.platform.startswith("win32") or sys.platform.startswith("darwin"): #check if platform is windows or macOS
        print(f"Operating System: {get_platform}")
        if key in KEY_COMBO:
            current.add(key)
            if all(k in current for k in KEY_COMBO):
                print(f"{KEY_COMBO} working!")            
                folder_name = input("Folder name: ")
                parent_dirname = "C:/Users/Admin/Desktop/"   #Location of where folder will go when created.   
                is_dir = os.path.isdir(parent_dirname)
                if is_dir is True and len(folder_name) >= 1:
                    print("Path is True")
                    path = os.path.join(parent_dirname, folder_name)
                    os.mkdir(path)
                    print(f'Folder {folder_name} created in {parent_dirname} on {date_now}')  
                else:
                    print("Unable to proceed.")         
        if key == keyboard.Key.esc: 
            listener.stop()
            print(f"{key} pressed, Action stopped.")
                
                   

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

with keyboard.Listener(on_press=c_folder_windows, on_release=on_release) as listener:
    listener.join()



c_folder_windows(key='')   
#c_folder_mac()        