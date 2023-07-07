from tkinter import *
import datetime
import time
import winsound
 
def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg="Current Time: "+str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("alarm.wav",winsound.SND_ASYNC)
            break
 
def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)
 
window = Tk()
window.title("Alarm Clock")
window.geometry("700x380")
window.config(bg="#922B21")
window.resizable(width=False,height=False)
 
time_format=Label(window, text= "Remember to set time in 24 hour format!!!", fg="white",bg="#922B21",font=("Arial bold",20)).place(x=82,y=310)
addTime = Label(window,text = "Hour     Min     Sec",font=("Arial bold",20),fg="white",bg="black").place(x = 235,y=120)
setYourAlarm = Label(window,text = "Set Time for Alarm ",fg="white",bg="#922B21",font=("Arial",30,"bold")).place(x=180, y=40)
 
hour = StringVar()
min = StringVar()
sec = StringVar()
 
hourTime= Entry(window,textvariable = hour,bg = "#48C9B0",width = 4,font=(20)).place(x=245,y=180)
minTime= Entry(window,textvariable = min,bg = "#48C9B0",width =4,font=(20)).place(x=335,y=180)
secTime = Entry(window,textvariable = sec,bg = "#48C9B0",width = 4,font=(20)).place(x=420,y=180)
 
submit = Button(window,text = "Set Your Alarm",fg="Black",bg="#b2b3d6",width = 18,command = get_alarm_time,font=("Arial bold",20)).place(x =200,y=240)
 
window.mainloop()
