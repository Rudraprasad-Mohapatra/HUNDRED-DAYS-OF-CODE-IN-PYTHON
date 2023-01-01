#When control can't enter inside the for loop then it enters the else block associated with the for loop.
#Always remember else means the end of loop(i.e. last value of 'i' has proessed successfully without interrruption),then only else will run after the complete execution of while/for loop,If any interrupt like break arrises then 'else' will not run.
for i in range(5):
    print(i)
else:
    print("Sorry,Your control can't enter in for loop")  

  
for i in range(5):
    print(i)
    if(i==3):
     continue #it will not affect to loop
    """if(i==4):
     break  """  #Due to i==4,loop will break and control goes out of loop and loop can't execute completely,So that else will not run for this,and viceversa for continue.
else:
    print("Sorry,no!")   

# else with While loop
i=5
while(i<10):
    """ if(i==6):
     break """
    if(i==9):
     print(i)
     i+=1
     continue
    print(i,end=" ")
    i+=1
else:
    print("Your loop has start with value i=5 end with value i=9") 

# format()
for x in range(10):
    print("This iteration-{} in for-loop".format(x+1)) #using string.format()
    print(f"This iteration-{x+1} in for-loop") #using f-string
else:
    print("I am else block!")   
print("Out of moh-maya like for-loop and else")     