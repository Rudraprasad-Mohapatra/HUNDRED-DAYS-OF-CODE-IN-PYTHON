#1
def average(a=9,b=1):
    print("The average is  ",(a+b)/2)
average(1,5) #3.0 Here order of arguments matters
average(b=9)
average(b=9,a=18)#order of arguments does not matter
average()   #5.0
average(3) #3 will be replaced at a
#2.Required Arguments
def average_of_three_numbers(num1,num2,num3=1): #Here during call of this function providing num3 value is optional but num1 and num2 is must
    print("The average is  ",(num1+num2+num3)/2)
    return(num1+num2+num3)/2
c=average_of_three_numbers(4,5,6)   
print(c) 
d=average_of_three_numbers(4,5)
print(d)  

#3.Variable length argument(as a list )

def average_num(*numbers): #numbers will be treated as a list i.e argument is like list
    print(type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    print("avergae is: ",sum/len(numbers))  
average_num(1,2,3)
average_num(1,2,3,4)
average_num(1,2,3,4,5)

#3.Variable length argument(as a dictionary)

def details(**names): #numbers will be treated as a dictionary i.e argument is like dictionary
    print(type(names))
    for i in names:
     print("Hello my name is",names[i],"and my home town is ",names["madd"],"and my friend name is ",names["mfriend"])  
details( mname="Harry",madd="Delhi",mfriend="Rohan")
details( mname="Harry1",madd="Delhi1",mfriend="Rohan1")


