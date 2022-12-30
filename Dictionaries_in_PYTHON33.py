# Afer PYTHON 3.7 onwards , Dictionaries are ordered collection of data items(i.e If we print the keys we will get the same order of keys everytime).They store multiple items in a single variable.dictionary iems are key-value pairs that are separated by comma and enclosed by {}
dic={
    "Harry":"Human Being",
    "Spoon":"Object",
    123:"Neha",
    456:"Shyama"
}
print(dic,type(dic))
print(dic[123])
print(dic["Harry"])#This method will raise error if the key value is not present in dictionary.(KeyError: 'Hary')
print(dic['Harry'])
# print(dic["Hary"])#Here we will get error as "hary" as a key value is not present in dictionary.
print(dic.get('Harry'))#This method will not raise error if the key value is not present in dictionary .
print(dic.get("Hary"))#Here we will not get error as "hary" as a key value is not present in dictionary.
print(dic[456])
print(dic["Spoon"])

# for loop in dictionary
for i in dic:
    print(i," : ",dic.get(i))

# print all keys
print(dic.keys())    #dict_keys(['Harry', 'Spoon', 123, 456])
print(dic.values())  #dict_values(['Human Being', 'Object', 'Neha', 'Shyama'])

# print all keys using for loop
for key in dic.keys():
    print(key)
# print all values using for loop
for value in dic.values():
    print(value)

# using "fstring" printing in a readable format
for key in dic.keys():
    print(f"The value corresponding to the key \"{key}\" is \"{dic[key]}\".")

#For printing key value pairs
print(dic.items())    #dict_items([('Harry', 'Human Being'), ('Spoon', 'Object'), (123, 'Neha'), (456, 'Shyama')])
 #iterating dictionary using dic.items() 
for key,value in dic.items():
    print(f"The value corresponding to the key \"{key}\" is \"{value}\".")

# e.g :- used for mrp of a product   