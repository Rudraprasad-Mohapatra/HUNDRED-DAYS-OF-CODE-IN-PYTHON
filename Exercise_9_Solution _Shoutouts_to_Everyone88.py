import win32com.client

names = ["Rahul","Rohan","Rohit","Rudraprasad","Rama"]
speaker = win32com.client.Dispatch("SAPI.SpVoice")
for name in names:
    speaker.speak(f"Shout out to {name}")