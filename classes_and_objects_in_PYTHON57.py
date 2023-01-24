class person:
    name="Harry"
    occupation="Software Developer"
    networth=10
    def info(self):#self means the object for which the function has calld 
        print(f"{self.name} is a {self.occupation}")

a=person()
a.name="Subham"
a.occupation="Accountant"
print(a.name,a.occupation) 
a.info()   
b=person()
b.name="Nitika"
b.occupation="Software Developer"
b.networth=1000
b.info()
c=person()
print(c.name) #Harry
c.info()









"""
Python Class and Objects
A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

Creating a Class:
Let us now create a class using the class keyword.

class Details:
    name = "Rohan"
    age = 20
Creating an Object:
Object is the instance of the class used to access the properties of the class Now lets create an object of the class.

Example:
obj1 = Details()
Now we can print values:

Example:
class Details:
    name = "Rohan"
    age = 20

obj1 = Details()
print(obj1.name)
print(obj1.age)
Output:
Rohan
20
"""