import shutil
import getpass
import os
import subprocess
import sys
USER_NAME = getpass.getuser()
destination = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
app = os.path.abspath(os.getcwd()) + "\main.pyw"
try:
    shutil.move(app, destination)
except:
    "Error while moving main.py to the startup folder"
# made for windows so start up folder won´t work on mac/linux
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "plyer"])
except:
    "Error while installing plyer or it has been already installed"

