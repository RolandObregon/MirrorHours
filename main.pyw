from plyer import notification as noti
from datetime import datetime as dt
import time
try:
    while setting == 1 or setting == 3:
        hora = dt.today().strftime('%H:%M')
        if dt.today().strftime('%H') == dt.today().strftime('%M'):
            noti.notify(title=hora, message="<3", app_name="MirrorHour")
            time.sleep(59)
        if dt.today().strftime('%S') == "02":
            time.sleep(58)
    while setting == 2 or setting == 3:
        hora = dt.today().strftime('%H:%M')
        if dt.today().strftime('%H') == dt.today().strftime('%M')[::-1] and dt.today().strftime('%H') != "00":
            noti.notify(title=hora, message="<3", app_name="MirrorHour")
            time.sleep(59)
        if dt.today().strftime('%S') == "02":
            time.sleep(58)

except:
    print("install.py was not used for setup")
