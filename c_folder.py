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
        if key in KEY_COMBO:
            current.add(key)
            if all(k in current for k in KEY_COMBO):
                print(f"{KEY_COMBO} working!")            
                folder_name = input("Folder name: ")
                parent_dirname = "C:/#/#/#/"   #Location of where folder will go once created.   
                path = os.path.join(parent_dirname, folder_name)
                os.mkdir(path)
                print(f'Directory {folder_name} created on {date_now}')       
        if key == keyboard.Key.esc: #when folder name is entered, it will go here, when pressing esc it will close the program.
            listener.stop()
                
                   

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

with keyboard.Listener(on_press=c_folder_windows, on_release=on_release) as listener:
    listener.join()



c_folder_windows(key='')   
#c_folder_mac()        