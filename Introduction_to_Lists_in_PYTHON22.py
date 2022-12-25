#List can be changed by using some functions but tupple can't be changed  
#list can store various types of same and different type of data
marks=[3,5,6]
print(marks)
print(type(marks))
for i in range(len(marks)):
    print (marks[i])
#count starts from '0' always
marks=[3,5,6,"Harry",0,'c']   
print(type(marks))
for i in range(len(marks)):
    print (marks[i])

print(marks[-3]) #which is equal with print(marks[len(marks)-3])

# check a item is present in list or not
if 6 in marks:
    print("yes")
else:
    print("no")  

if '6' in marks:
    print("yes")
else:
    print("no") 

if "Harry" in marks:
    print("yes")
else:
    print("no")  

if "rry" in "Harry":
    print("yes")
else:
    print("no")     

if "rary" in "Harry":
    print("yes")
else:
    print("no")     


print(marks[1:-1]) #print(marks[1:len(marks)-1])
print(marks[1:len(marks):2])
print(marks[1:]) #print(marks[1:len(marks)])
print(marks[:6]) #print(marks[0:6])


# list comprehension
lst=[i for i in range(4)]
print(lst)
lst=[i*i for i in range(4)]
print(lst)

# Writing complex comprehension code on list
lst=[i*i for i in range(10) if i%2==0] # it says store i*i fro, i=0 to 9 where i is completely divisible by 2
print(lst)