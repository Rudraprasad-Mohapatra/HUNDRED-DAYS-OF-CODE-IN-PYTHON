# Strings are immutable i.e. we can't change the string value at the variable where  it is stored,but we can apply some methods on it to get the desired result and can store it in another variable i.e. it does not change the value of original variable.

a="Harry"
print(len(a))
print(a.upper())
print(a.lower())

# rstrip()
b="!!!!HArryBhai !!!!!!!"
print(b.rstrip('!')) # it will print !!!!HArryBhai i.e it will only remove the "!" from end 
print(b.rstrip("!")) # it will print !!!!HArryBhai i.e it will only remove the "!" from end 

# replace()
ab="Harryarr,arr"
print(ab.replace("arr","0kl")) # will print H0kly
# string.replace( character, replacement, count)  #count signifies how many times you want to replace
ab=ab.replace('a','o',1)
print(ab)


# split()
# :-It coverts string into list ,string must contain " "
ab="H arr y arr, arr"
lis=ab.split()
print(lis,type(lis),lis[0])
abd="H,arr,y,arr,,arr"
liss=abd.split(',')
print(liss)

# capitalize() used to conver the first character of String to uppercase
blogHead="welcome to CodeWithHarry channel "
print(blogHead.capitalize()) #Answer will be "Welcome to codewithharry" it does the first letter of string to capital(If already capital then does not matter) and all converts all capital letter inside the string except first letter to lower case

# center(number_value)#It first counts the number of characters in String then it subtracts that value from number_value (let the result value is "result")and then add that no. of result "spaces" at the beginning of string to make the string comes at center  
print(blogHead)
print(len(blogHead))
print(blogHead.center(50)) #Output will be "        welcome to CodeWithHarry channel"
print(len(blogHead.center(50))) 

# count("String/partof string"):-It givs how many times a thing is coming inside a string
print(abd.count("arr"))
# endswith("String/partof string"):-
print(ab.endswith("arr"));#returns true or false
str1="Welcome to the console to to!!!"
print(str1.endswith("to",4,10))#It says wheteher the string whose index starts from the 4 to 9 ends with string "to" or not
# find():-it returns the index of first occurence of a string inside a String
print(str1.find("to"))      
print(str1.find("two"))#returns -1 if that word is not prsent in string

#index():-same as find() but when find() returns -1 ,it raises an error
# print(str1.index("two"))

# isalnum():-To check a string consists of alphanumeric characters(A-Z,a-z,0-9) or not we use it.
str1="WelcometotheconsoleASX123"
print(str1.isalnum())

# isalpha():-To check a string consists of alphabate characters(A-Z,a-z) or not we use it.
str1="WelcometotheconsoleASX"
print(str1.isalpha())

# islower():-To check a string consists of lower case characters(a-z) or not we use it.
str1="welcometotheconsole"
print(str1.islower())

# isupper():-To check a string consists of upper case characters(A-Z) or not we use it.
str1="WELCOMETOCODEWITHHARRY"
print(str1.isupper())

# isprintable():-if all characters are printable then it returns true else returns false
str3="Hey how are you\n"#As "\n" is not printable so it returns false
print(str3.isprintable())
str3="Hey how are you"
str3=str3+"hii"
# str3[0]='i'#strings are immutable
print(str3[0])
print(str3.isprintable())

# isspace():if stringf contains only space(created by space bar or tab bar not space charcter) returns true else returns false
str4="   "
print(str4.isspace())
str4="   Hii"
print(str4.isspace())

# istitle():=If all the words in line are starts with a capital word returns true
str3="Hey how are you"
str3.istitle()# false
str3="Hey How Are You"
str3.istitle() #true

#swpcase():-converts lowercase letters in a string to uppercase and viceversa
str3="Hey hOW aRE yOU"
print(str3.swapcase())

#title():-converts  starting letter of all words to capital letters irrespective of case
print(str3.title())

# Reverse the string "Hello World":

# txt = "Hello World"[::-1]
# print(txt)

# Create a slice that starts at the end of the string, and moves backwards.

# In this particular example, the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.
