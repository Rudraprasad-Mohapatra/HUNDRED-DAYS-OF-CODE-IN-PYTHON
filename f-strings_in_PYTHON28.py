# String format mechanism
letter="Hey my name is {} and I am from {}"
country="India"
name="Harry"

print(letter.format(name,country)) #1.Hey my name is Harry and I am from India
print(letter.format(country,name)) #2.Hey my name is India and I am from Harry
# so to fix the type of error we use indx inside {}
letter="Hey my name is {0} and I am from {1}"
country="India"
name="Harry"
print(letter.format(name,country)) #print(letter.format(0,1))

# Now if we increase the letter characters and parameters in letter.format(parameters) then it will be difficult to implement So we use "f-string" to overcome this,i.e start your string with letter "f" so that interpreter will understand that this is a "f-string"
word=f"Hii My name is {name} and I am from {country}" #python will understand  word as f-string
print(word)

# if we want to print the word string as it is i.e. nothing will be replaed at {name},{country}
word=f"Hii My name is {{name}} and I am from {{country}}"
print(word) #o/p is:- Hii My name is {name} and I am from {country}


# Without f-string
txt="For only {price:.2f} dollars!"
print(txt.format(price=49.078654432))  

# Using f-string
price=49.078654432
txt=f"For only {2*price:.2f} dollars!"
print(type(txt),txt)  