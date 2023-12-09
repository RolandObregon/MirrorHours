import shutil
import getpass
import os
USER_NAME = getpass.getuser()
destination = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
app = os.path.abspath(os.getcwd()) + "\main.py"
shutil.move(app, destination)
# made for windows so start up folder won´t work on mac/linux