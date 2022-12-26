# obj.index(val) raises value error if value is not present in list or tuple 
import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour=int(input("Enter hour: "))
print(hour)
if(hour>=0 and hour<12):
    print("Good Morning Bhai !")
elif(hour>=12 and hour<17):
    print("Good afternoon Bhai !")
elif(hour>=17 and hour<0):
    print("GoodNight sir")    


