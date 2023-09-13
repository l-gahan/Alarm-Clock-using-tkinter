import tkinter
import datetime

class Clock():
    '''
    Clock class when run displays an alarm clock on a tkinter window
    '''
    def __init__(self) -> None:
        '''
        Initialise and create clock window and buttons
        '''
        self.__AmPm=False
        self.__clockWindow = tkinter.Tk() # Create window for alarm clock 
        self.__clockWindow.title("Alarm Clock") #Set window title
        self.__clockWindow.resizable(False,False)# Set window dimensions to be fixed
        self.__clockWindow.configure(bg="grey")#Set background color
        
        self.__onDisplayScreen=False#Set to true if on the time display screen
        self.__setAlarmScreen=False #Set to true if user on screen where you can set alarm
        self.__setTimerScreen=False #Set to true if user on screen where you can set timer

        self.__buttonColor="lightgreen"#set button color

        self.__alarm="00:00"#Alarm display
        self.__timer="00:00"#Timer display
        self.__originalTimer="00:00"#Placeholder to keep users original timer value
        self.__timerComplete=False#The timer can only run if this variable is false

        self.__alarmMessage=False#Variable to change message shown when alarm is activated to indicate urgency
        self.__timerMessage=False#Variable to change message shown when timer is activated to indicate urgency

        self.__alarmSet=False #Set to true if an alarm has been set by the user to go off at a specific time
        self.__timerReady=False#Set to true if user has inputted a time they want to count down from

        # Create a display to show the time/timer/date etc and display the time on it
        self.__mainDisplay=tkinter.Entry(self.__clockWindow, font=("Arial", 22), width=40,justify="center")
        self.__mainDisplay.grid(padx=15,pady=15,columnspan=8)
        self.__displayTime() #Display the time on the screen

        #Create buttons on the window to control the alarm clock
        #Button to display the date
        self.__showDate=tkinter.Button(self.__clockWindow,text="Display Date", font=("Calabri", 15),command=self.__displayDate,relief="raised",bg="blue")
        self.__showDate.grid(row=2,column=1,columnspan=6,sticky="nsew",pady=5)
        #Button to display the time
        self.__showTime=tkinter.Button(self.__clockWindow,text="Display Time", font=("Calabri", 15),command=self.__displayTime,relief="raised",bg="blue")
        self.__showTime.grid(row=7,column=1,columnspan=6,sticky="nsew",pady=5)
        #Button to change the time from 24hr time to 12hr time
        self.__setAmPm=tkinter.Button(self.__clockWindow,text="Set AM/PM", font=("Calabri", 15),command=self.__setTimeType,relief="raised",bg="yellow")
        self.__setAmPm.grid(row=4,column=6,sticky="nsew")
        #Button to go to the screen to set an alarm (also used to set the alarm on the alarm screen)
        self.__setAlarmClock=tkinter.Button(self.__clockWindow,text="Set Alarm", font=("Calabri", 15),command=self.__setAlarm,relief="raised",bg="orange")
        self.__setAlarmClock.grid(row=5,column=4,sticky="nsew")
        #Button to allow user to input 0
        self.__setZero=tkinter.Button(self.__clockWindow,text="0", font=("Calabri", 15),command=self.__inputZero,relief="raised",bg=self.__buttonColor)
        self.__setZero.grid(row=6,column=2,sticky="nsew")
        #Button to allow user to input 1
        self.__setOne=tkinter.Button(self.__clockWindow,text="1", font=("Calabri", 15),command=self.__inputOne,relief="raised",bg=self.__buttonColor)
        self.__setOne.grid(row=3,column=1,sticky="nsew")
        #Button to allow user to input 2
        self.__setTwo=tkinter.Button(self.__clockWindow,text="2", font=("Calabri", 15),command=self.__inputTwo,relief="raised",bg=self.__buttonColor)
        self.__setTwo.grid(row=3,column=2,sticky="nsew")
        #Button to allow user to input 3
        self.__setThree=tkinter.Button(self.__clockWindow,text="3", font=("Calabri", 15),command=self.__inputThree,relief="raised",bg=self.__buttonColor)
        self.__setThree.grid(row=3,column=3,sticky="nsew")
        #Button to allow user to input 4
        self.__setFour=tkinter.Button(self.__clockWindow,text="4", font=("Calabri", 15),command=self.__inputFour,relief="raised",bg=self.__buttonColor)
        self.__setFour.grid(row=4,column=1,sticky="nsew")
        #Button to allow user to input 5
        self.__setFive=tkinter.Button(self.__clockWindow,text="5", font=("Calabri", 15),command=self.__inputFive,relief="raised",bg=self.__buttonColor)
        self.__setFive.grid(row=4,column=2,sticky="nsew")
        #Button to allow user to input 6
        self.__setSix=tkinter.Button(self.__clockWindow,text="6", font=("Calabri", 15),command=self.__inputSix,relief="raised",bg=self.__buttonColor)
        self.__setSix.grid(row=4,column=3,sticky="nsew")
        #Button to allow user to input 7
        self.__setSeven=tkinter.Button(self.__clockWindow,text="7", font=("Calabri", 15),command=self.__inputSeven,relief="raised",bg=self.__buttonColor)
        self.__setSeven.grid(row=5,column=1,sticky="nsew")
        #Button to allow user to input 8
        self.__setEight=tkinter.Button(self.__clockWindow,text="8", font=("Calabri", 15),command=self.__inputEight,relief="raised",bg=self.__buttonColor)
        self.__setEight.grid(row=5,column=2,sticky="nsew")
        #Button to allow user to input 9
        self.__setNine=tkinter.Button(self.__clockWindow,text="9", font=("Calabri", 15),command=self.__inputNine,relief="raised",bg=self.__buttonColor)
        self.__setNine.grid(row=5,column=3,sticky="nsew")
        #Allows user to cancel alarm
        self.__Reset=tkinter.Button(self.__clockWindow,text="Reset Alarm", font=("Calabri", 15),command=self.__resetAlarm,relief="raised",bg="orange")
        self.__Reset.grid(row=5,column=5,sticky="nsew")
        #When clicked shows the time the alarm is set for in 24hr time
        self.__showAlarmTime=tkinter.Button(self.__clockWindow,text="Show Alarm", font=("Calabri", 15),command=self.__showAlarm,relief="raised",bg="orange")
        self.__showAlarmTime.grid(row=5,column=6,sticky="nsew")
        #Allows user to snooze alarm for 25 minutes
        self.__snoozeButton=tkinter.Button(self.__clockWindow,text="Snooze", font=("Calabri", 15),command=self.__snooze,relief="raised",bg="red")
        self.__snoozeButton.grid(row=6,column=4, columnspan=3,sticky="nsew")
        #Allows user to set the timer
        self.__setTimer=tkinter.Button(self.__clockWindow,text="Set Timer", font=("Calabri", 15),command=self.__timerSet,relief="raised",bg="lightblue")
        self.__setTimer.grid(row=3,column=4,sticky="nsew")
        #Allows user to pause the timer
        self.__pauseTimer=tkinter.Button(self.__clockWindow,text="Pause timer", font=("Calabri", 15),command=self.__timerPause,relief="raised",bg="lightblue")
        self.__pauseTimer.grid(row=3,column=5,sticky="nsew")
        #Allows user to reset the timer
        self.__resetTimer=tkinter.Button(self.__clockWindow,text="Reset Timer", font=("Calabri", 15),command=self.__timerReset,relief="raised",bg="lightblue")
        self.__resetTimer.grid(row=3,column=6,sticky="nsew")
        #Allows user to start the timer
        self.__runTimer=tkinter.Button(self.__clockWindow,text="Start Timer", font=("Calabri", 15),command=self.__timerRun,relief="raised",bg="lightblue")
        self.__runTimer.grid(row=4,column=4,sticky="nsew",columnspan=2)
        # Two functionless buttons for display only
        self.__blankButton1=tkinter.Button(self.__clockWindow,state="disabled",relief="groove",bg="lightgrey")
        self.__blankButton1.grid(row=6,column=3,sticky="nsew")
        self.__blankButton2=tkinter.Button(self.__clockWindow,state="disabled",relief="groove",bg="lightgrey")
        self.__blankButton2.grid(row=6,column=1,sticky="nsew")

        
        self.__clockWindow.mainloop()# Run the window
    def __displayDate(self):
        '''
        Displays the current date on the display panel
        '''    
        self.__onDisplayScreen=False#Set variable to indicate we have changed screens
        self.__setAlarmScreen=False#Set variable to indicate we have changed screens
        self.__setTimerScreen=False#Set variable to indicate we have changed screens

        self.__updateDisplay(datetime.datetime.now().strftime("%B %d-%m-%y"))

    def __displayTime(self):
        '''
        Displays the current time on the display panel and can display the alarm if set
        '''
        self.__setAlarmScreen=False#Set variable to indicate we have changed screens
        self.__setTimerScreen=False#Set variable to indicate we have changed screens

        symbolAmPm=""#Variable to display am/pm if user requires it
        self.__onDisplayScreen=True#Variable to allow time to update but ONLY when in this screen
        hr=datetime.datetime.now().hour#Get the current hour
        minute=datetime.datetime.now().minute#Get the current minute
        #If the alarm is set and it is time for it to do so display the alarm message
        if ((str(hr)+":"+str(minute)==self.__alarm) or int(self.__alarm[0:2]) <hr or (int(self.__alarm[0:2]) ==hr and int(self.__alarm[-2:])<=minute))and self.__alarmSet==True:
            self.__displayAlarm()
        
        #If the user has selected it convert the current time from 24 hour time to 12 hour time and update the variable to the correct suffix
        if self.__AmPm==True:
            if hr >12:
                symbolAmPm="PM"
                hr=hr-12
            else:
                symbolAmPm="AM"

        nextMinute=(60-datetime.datetime.now().second)*1000#calculate how many seconds until the next minute on the clock

        #if the minute on display is less than 10 add an extra 0 to the display so that 0 is not erased when converting the minute to a string
        if minute<10:
            self.__updateDisplay(str(hr)+":0"+str(minute)+" "+symbolAmPm)
        else:
            self.__updateDisplay(str(hr)+":"+str(minute)+" "+symbolAmPm)
        
        #\If the user is still on this screen update the time when it is appropriate
        if self.__onDisplayScreen==True:
            self.__clockWindow.after(nextMinute,self.__displayTime)

    def __displayAlarm(self):
        '''
        Displays Alarm when time is reached
        '''
        self.__onDisplayScreen=False#Set variable to indicate we have changed screens
        self.__setTimerScreen=False#Set variable to indicate we have changed screens

        #When called change message every time it loops until alarm is canceled
        if self.__alarmMessage==False:
            self.__updateDisplay("-----")
            self.__alarmMessage=True
        else:        
            self.__alarmMessage=False
            self.__updateDisplay("Alarm")
        #While alarm is set loop again and change message
        if self.__alarmSet==True:
            self.__clockWindow.after(1000,self.__displayAlarm)

    def __setAlarm(self):
        '''
        Sets the alarm time (in 24 hour time) by user inputting numbers one by one (scrolling left to right)
        '''
        self.__onDisplayScreen=False#Set variable to indicate we have changed screens
        self.__setTimerScreen=False#Set variable to indicate we have changed screens

        #Set variable to true to allow users to edit alarm if users just entered this screen
        if self.__setAlarmScreen==False:
            self.__setAlarmScreen=True
            self.__updateDisplay("00:00")#set to 00:00 as a common starting point

        #else the user was already on the screen and now wishes to set the inputted time as their alarm
        else:
            alarm=self.__mainDisplay.get()
            #If inputted time isn't a viable time display an error
            if int(alarm[0:2])>23 or int(alarm[-2])>5:
                self.__updateDisplay("Error")

            #else set the alarm and update variables as appropriate
            else:
                self.__alarm=alarm
                self.__alarmSet=True
                self.__updateDisplay("Alarm Set")

            self.__setAlarmScreen=False#stop users being able to change the screen

    def __snooze(self):
        '''
        "Snoozes" the alarm and adds an extra 25 minutes before the alarm goes off again 
        '''
        self.__onDisplayScreen=False#Set variable to indicate we have changed screens
        self.__setTimerScreen=False#Set variable to indicate we have changed screens
        
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

        self.__alarm=str(hr)+":"+minute#Update the new alarm time
        self.__showAlarm()#Display the new alarm time to the user
        
    def __setTimeType(self):
        '''
        Allows user to switch the clock display from 24 hour time to 12 hour time
        '''
        #Set the AmPm variable to true or false each time the user presses the button to indicate which time type they want
        if self.__AmPm==False:
            self.__AmPm=True
        else:
            self.__AmPm=False
        
        self.__displayTime()#Display the new time

    def __inputNumber(self,number:int):
        '''
        helper function to help input numbers into the alarm or timer screen 
        '''
        #Get the time currently displayed and shift all the numbers one position to the left
        #In doing so the first digit will be removed and place the users inputted digit into the last place of the number
        #Eg. 12:34 with the user inputting 5 would become 23:45
        if self.__setAlarmScreen==True or self.__setTimerScreen==True:

            curSetTime=self.__mainDisplay.get()#get the displayed number
            curSetTime=curSetTime[0:2]+curSetTime[3:]#remove the ":"
            # curSetTime=curSetTime[:-1]#remove \n as .get() includes a \n at the last position of the number
            curSetTime=curSetTime[1:3]+":"+curSetTime[3:]#reassemble the number with the first and last digits removed
            curSetTime=curSetTime+str(number)#add the new digit

            self.__updateDisplay(curSetTime)#Update the time displayed

    def __inputZero(self):
        '''
        Helper function to set alarm and timer (Inputs 0)
        '''
        self.__inputNumber(0)
    
    def __inputOne(self):
        '''
        Helper function to set alarm and timer (Inputs 1)
        '''
        self.__inputNumber(1)
    
    def __inputTwo(self):
        '''
        Helper function to set alarm and timer (Inputs 2)
        '''
        self.__inputNumber(2)
    
    def __inputThree(self):
        '''
        Helper function to set alarm and timer (Inputs 3)
        '''
        self.__inputNumber(3)
    
    def __inputFour(self):
        '''
        Helper function to set alarm and timer (Inputs 4)
        '''
        self.__inputNumber(4)
    
    def __inputFive(self):
        '''
        Helper function to set alarm and timer (Inputs 5)
        '''
        self.__inputNumber(5)
    
    def __inputSix(self):
        '''
        Helper function to set alarm and timer (Inputs 6)
        '''
        self.__inputNumber(6)
    
    def __inputSeven(self):
        '''
        Helper function to set alarm and timer (Inputs 6)
        '''
        self.__inputNumber(7)
    
    def __inputEight(self):
        '''
        Helper function to set alarm and timer (Inputs 8)
        '''
        self.__inputNumber(8)
    
    def __inputNine(self):
        '''
        Helper function to set alarm and timer (Inputs 9)
        '''
        self.__inputNumber(9)
    
    def __showAlarm(self):
        '''
        Function which shows in the display what time the alarm is set for
        '''
        self.__onDisplayScreen=False#Set variable to indicate we have changed screens
        self.__setAlarmScreen=False#Set variable to indicate we have changed screens
        self.__setTimerScreen=False#Set variable to indicate we have changed screens
        
        #If alarm is set show the user the alarm else show an error message
        if self.__alarmSet==True:
            self.__updateDisplay(self.__alarm)
        else:
            self.__updateDisplay("Alarm not Set")
    
    def __resetAlarm(self):
        '''
        Function which turns off the alarm
        '''
        self.__onDisplayScreen=False#Set variable to indicate we have changed screens
        
        # If the alarm is set reset its variables and display message saying it has been reset
        if self.__alarmSet==True:
            self.__alarm="00:00"#set alarm back to placeholder
            self.__alarmSet=False
            self.__updateDisplay("Alarm Off")

        #Else show a message that no alarm is set
        else:
            self.__updateDisplay("Alarm not Set")
    
    def __timerSet(self):
        '''
        Function which sets the timer
        '''
        self.__onDisplayScreen=False#Set variable to indicate we have changed screens
        self.__setAlarmScreen=False#Set variable to indicate we have changed screens
        
        # If user wasnt already on the screen update variable so they can edit and show placeholder
        if self.__setTimerScreen==False:
            self.__setTimerScreen=True
            self.__updateDisplay("00:00")
        else:
            timer=self.__mainDisplay.get()#Get the inputted time and remove \n

            # If time is not a valid time show an error
            if int(timer[-2])>5 or timer=="00:00":
                self.__updateDisplay("Error")
            #Else set as timer
            else:
                self.__timer=timer
                self.__originalTimer=timer#backup of timer value so main timer value can be edited
                self.__updateDisplay("Set: "+self.__timer)
            
            self.__setTimerScreen=False# Stop user from further editing timer
            self.__timerComplete=False# Set timer to be ready to run

    def __timerPause(self):
        '''
        Function which pauses the timer
        Stops by preventing timerRun from running
        '''
        self.__timerComplete=True#By setting this to True the timer is paused until it is resumed

    def __timerRun(self):
        '''
        Function which starts the timer
        '''
        if self.__setTimerScreen==False and self.__timerComplete==False and self.__timer!="00:00" :#If the user has set a time into the timer
            self.__timerComplete=False#Allows the timer to be decremented every second when set to False
            

            newMinute =int(self.__timer[0:2])#Get the minutes left on the timer

            # If the minute is 0 set it to string 00 to accommodate for 0 lost during conversion
            if newMinute==0:
                newMinute="00"

            newSecond=int(self.__timer[-2:])-1#Get the seconds left on the timer and subtract a second

            # If the seconds become a negative number take away a minute from the minute counter and update seconds to 59
            if newSecond<0 and self.__timerComplete==False:
                newSecond=59
                newMinute-=1

            # If seconds are less than 10 add back in the string 0 for formatting
            if newSecond<10:
                newSecond="0"+str(newSecond)

            self.__updateDisplay(str(newMinute)+":"+str(newSecond)) #Update the display with the new timer values
            self.__timer=str(newMinute)+":"+str(newSecond)#Update the timer variable

            #If the timer is 00:00 it is finished and it is stopped and shows a completion message
            if self.__timer=="00:00":
                self.__timerComplete=True#Stop timer from ticking down
                self.__timerFinished()
            # While the timer has still time to tick down keep updating the timer
            if self.__timerComplete==False:
                self.__clockWindow.after(1000,self.__timerRun)

    def __timerReset(self):
        '''
        Function which resets the timer
        '''
        self.__onDisplayScreen=False#Set variable to indicate we have changed screens
        self.__setTimerScreen=True# Make timer ready to run
        self.__timerComplete=True#Stop timer from decreasing
        self.__updateDisplay(self.__originalTimer)#Place original time back on the screen ready to be ran

    def __timerFinished(self):
        '''
        Displays message that timer is complete
        '''
        self.__updateDisplay("Timer Finished")#Display message

    def __updateDisplay(self,newDisplay:str):
        '''
        Updates display and locks textbox so it cant be edited directly by the user
        '''
        self.__mainDisplay.config(state="normal")#Allows display to be updated
        self.__mainDisplay.delete(0,"end")#Delete what was in display
        self.__mainDisplay.insert(0,newDisplay)#Place new message in display
        self.__mainDisplay.config(state="disabled",disabledforeground="black",disabledbackground="white")#Stops display from being updated


# Run the program
C=Clock()
