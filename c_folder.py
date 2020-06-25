#Objective of this is to create a simple script to create folders without use of mouse.
import sys
import platform
import os

get_platform = sys.platform

def c_folder_windows():
    if sys.platform.startswith("win32"):
        print("on windows")
    else:
        print("not on windows") 


def c_folder_mac():
    if sys.platform.startswith("darwin"):
        print("platform you're on is macOS")
        
    else:
         print("not macOS ")    
         print(f"current plaform: {get_platform}")


c_folder_windows()   
c_folder_mac()        