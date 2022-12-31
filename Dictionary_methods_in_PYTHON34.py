# set is unordered and dictionary is ordered
ep1={123:45,123:89,567:69,678:69}
ep2={222:67,566:90}
ep1.update(ep2)
print(ep1)
ep1.clear()
print(ep1)
# create empty dictionary
empty_dictionary={}
print(empty_dictionary,type(empty_dictionary))
ep1={123:89,567:69,678:69}
ep1.pop(123)
print(ep1)
# ep1.pop(123) #KeyError: 123
# delete a dictionary by "del dictionary_name"
# del ep1
# print(ep1)
del ep1[567] #will delete the key 567 and it's corresponding value
print(ep1)