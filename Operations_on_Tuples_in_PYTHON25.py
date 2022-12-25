#We can't change uple directly
countries=("spain","Italy","India","England","Germany")
temp=list(countries) #converting tuple to list
temp.append("Russia") #Add item
temp.pop(3) #remove item at perticular index
temp[2]="Finland" #change item
countries=tuple(temp) #converting list to tuple
print(countries)

#concatenation (do not change the existing tuple ,returns a new uple)
countries=("pakistan","Afghanistan","Bangladesh","Shrilanka")
countries2=("Vietnam","India","China")
resultant_country=countries+countries2
print(resultant_country)

# count() same as list

tuple1=(0,1,2,3,2,31,1,3,2,3)
# print(tuple1.count(399)) #raises error
print(tuple1.count(3))
print(tuple1.index(3)) #returns first index of 3
print(tuple1.index(3,4,8)) #returns first index of 3 between 4 to 8