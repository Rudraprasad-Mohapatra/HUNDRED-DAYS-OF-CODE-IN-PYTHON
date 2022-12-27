#factorial(7)=7*6*5*4*3*2*1
#factorial(6)=5*4*3*2*1
#factorial(5)=5*4*3*2*1
#factorial(4)=4*3*2*1
#factorial(3)=3*2*1
#factorial(2)=2*1
#factorial(1)=1
#factorial(0)=1
"""
def factorial(n):
    if(n==0 or n==1):
     return 1
    return n*factorial(n-1)

print(factorial(5)) """

"""Fibonacci Series"""
def fibonacci(serialNum):
    if(serialNum==0):
        return 0
    elif(serialNum==1):
        return 1 
    return fibonacci(serialNum-2)+fibonacci(serialNum-1)   

for i in range(6):
    print(fibonacci(i),end=" ")    

# print(fibonacci(int(input("Enter the serial number "))))       