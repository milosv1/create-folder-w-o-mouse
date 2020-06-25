#Objective of this is to create a simple script to create folders without use of mouse.
import sys
import platform
import os
def c_folder_windows():
    if sys.platform.startswith("win32"):
        print("on windows")
    else:
        print("not on windows") 


c_folder_windows()           