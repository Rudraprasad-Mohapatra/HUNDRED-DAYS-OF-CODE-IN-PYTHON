# tuple can't be changed
#other functions are same as list
tup=(1,5,6)
print(len(tup))
print(type(tup),tup) #<class 'tuple'> (1, 5, 6)
tup=(1,5)
print(type(tup),tup)#<class 'tuple'> (1, 5)
tup=(1) # compler will confuse for only one element, so better to use "," after a single number or character to represent as tuple
print(type(tup),tup)#<class 'int'> 1
tup=(1,)
print(type(tup),tup)#<class 'tuple'> (1,)

if 342 in tup:
    print("yes")
else:
    print("No")
# Here we can do slicing also but here original tuple will not change it will return a new tuple 
tup=(1,2,3,4,5,6,7,8,9)
tup2=tup[1:7:2]
print(tup2)
print(tup[2:4])
