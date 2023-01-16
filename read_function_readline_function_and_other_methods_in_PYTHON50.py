# f=open('myfile3.txt','r')
# while True:
#     line=f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))  #When It get no lines it simply print() space of type string.
#         break
# f.close()


# with open('myfile4.txt', 'r') as p:
#     while (True):
#         line = p.readline()
#         if not line:
#             break
#         m1 = line.split(',')[0] #gives string
#         m2 = line.split(',')[1] #gives string
#         m3 = line.split(',')[2] #gives string
#         print(f"marks of student in 1st three subject is {m1},{m2},{m3}")
#         print(f"Average marks of student in 1st three subject is {(int(m1)+int(m2)+int(m3))/3}")


# f = open('myfile3.txt', 'r')

# line = f.readlines()
# print(line,end="") #output will be ['Harry Bhai Python course is great.\n', "Wow it's Amazing."]
# line = f.readline()
# print(line)


f=open('myfile5.txt','w')
lines=['line 1\n','line 2\n','line 3\n'] #list is provided
f.writelines(lines)
f.close()
# Note:-
"""
readlines() method
The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
The readlines() method reads all the lines of the file and returns them as a list of strings.

writelines() method
The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.

Here's an example of how to use the writelines() method:

f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.

Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:

f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()
It is also a good practice to close the file after you are done with it.
"""
