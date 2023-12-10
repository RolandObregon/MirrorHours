from plyer import notification as noti
from datetime import datetime as dt
import time
while True:
    hora = dt.today().strftime('%I:%M')
    triplehour = {"1":"11", "2":"22", "3":"33", "4":"44", "5":"55"}
    if dt.today().strftime('%I:%M %P') == "12:13 AM":
        noti.notify(title="Good Night", message="Go to sleep", app_name="MirrorHour")
        break
    if dt.today().strftime('%I') == dt.today().strftime('%M'):
        noti.notify(title=hora, message="<3", app_name="MirrorHour")
        time.sleep(59)
    if dt.today().strftime('%I') in triplehour.keys() and dt.today().strftime('%M') == triplehour.get(dt.today().strftime('%I')):
        noti.notify(title=hora, message="<3", app_name="MirrorHour")
        time.sleep(59)
    if dt.today().strftime('%S') == "02":
        time.sleep(58)