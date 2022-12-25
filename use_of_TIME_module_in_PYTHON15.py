import time
# print(time.gmtime(0))#prints the epoch time 1jan 1970 as parameter is '0' else give time in seconds for getting reult (try: "print(time.gmtime(time.time()))" ) 
# curr=time.time()#time.time() methods return the    current time in seconds since epoch. It returns a  floating-point number.
# print(curr) 
# print("Current Time=",time.ctime(curr)) # time.ctime(time_in_second)function returns a 24 character time string but takes seconds as argument and computes time till mentioned seconds. If no argument is passed, time is calculated till the present.

# """for i in range(4):
#     time.sleep(1)  # using sleep(sec) to halt execution
#     print(i) """
# print()
# obj=time.localtime()    
# print(obj)
# print()
# obj1=1671936914.8473573
# print(time.gmtime(obj1))
# print()
# print(time.gmtime(time.time()))


# time.strftime() :-
# time.strftime() function converts a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument. If t is not provided, the current time as returned by localtime() is used. The format must be a string. ValueError is raised if any field in t is outside of the allowed range.
# from time import strftime,gmtime,localtime
# s=strftime("%a,%d/%b/%Y %H:%M:%S",gmtime(1671937070.2903538))
# print(s)
# s=type(strftime("%a,%d %b %Y %H:%M:%S",localtime()))
# print(s)
# s=strftime("%a,%d %b %Y %H:%M:%S",localtime())
# print(s)

# obj = time.gmtime(1627987508.6496193)
 
# Convert the time.struct_time
# object to a string of the
# form 'Day Mon Date Hour:Min:Sec Year'
# using time.asctime() method
# time_str = time.asctime(time.gmtime(1627987508.6496193))
# print(time_str)
# time_str = time.asctime(time.localtime(time.time()))
# print(time_str)


string = "Tue, 03 Aug 2021 13:45:08"
obj = time.strptime(string, "%a, %d %b %Y %H:%M:%S")
 
print(obj)

timestamp = time.strftime('%A %H:%M:%S',time.gmtime(1627987508.6496193))
print(timestamp)
timestamp = time.strftime('%A %H:%M:%S')
print(timestamp)
hour= int(time.strftime('%H'))
print(hour)
month= int(time.strftime('%M'))
print(month)
second = int(time.strftime('%S'))
print(second)

if((hour<12) and (second<60)) :
    print("Good Morning.")
 