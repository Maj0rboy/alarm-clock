from tkinter import *
import datetime
import time
import winsound
root = Tk()
root.title("Alarm clock")
root.geometry("400x400")

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time =datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date =current_time.strftime("%d/%m/%y")
        # print("the set date is: ",date)
        mylabel = Label(root, text="the set date is " + date, fg="blue",relief="solid").place(x=100, y=80)
        # print(now)
        mylabel2 = Label(root, text=now, fg="blue",relief="solid").place(x=100, y=100)
        if now == set_alarm_timer:
            print("Time to wake up")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        break
        

def actual_time():
    set_alarm_timer = f"{hour.get()} : {min.get()} :{sec.get()}"
    alarm(set_alarm_timer)
# labels
time_format = Label(root, text="enter time in 24 hour format", fg="red", bg="black",font="Arial").place(x=60, y=120)
addtime = Label(root, text="Hour Min Sec", font=60).place(x=110)
setYourAlarm = Label(root, text="when to wake you up",fg="blue",relief="solid", font=("Helevetica",7,"bold")).place(x=100, y=150)

# variables
hour = StringVar()
min = StringVar()
sec = StringVar()
# entry boxes
hourTime = Entry(root, textvariable=hour, bg="pink",width=15).place(x=110, y=30)
minTime = Entry(root, textvariable=min, bg="pink",width=15).place(x=150, y=30)
secTime = Entry(root, textvariable=sec, bg="pink",width=15).place(x=200, y=30)
# submit button
btn = Button(root, text="Set Alarm", fg="red",width=10,command=actual_time).place(x=110, y=170)

mainloop()
