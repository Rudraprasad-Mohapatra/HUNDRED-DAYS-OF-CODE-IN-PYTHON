# Implicit typecasting :-lower order datatype converts into higherorder datatype to prevent data loss.
# Explicit Typecasting are int(data),float(data),hex(data),oct(data),str(data)

# Taking user input in python
# We can take input directly by using input(),and this function returns a value as String or character hence we have to pass that value to a variable

a=input("Enter your name")
print("My name is",a);
x=input("Enter First Number ");
y=input("Second Number ");
print(int(x)+int(y))