print("Hey I am agood Boy \nYou are also a good Boy");#\n is an escape sequence Character (backslash+character)
# print("Hey I am a "very good" Boy");#Error arrises due to  the presence of "" inside "" we can achieve "" inside "" by adding escape sequence
print("Hey I am a \"very good\" Boy");
# or
print('Hey I am a "very good" Boy');

''' Multi Line comment'''
""" Multi Line comment """

#Inside print() arguments are optional
print ("hey",6,7,sep="~");# Use sep="character" for separating multiple statements with a separator(any character you want) inside a print statement
print ("hey",6,7,sep="~",end="009");
print("Hii");
#end determines what should be at the end of print statement
#By default end is \n
print ("hey",6,7,sep="~",end="009\n");
print("Hii");