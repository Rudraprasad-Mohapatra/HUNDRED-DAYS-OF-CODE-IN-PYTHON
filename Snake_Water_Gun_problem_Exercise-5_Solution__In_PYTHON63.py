import random

def check(comp,user):
    if comp==user:
        return 0
    if comp==0 and user==1 :
        return -1
    if comp==1 and user==2 :
        return -1
    if comp==0 and user==2 :
        return -1
    if comp==2 and user==0 :
        return -1
    # For rest cases user will win 
    return 1

comp=random.randint(0,2)
user=int(input("0 for Snake,1 for water and 2 for Gun:- "))
if(user>2 or user<0): 
    print("Not a valid input.")
    exit()
print("You-",user)
print("Comp-",comp)
score=check(comp,user)
if score==0:
    print("Bhai ye toh Draw hogaya!")
if(score==1):
    print("Bhai Tu Jit Gaya")
else:
    print("Bhai Computer Jit Gaya")