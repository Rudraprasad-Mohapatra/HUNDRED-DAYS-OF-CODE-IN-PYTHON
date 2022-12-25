l=[1,2,4,"Harry",6]
m=[10,21,3,4,56,34]
print(l)
l.append(7) # 7 is added at end of list
print(l)
s=["Ram","shyam","hari","gopal"]
print(s.sort()) #returns None
m.sort() #applied on same type data containing list
print("Printing in sorting order",m)
m.sort(reverse=True)
print("Printing in revrse sorting order",m)

# reverse()
print(l.reverse()) #just reverse the original list

# index()
print(l.index(1)) #due to reverse() 1 is at end

# count() count the no. of occurence of an item.
print(l.count(1))

# copy()
"""
m=[1,2,3,4]
k=m
k[0]=0
print(m) """ #if we do copy like this then here m value will also be changed because k=m,means k is arefernce to m i.e. same memory address both are using so change in any one will affect the same memory location
#instead of doing like above we can use copy() which will not change the original list lile above
m=[1,2,3,4]
k=m.copy()
k[0]=0
print(m)
print(k)

# insert()
m.insert(1,869)
print(m)

#extend()
l=[9,8,6,5]
l.extend(m) #m will be added at the end of l by which l will be changed permanently
print(l)

#concatenate(+) By using this the function we can conactenate two list without changing the original list
j=[1,2,3]
n=[3,6,7,8]
h=j+n
print(h)
print(j)
print(n)

