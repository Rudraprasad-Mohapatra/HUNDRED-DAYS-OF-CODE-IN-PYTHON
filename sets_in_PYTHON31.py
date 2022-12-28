# Sets accepts and stores unique value only.No order is maintained like first 2 then 3 then 4 etc,So set is unorderd set of collections of data items.
#sets are unchangeable, like in the place of 2  we can't replace with 4 .
#Data items can't be accessed by index numbers.
s={2,4,2,6} # s is a set ,so it does not accept repated values here 2 repeats twice which will be considered as one.
# Here dict is a dictionary.Both set and dictionary starts with {}.
dict={
    "brand":"ford",
    "model":"Mustang",
    "year":1964
}

print(s,type(s))

info={1,"Hii","2","Wow"}
print(info)

# For in loop in set
for element in info:
    print(element)

#empty set
# harry={} #This is wrong and it's type is dictionary
harry=set() # It is the correct format of an Empty set
print(harry,type(harry))

