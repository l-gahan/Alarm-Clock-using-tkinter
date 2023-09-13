import tkinter
import datetime
import time

class Clock():
    def __init__(self) -> None:
        '''
        Initialise and create clock window and buttons
        '''
        self.AmPm=False
        self.clockWindow = tkinter.Tk() # Create window for alarm clock 
        self.clockWindow.title="Clock" #Window title
        
        self.onDisplayScreen=False#Set to true if on the time display screen
        self.setAlarmScreen=False #Set to true if user on screen where you can set alarm
        self.setTimerScreen=False #Set to true if user on screen where you can set timer

        self.alarm="00:00"#Alarm display
        self.timer="00:00"#Timer display
        self.originalTimer="00:00"#Placeholder to keep users original timer value
        self.timerComplete=False#The timer can only run if this variable is false

        self.alarmMessage=False#Variable to change message shown when alarm is activated to indicate urgency
        self.timerMessage=False#Variable to change message shown when timer is activated to indicate urgency

        self.alarmSet=False #Set to true if an alarm has been set by the user to go off at a specific time
        self.timerReady=False#Set to true if user has inputted a time they want to count down from

        # Create a display to show the time/timer/date etc and display the time on it
        self.mainDisplay=tkinter.Text(self.clockWindow, font=("Arial", 22), height=1, width=25)
        self.mainDisplay.grid(padx=15,pady=15,columnspan=6)
        self.displayTime() #Display the time on the screen

        #Create buttons on the window to control the alarm clock
        #Button to display the date
        self.showDate=tkinter.Button(self.clockWindow,text="Display Date", font=("Calabri", 15),command=self.displayDate)
        self.showDate.grid(row=2,column=1,columnspan=6)
        #Button to display the time
        self.showTime=tkinter.Button(self.clockWindow,text="Display Time", font=("Calabri", 15),command=self.displayTime)
        self.showTime.grid(row=3,column=4)
        #Button to change the time from 24hr time to 12hr time
        self.setAmPm=tkinter.Button(self.clockWindow,text="Set AM/PM", font=("Calabri", 15),command=self.setTimeType)
        self.setAmPm.grid(row=3,column=5)
        #Button to go to the screen to set an alarm (also used to set the alarm on the alarm screen)
        self.setAlarmClock=tkinter.Button(self.clockWindow,text="Set Alarm", font=("Calabri", 15),command=self.setAlarm)
        self.setAlarmClock.grid(row=4,column=4)
        #Button to allow user to input 0
        self.setZero=tkinter.Button(self.clockWindow,text="0", font=("Calabri", 15),command=self.inputZero)
        self.setZero.grid(row=6,column=2)
        #Button to allow user to input 1
        self.setOne=tkinter.Button(self.clockWindow,text="1", font=("Calabri", 15),command=self.inputOne)
        self.setOne.grid(row=3,column=1)
        #Button to allow user to input 2
        self.setTwo=tkinter.Button(self.clockWindow,text="2", font=("Calabri", 15),command=self.inputTwo)
        self.setTwo.grid(row=3,column=2)
        #Button to allow user to input 3
        self.setThree=tkinter.Button(self.clockWindow,text="3", font=("Calabri", 15),command=self.inputThree)
        self.setThree.grid(row=3,column=3)
        #Button to allow user to input 4
        self.setFour=tkinter.Button(self.clockWindow,text="4", font=("Calabri", 15),command=self.inputFour)
        self.setFour.grid(row=4,column=1)
        #Button to allow user to input 5
        self.setFive=tkinter.Button(self.clockWindow,text="5", font=("Calabri", 15),command=self.inputFive)
        self.setFive.grid(row=4,column=2)
        #Button to allow user to input 6
        self.setSix=tkinter.Button(self.clockWindow,text="6", font=("Calabri", 15),command=self.inputSix)
        self.setSix.grid(row=4,column=3)
        #Button to allow user to input 7
        self.setSeven=tkinter.Button(self.clockWindow,text="7", font=("Calabri", 15),command=self.inputSeven)
        self.setSeven.grid(row=5,column=1)
        #Button to allow user to input 8
        self.setEight=tkinter.Button(self.clockWindow,text="8", font=("Calabri", 15),command=self.inputEight)
        self.setEight.grid(row=5,column=2)
        #Button to allow user to input 9
        self.setNine=tkinter.Button(self.clockWindow,text="9", font=("Calabri", 15),command=self.inputNine)
        self.setNine.grid(row=5,column=3)
        #Allows user to cancel alarm
        self.Reset=tkinter.Button(self.clockWindow,text="Reset Alarm", font=("Calabri", 15),command=self.resetAlarm)
        self.Reset.grid(row=4,column=5)
        #When clicked shows the time the alarm is set for in 24hr time
        self.showAlarmTime=tkinter.Button(self.clockWindow,text="Show Alarm", font=("Calabri", 15),command=self.showAlarm)
        self.showAlarmTime.grid(row=4,column=6)
        #Allows user to snooze alarm for 25 minutes
        self.setTimer=tkinter.Button(self.clockWindow,text="Snooze", font=("Calabri", 15),command=self.snooze)
        self.setTimer.grid(row=3,column=6)
        #Allows user to set the timer
        self.setTimer=tkinter.Button(self.clockWindow,text="Set Timer", font=("Calabri", 15),command=self.timerSet)
        self.setTimer.grid(row=5,column=4)
        #Allows user to pause the timer
        self.pauseTimer=tkinter.Button(self.clockWindow,text="Pause timer", font=("Calabri", 15),command=self.timerPause)
        self.pauseTimer.grid(row=5,column=5)
        #Allows user to reset the timer
        self.resetTimer=tkinter.Button(self.clockWindow,text="Reset Timer", font=("Calabri", 15),command=self.timerReset)
        self.resetTimer.grid(row=5,column=6)
        #Allows user to start the timer
        self.runTimer=tkinter.Button(self.clockWindow,text="Start Timer", font=("Calabri", 15),command=self.timerRun)
        self.runTimer.grid(row=6,column=5)
        
        self.clockWindow.mainloop()# Run the window
    def displayDate(self):
        '''
        Displays the current date on the display panel
        '''    
        self.onDisplayScreen=False#Set variable to indicate we have changed screens
        self.setAlarmScreen=False#Set variable to indicate we have changed screens
        self.setTimerScreen=False#Set variable to indicate we have changed screens

        self.updateDisplay(datetime.datetime.now().strftime("%B %d-%m-%y"))

    def displayTime(self):
        '''
        Displays the current time on the display panel and can display the alarm if set
        '''
        self.setAlarmScreen=False#Set variable to indicate we have changed screens
        self.setTimerScreen=False#Set variable to indicate we have changed screens

        symbolAmPm=""#Variable to display am/pm if user requires it
        self.onDisplayScreen=True#Variable to allow time to update but ONLY when in this screen
        hr=datetime.datetime.now().hour#Get the current hour
        minute=datetime.datetime.now().minute#Get the current minute
        #If the alarm is set and it is time for it to do so display the alarm message
        if ((str(hr)+":"+str(minute)==self.alarm) or int(self.alarm[0:2]) <hr or (int(self.alarm[0:2]) ==hr and int(self.alarm[-2:])<=minute))and self.alarmSet==True:
            self.displayAlarm()
        
        #If the user has selected it convert the current time from 24 hour time to 12 hour time and update the variable to the correct suffix
        if self.AmPm==True:
            if hr >12:
                symbolAmPm="PM"
                hr=hr-12
            else:
                symbolAmPm="AM"

        nextMinute=(60-datetime.datetime.now().second)*1000#calculate how many seconds until the next minute on the clock

        #if the minute on display is less than 10 add an extra 0 to the display so that 0 is not erased when converting the minute to a string
        if minute<10:
            self.updateDisplay(str(hr)+":0"+str(minute)+" "+symbolAmPm)
        else:
            self.updateDisplay(str(hr)+":"+str(minute)+" "+symbolAmPm)
        
        #\If the user is still on this screen update the time when it is appropriate
        if self.onDisplayScreen==True:
            self.clockWindow.after(nextMinute,self.displayTime)

    def displayAlarm(self):
        '''
        Displays Alarm when time is reached
        '''
        self.onDisplayScreen=False#Set variable to indicate we have changed screens
        self.setTimerScreen=False#Set variable to indicate we have changed screens

        #When called change message every time it loops until alarm is canceled
        if self.alarmMessage==False:
            self.updateDisplay("-----")
            self.alarmMessage=True
        else:        
            self.alarmMessage=False
            self.updateDisplay("Alarm")
        #While alarm is set loop again and change message
        if self.alarmSet==True:
            self.clockWindow.after(1000,self.displayAlarm)

    def setAlarm(self):
        '''
        Sets the alarm time (in 24 hour time) by user inputting numbers one by one (scrolling left to right)
        '''
        self.onDisplayScreen=False#Set variable to indicate we have changed screens
        self.setTimerScreen=False#Set variable to indicate we have changed screens

        #Set variable to true to allow users to edit alarm if users just entered this screen
        if self.setAlarmScreen==False:
            self.setAlarmScreen=True
            self.updateDisplay("00:00")#set to 00:00 as a common starting point

        #else the user was already on the screen and now wishes to set the inputted time as their alarm
        else:
            alarm=self.mainDisplay.get(1.0,"end")
            #If inputted time isn't a viable time display an error
            if int(alarm[0:2])>23 or int(alarm[-3])>5:
                self.updateDisplay("Error")

            #else set the alarm and update variables as appropriate
            else:
                self.alarm=alarm
                self.alarmSet=True
                self.updateDisplay("Alarm Set")

            self.setAlarmScreen=False#stop users being able to change the screen

    def snooze(self):
        '''
        "Snoozes" the alarm and adds an extra 25 minutes before the alarm goes off again 
        '''
        self.onDisplayScreen=False#Set variable to indicate we have changed screens
        self.setTimerScreen=False#Set variable to indicate we have changed screens
        
        #Get the current time and add 15 minutes for a snooze period
        hr=datetime.datetime.now().hour
        minute=datetime.datetime.now().minute+15

        #If increasing by 15 minutes creates an invalid time update the hour and minutes to create a valid time
        if minute>59:
            minute-=59
            hr+=1
        if minute<10:
            minute="0"+str(minute)#Add back in the zero that would have been lost when casting the minute to a string
        else:
            minute=str(minute)
        if hr>23:
            hr="00"

        self.alarm=str(hr)+":"+minute#Update the new alarm time
        self.showAlarm()#Display the new alarm time to the user
        
    def setTimeType(self):
        '''
        Allows user to switch the clock display from 24 hour time to 12 hour time
        '''
        #Set the AmPm variable to true or false each time the user presses the button to indicate which time type they want
        if self.AmPm==False:
            self.AmPm=True
        else:
            self.AmPm=False
        
        self.displayTime()#Display the new time

    def inputNumber(self,number):
        '''
        helper function to help input numbers into the alarm or timer screen 
        '''
        #Get the time currently displayed and shift all the numbers one position to the left
        #In doing so the first digit will be removed and place the users inputted digit into the last place of the number
        #Eg. 12:34 with the user inputting 5 would become 23:45
        if self.setAlarmScreen==True or self.setTimerScreen==True:

            curSetTime=self.mainDisplay.get(1.0,"end")#get the displayed number
            curSetTime=curSetTime[0:2]+curSetTime[3:]#remove the ":"
            curSetTime=curSetTime[:-1]#remove \n as .get() includes a \n at the last position of the number
            curSetTime=curSetTime[1:3]+":"+curSetTime[3:]#reassemble the number with the first and last digits removed
            curSetTime=curSetTime+str(number)#add the new digit

            self.updateDisplay(curSetTime)#Update the time displayed

    def inputZero(self):
        '''
        Helper function to set alarm and timer (Inputs 0)
        '''
        self.inputNumber(0)
    
    def inputOne(self):
        '''
        Helper function to set alarm and timer (Inputs 1)
        '''
        self.inputNumber(1)
    
    def inputTwo(self):
        '''
        Helper function to set alarm and timer (Inputs 2)
        '''
        self.inputNumber(2)
    
    def inputThree(self):
        '''
        Helper function to set alarm and timer (Inputs 3)
        '''
        self.inputNumber(3)
    
    def inputFour(self):
        '''
        Helper function to set alarm and timer (Inputs 4)
        '''
        self.inputNumber(4)
    
    def inputFive(self):
        '''
        Helper function to set alarm and timer (Inputs 5)
        '''
        self.inputNumber(5)
    
    def inputSix(self):
        '''
        Helper function to set alarm and timer (Inputs 6)
        '''
        self.inputNumber(6)
    
    def inputSeven(self):
        '''
        Helper function to set alarm and timer (Inputs 6)
        '''
        self.inputNumber(7)
    
    def inputEight(self):
        '''
        Helper function to set alarm and timer (Inputs 8)
        '''
        self.inputNumber(8)
    
    def inputNine(self):
        '''
        Helper function to set alarm and timer (Inputs 9)
        '''
        self.inputNumber(9)
    
    def showAlarm(self):
        '''
        Function which shows in the display what time the alarm is set for
        '''
        self.onDisplayScreen=False#Set variable to indicate we have changed screens
        self.setAlarmScreen=False#Set variable to indicate we have changed screens
        self.setTimerScreen=False#Set variable to indicate we have changed screens
        
        #If alarm is set show the user the alarm else show an error message
        if self.alarmSet==True:
            self.updateDisplay(self.alarm)
        else:
            self.updateDisplay("Alarm not Set")
    
    def resetAlarm(self):
        '''
        Function which turns off the alarm
        '''
        self.onDisplayScreen=False#Set variable to indicate we have changed screens
        
        # If the alarm is set reset its variables and display message saying it has been reset
        if self.alarmSet==True:
            self.alarm="00:00"#set alarm back to placeholder
            self.alarmSet=False
            self.updateDisplay("Alarm Off")

        #Else show a message that no alarm is set
        else:
            self.updateDisplay("Alarm not Set")
    
    def timerSet(self):
        '''
        Function which sets the timer
        '''
        self.onDisplayScreen=False#Set variable to indicate we have changed screens
        self.setAlarmScreen=False#Set variable to indicate we have changed screens
        
        # If user wasnt already on the screen update variable so they can edit and show placeholder
        if self.setTimerScreen==False:
            self.setTimerScreen=True
            self.updateDisplay("00:00")
        else:
            timer=self.mainDisplay.get(1.0,"end")[:-1]#Get the inputted time and remove \n

            # If time is not a valid time show an error
            if int(timer[-2])>5:
                self.updateDisplay("Error")
            #Else set as timer
            else:
                self.timer=timer
                self.originalTimer=timer#backup of timer value so main timer value can be edited
                self.updateDisplay("Set: "+self.timer)
            
            self.setTimerScreen=False# stop user from further editing timer

    def timerPause(self):
        '''
        Function which pauses the timer
        Stops by preventing timerRun form running
        '''
        self.timerComplete=True#By setting this to True the timer is paused until it is resumed

    def timerRun(self):
        '''
        Function which starts the timer
        '''
        if self.setTimerScreen==False and self.timerComplete==False:#If the user has set a time into the timer
            self.timerComplete=False#Allows the timer to be decremented every second when set to False
            
            #If the timer is 00:00 it is finished and it is stopped and shows a completion message
            if self.timer=="00:00":
                self.timerComplete=True#Stop timer from ticking down
                self.timerFinished()

            newMinute =int(self.timer[0:2])#Get the minutes left on the timer

            # If the minute is 0 set it to string 00 to accommodate for 0 lost during conversion
            if newMinute==0:
                newMinute="00"

            newSecond=int(self.timer[-2:])-1#Get the seconds left on the timer and subtract a second

            # If the seconds become a negative number take away a minute from the minute counter and update seconds to 59
            if newSecond<0 and self.timerComplete==False:
                newSecond=59
                newMinute-=1

            # If seconds are less than 10 add back in the string 0 for formatting
            if newSecond<10:
                newSecond="0"+str(newSecond)

            self.updateDisplay(str(newMinute)+":"+str(newSecond)) #Update the display with the new timer values
            self.timer=str(newMinute)+":"+str(newSecond)#Update the timer variable

            # While the timer has still time to tick down keep updating the timer
            if self.timerComplete==False:
                self.clockWindow.after(1000,self.timerRun)

    def timerReset(self):
        '''
        Function which resets the timer
        '''
        self.setTimerScreen=True# Make timer ready to run
        self.timerComplete=True#Stop timer from decreasing
        self.updateDisplay(self.originalTimer)#Place original time back on the screen ready to be ran

    def timerFinished(self):
        '''
        Displays message that timer is complete
        '''
        self.updateDisplay("Timer Finished")#Display message

    def updateDisplay(self,newDisplay:str):
        '''
        Updates display and locks textbox so it cant be edited directly by the user
        '''
        self.mainDisplay.config(state="normal")#Allows display to be updated
        self.mainDisplay.delete(1.0,"end")#Delete what was in display
        self.mainDisplay.insert(1.0,newDisplay)#Place new message in display
        self.mainDisplay.config(state="disabled")#Stops display from being updated


# Run the program
C=Clock()
