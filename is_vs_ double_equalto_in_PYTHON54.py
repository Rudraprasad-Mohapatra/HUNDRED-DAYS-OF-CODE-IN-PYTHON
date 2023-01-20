a=4
b="4"
c=a
print(a is b) #compares exact location in memory
print(a is c) #compares exact location in memory and returns true when refers to same object
print(a==b) # compares value


#true for constants or immutable objects(tuple,etc.) python never allocate new memory it references the same memory and viceversa for mutable objects like list,,sets etc..
k=123
l=123
print(k is l) 
print(k == l) #true due to line-no.9
km="Hii"
lm="Hii"
print(km is lm) #true due to line-no.9
print(km == lm) #true

abc=(1,2,3)
deff=(1,2,3)
print(abc is deff)
print(abc == deff)

a=None
b=None
print(a==b)
print(a is b)





"""
'is' vs '==' in Python
In Python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that you should be aware of.

The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.

For example:

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
In this case, a and b are two separate lists that have the same values, so == returns True. However, a and b are not the same object in memory, so is returns False.

One important thing to note is that, in Python, strings and integers are immutable, which means that once they are created, their value cannot be changed. This means that, for strings and integers, is and == will always return the same result:

a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True
In these cases, a and b are both pointing to the same object in memory, so is and == both return True.

For mutable objects such as lists and dictionaries, is and == can behave differently. In general, you should use == when you want to compare the values of two objects, and use is when you want to check if two objects are the same object in memory.

I hope this helps clarify the difference between is and == in Python!
"""