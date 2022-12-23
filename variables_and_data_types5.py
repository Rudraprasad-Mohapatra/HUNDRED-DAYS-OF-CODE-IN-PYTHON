# in python Everything is object
#variables are stored in RAM
a=1;#Here command says store '1' in my main memory and give the address where you store to 'a'
print(a)
b="Harry"
print(b)
d=None
print(d)
# print(a+d)# will not work
print("The type of d is",type(a))
a1=1.12
print("The type of d is",type(a1))
# Complex Number
c=complex(8,2)
print(c,type(c))

# list:-It is list of Items which can store different types of data items
# List is mutable (changeable)
list1=[8,2.3,[4,-5],["apple","Bananana",'a']]
print(list1,type(list1))

# tupple :-It is list of Items which can store same types of data items
tupple1=(("parrot","Sparrow"),("Lion","Tiger"))
print(tupple1,type(tupple1))

# Mapped data:dict
dict1={"name":"sakshi","age":0,"canVote":True}
print(dict1,type(dict1))