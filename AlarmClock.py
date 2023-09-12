import tkinter
import datetime
import time

class Clock():
    def __init__(self) -> None:
        self.AmPm=False
        self.clockWindow = tkinter.Tk() # create window for alarm clock 
        self.clockWindow.title="Clock" #window title

        self.mainDisplay=tkinter.Text(self.clockWindow, font=("Arial", 22), height=1, width=25)
        self.mainDisplay.pack(padx=15,pady=15)
        self.displayTime()
        self.showDate=tkinter.Button(self.clockWindow,text="Display Date", font=("Calabri", 15),command=self.displayDate)
        self.showDate.pack()
        self.showTime=tkinter.Button(self.clockWindow,text="Display Time", font=("Calabri", 15),command=self.displayTime)
        self.showTime.pack()
        self.setAmPm=tkinter.Button(self.clockWindow,text="Set AM/PM", font=("Calabri", 15),command=self.setTimeType)
        self.setAmPm.pack()
        self.setAlarmClock=tkinter.Button(self.clockWindow,text="Set Alarm", font=("Calabri", 15),command=self.setAlarm)
        self.setAlarmClock.pack()
        self.setZero=tkinter.Button(self.clockWindow,text="0", font=("Calabri", 15),command=self.inputZero)
        self.setZero.pack()
        self.setOne=tkinter.Button(self.clockWindow,text="1", font=("Calabri", 15),command=self.inputOne)
        self.setOne.pack()
        self.setTwo=tkinter.Button(self.clockWindow,text="2", font=("Calabri", 15),command=self.inputTwo)
        self.setTwo.pack()
        self.setThree=tkinter.Button(self.clockWindow,text="3", font=("Calabri", 15),command=self.inputThree)
        self.setThree.pack()
        self.setFour=tkinter.Button(self.clockWindow,text="4", font=("Calabri", 15),command=self.inputFour)
        self.setFour.pack()
        self.setFive=tkinter.Button(self.clockWindow,text="5", font=("Calabri", 15),command=self.inputFive)
        self.setFive.pack()
        self.setSix=tkinter.Button(self.clockWindow,text="6", font=("Calabri", 15),command=self.inputSix)
        self.setSix.pack()
        self.setSeven=tkinter.Button(self.clockWindow,text="7", font=("Calabri", 15),command=self.inputSeven)
        self.setSeven.pack()
        self.setEight=tkinter.Button(self.clockWindow,text="8", font=("Calabri", 15),command=self.inputEight)
        self.setEight.pack()
        self.setNine=tkinter.Button(self.clockWindow,text="9", font=("Calabri", 15),command=self.inputNine)
        self.setNine.pack()
        
        self.clockWindow.mainloop()# run the window
    def displayDate(self):
        self.mainDisplay.config(state="normal")
        self.mainDisplay.delete(1.0,"end")
        self.mainDisplay.insert(1.0,datetime.datetime.now().strftime("%B %d-%m-%y"))
        self.mainDisplay.config(state="disabled")
    def displayTime(self):
        hr=datetime.datetime.now().hour
        minute=datetime.datetime.now().minute
        if self.AmPm==True:
            if hr >12:
                hr=hr-12
        nextMinute=(60-datetime.datetime.now().second)*1000
        self.mainDisplay.config(state="normal")
        self.mainDisplay.delete(1.0,"end")
        if minute<10:
            self.mainDisplay.insert(1.0,str(hr)+":0"+str(minute))
        else:
            self.mainDisplay.insert(1.0,str(hr)+":"+str(minute))
        self.mainDisplay.config(state="disabled")
        self.clockWindow.after(nextMinute,self.displayTime)
    def timer(self):
        pass
    def setAlarm(self):
        self.mainDisplay.config(state="normal")
        self.mainDisplay.delete(1.0,"end")
        self.mainDisplay.insert(1.0,"00:12")
        self.mainDisplay.config(state="disabled")
    def snooze(self):
        pass
    def setTimeType(self):
        if self.AmPm==False:
            self.AmPm=True
        else:
            self.AmPm=False
        self.displayTime()
    def inputNumber(self,number):
        self.mainDisplay.config(state="normal")
        alarm=self.mainDisplay.get(1.0,"end")
        alarm=alarm[0:2]+alarm[3:]
        alarm=alarm.strip("\n")
        alarm=alarm[1:3]+":"+alarm[3:]
        alarm=alarm+str(number)
        print(alarm)
        self.mainDisplay.delete(1.0,"end")
        self.mainDisplay.insert(1.0,alarm)
        self.mainDisplay.config(state="disabled")
    def inputZero(self):
        self.inputNumber(0)
    def inputOne(self):
        self.inputNumber(1)
    def inputTwo(self):
        self.inputNumber(2)
    def inputThree(self):
        self.inputNumber(3)
    def inputFour(self):
        self.inputNumber(4)
    def inputFive(self):
        self.inputNumber(5)
    def inputSix(self):
        self.inputNumber(6)
    def inputSeven(self):
        self.inputNumber(7)
    def inputEight(self):
        self.inputNumber(8)
    def inputNine(self):
        self.inputNumber(9)

C=Clock()
