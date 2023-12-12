import shutil
import getpass
import os
import subprocess
import sys
while True:
    try:
        settimes = int(input("Type a setting"))
        if settimes in (1, 2, 3):
            break
        else:
            print("Only 3 settings available")
    except:
        print("Not valid input")
setting = settimes
with open("main.pyw", "r+") as f:
    lines = f.readlines()
    f.seek(0)
    f.write("setting = " + str(settimes) + "\n")
    for line in lines:
        f.write(line)

USER_NAME = getpass.getuser()
destination = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
app = os.path.abspath(os.getcwd()) + "\main.pyw"
try:
    shutil.move(app, destination)
except:
    "Error while moving main.pyw to the startup folder"
# made for windows so start up folder won´t work on mac/linux
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "plyer"])
except:
    "Error while installing plyer or it has been already installed"

