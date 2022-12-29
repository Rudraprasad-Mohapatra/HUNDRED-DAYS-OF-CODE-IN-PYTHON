s1={1,2,5,6}
s2={3,6,7}
# union()
print(s1.union(s2)) #union of sets according to Venn diagram in sets

print(s1,s2)#we can observe that our s1 and s2 are remain untouched
# update()
s1.update(s2) #s1 is updated i.e. s1 brings the value from s2 those are not present in s1
print(s1,s2)
# intersection() and intersection_update()
print(s1.intersection(s2))# here s1={1, 2, 3, 5, 6, 7} ,s2={3, 6, 7} due to above operation
s1.intersection_update(s2)# here s1={1, 2, 3, 5, 6, 7} ,s2={3, 6, 7} due to intersection_update operation the result of intersection between s1 and s2 is stored in s1 i.e s1 is updated with only the intersection values and remaining values are removed
print(s1)

# differnce() and difference_update()
s1={1,2,3,4,5}
s2={4,5,6,7,8,9}
print(s1.difference(s2))
s2.difference_update(s1)
print(s2)

# disjoint():-No intersection element is there
print(s1.isdisjoint(s2))# Here s2={6, 7, 8, 9} and s1={1, 2, 3, 4, 5} so ans will be true

s1={1,2,3,4,5,6}
s2={1,2,3,4,5,6,7,8,9}
print(s2.issuperset(s1))#true
print(s1.issubset(s2))#true

# remove() raises error/discard() donot raises error
s1.remove(2)
print(s1)
s1.discard(1)#simply discards
print(s1)
s1.discard(7)#No error raises
print(s1)
s1.remove(3)#simply removes
# s1.remove(7)# raises an error

# pop()
item=s2.pop() # A random value from s2 will be popped out.
print(s2,item)
item=s2.pop() # A random value from s2 will be popped out.
print(s2,item)

# "del" keyword, it is used to delete a whole set
del s1
# print(s1)

# clear():It dos not delete the set but delete all the values inside it
s1={1,2,3,4,5,6,7,8,9}
s1.clear()
print(s1)#Now s1 is an empty set

# CHECK IF ITEM EXISTS
s1={"karla",1,2,3,4}
if "karla" in s1:
    print("Carla is present!")
else:
    print("Carla is not present!")

