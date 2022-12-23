# Anything in python enclosed between "" or '' is called String

friend="Rohan"
anotherfield='lovish'
apple='He said,"Hii Harry" apple'
print(apple)
# apple1="He said,"Hii Harry"" #double quote inside double quote can't be applied use escape sequence or triple sigle quote
apple2='He said,\"Hii Harry\" apple2'
print(apple2)
apple3='''"He said,"Hii Harry" apple3"'''
print(apple3)

name="Harry"
# Strings are sequence of characters so according to index the character will print
print(name[0],name[1],name[2],name[3],name[4],sep='~') #For index 5it will give index out of range

# Looping Through the String
print("let us use a for loop  for printing name characters",end=":\n")
for character in name:
    print(character,end="~")