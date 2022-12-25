for i in range(1,55):
    print(i,end=" ")
print()
i=4
while(i<15):
    print(i,end=" ")
    i+=1
i=14
while(i<15):
    if(i==0):
        print("BYE")
        exit()
    print(i,end=" ")
    i-=1

i=int(input("Enter anumber: "))
if(i>38):
        print("bye")
while(i<38):
    print("I am less than 38",end="^\n")
    i=int(input("Enter anumber: "))
    if(i>38):
        print("bye")
# There is no do-while loop in python        