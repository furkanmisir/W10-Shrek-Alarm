import time
#from playsound import playsound
import os
from win10toast import ToastNotifier

#a_hour == alarm hour
toaster = ToastNotifier()
while True:
    a_hour = input("Welcome to alarm app.\nPlease set the alarm.\nFirst, enter the hour (Like 16):  ")
    a_min = input("Now, please enter the minute: ")
    a_comment = input("Do you want to add a comment to your alarm: ")

    try:
        a_hour = int(a_hour)
        a_min = int(a_min)
        
    except ValueError:
        os.system("cls")
        print("Invalid syntax! Please enter the values ​​in the appropriate format.")
        continue

    break

os.system("cls")

a_min = str(a_min)
a_hour = str(a_hour)

if len(a_min) == 1 or len(a_hour) == 1 :
    a_min = "0" + a_min
    a_hour = "0" + a_hour
else:
    pass

a_time = a_hour + ":" + a_min

while True:
    pc_time = time.localtime(time.time())
    if int(a_hour) == pc_time.tm_hour and int(a_min) == pc_time.tm_min:
        print(a_comment, ", ", a_hour, ":", a_min)
        toaster.show_toast(a_comment, a_time, icon_path="Alarm.app/shrek.ico", duration=10)
        #playsound('/alarm.mp3' )
        os.system("start Alarm.app/shrek-alarm.mp4")
        break
    else:
        pass