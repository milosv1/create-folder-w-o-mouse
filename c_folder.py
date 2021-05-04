#Objective of this is to create a simple script to create folders without use of mouse.
import sys, platform, os, datetime
from pynput import keyboard


get_platform = sys.platform
KEY_COMBO = {keyboard.Key.tab, keyboard.KeyCode.from_char('n')}
current = set()
date_now = datetime.datetime.now()


def c_folder_windows(key):
    if sys.platform == "win32" or sys.platform == "darwin": 
        if key in KEY_COMBO:
            current.add(key)
            if all(k in current for k in KEY_COMBO):
                print(f"{KEY_COMBO} pressed.")            
                folder_name = input("Folder name:")
                parent_dirname = "C:/U/A/D/"   #Location of where folder will go when created.   
                is_dir = os.path.isdir(parent_dirname)
                if is_dir is True and len(folder_name) >= 1:
                    print("Path is valid.")
                    path = os.path.join(parent_dirname, folder_name)
                    os.mkdir(path)
                    print(f'Folder {folder_name}, created in {parent_dirname} on {date_now}.')  
                else:
                    print("Unable to create folder.")         
        if key == keyboard.Key.esc: 
            listener.stop()
            print("ESC pressed, Action stopped.")
                
                   
def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=c_folder_windows, on_release=on_release) as listener:
    listener.join()


def main():
    c_folder_windows(key='')
    on_release(key='')


if __name__ == '__main__':
    main()

   