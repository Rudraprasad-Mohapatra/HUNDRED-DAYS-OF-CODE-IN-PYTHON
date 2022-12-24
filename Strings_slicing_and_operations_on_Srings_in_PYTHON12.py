names="Harry,Subham"
print(names[0:5])#It will print from 0 to n-1 i.e. 4
print(len(names))

print(names[0:4]) #Harr
print(names[1:4]) #arr
print(names[:4]) #Harr         ->automatically it replaces 0 before ":" as no index is mntioned
print(names[3:]) #ry,Subham    ->automatically it replaces len(names) after ":"

# negative slicing
print(names[2:-3]) # will print "rry,Sub" because python interprets it as print(names[2:len(names)-3])
print(names[2:len(names)-3]) 

print(names[-5:10]) # will print "ubh" because python interprets it as print(names[len(names)-5:10]) 
print(names[len(names)-5:10]) 

print(names[-10:-5]) # will print "rry,S" because python interprets it as print(names[len(names)-10:len(names)-5])
print(names[len(names)-10:len(names)-5])

# Quick Quiz
nm="Harry"
print(nm[-4:-2])
print(nm[(len(nm)-4):len(nm)-2])