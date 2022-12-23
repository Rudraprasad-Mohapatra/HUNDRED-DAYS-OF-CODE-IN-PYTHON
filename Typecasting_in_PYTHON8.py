# Typecasting:Converting one datatype to another datatype done by PYTHON interpreter
a="1"
b="2"
print(a+b)#two strings are added
print(int(a)+int(b))#two strings after typecasting are added
# print(int("Harry")+int("Bhai")) #In above the strings are non other than numbers aren in string format but here "Harry" and "Bhai" both are actual collection of letters i.e. Strings so cant be typecasted
# Explicit Typecasting are int(data),float(data),hex(data),oct(data),str(data)
print(int(12345))
print(float("12345"))
print(hex(12345))
print(oct(12345))
print(str(12345))

# Implicit typecasting :-lower order datatype converts into higherorder datatype
c=1.2
d=2
print(c+d,type(c+d))