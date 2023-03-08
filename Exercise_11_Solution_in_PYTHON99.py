# Exercise 11 - DRINK WATER REMINDER
# Write a python program which reminds you of drinking water every hour or two.
# Your program can either beep or send desktop notifications
# For a specific operating system

import win32com.client
from plyer import notification
import time

# Creating The speak method


def Speak(messageText):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.speak(f"{messageText}")

# Creating the Take_break method that will create a pop-up notification for our windows

def takebreak():
    print("Do you want to start your work sir? (yes/no) ")
    Speak("Do you want to start your work sir?")
    question = input()

    if "yes" == question:
        print("Starting sir...")
        Speak("Starting sir")
    if "no" == question:
        print("We will automatically start after 5 mins sir.")
        Speak("We will automatically start after 5 mins sir.")
        time.sleep(0.2*60)
        print("Starting Sir...")
        Speak("Starting Sir")

    # A notification we will held that
    # Let's Start sir and with a message of
    # will tell you to take a break
    # after 1 hour for 10 seconds

    val = True
    while (True):
        if val == True:
            notification.notify(title="Let's Start sir",
                                message="will tell you to take a break and drink a glass of water after 1 hour.",
                                timeout=10)
            # For 1 hour there will be no notification but
            # after 1 hour a notification will popup
            print("Now User has started Working !!!")
            time.sleep(0.1*60)  
            print("1 hour later...")
            # e.g here we are doing for 6 sec. because 1 hour is a very long time so we can replace it by "3600" sec i.e 1 hour when we need 
        if val == False:
            Speak("Your 5 mins is over.")
        print("You have worked for 1 hour")
        Speak("You have worked for 1 hour")
        print("Please take a break and drink a glass of water ,Sir.")
        Speak("Please take a break and drink a glass of water ,Sir.")
        notification.notify(title="Break Notification",
                            message="Please do use your device after sometime as you have been continuously using it for 1 hour and it will affect your eyes",
                            timeout=10)
        time.sleep(0.1*60)
        if val == True:
            print("Do you want to snooze notification for 5 mins? (yes/exit) ")
            Speak("Do you want to snooze notification for 5 mins?")
            val=False
            choice = input()
            if (choice == "yes"):
                time.sleep(0.1*60)
            elif (choice == "exit"):
                Speak("Thank you Sir ! Have a great day !")
                break;    
        else:
            continue


# Driver's Code

if __name__ == "__main__":
    takebreak()
    # Speak("Hii")
