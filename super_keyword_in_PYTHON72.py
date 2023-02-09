"""
class ParentClass:
    def parent_method(self):
        print("This is the parent method in parent class")

class ChildClass(ParentClass): #ChildClass will inherit all the methods and properties of ParentClass
    # def parent_method(self): #whether this parent_method present or not in the child class if super key word is used is used then it will call the method of parent class
    #     print("This is the parent_method in child class")
    def child_method(self):
        print("This is the child Method")
        super().parent_method()

c=ChildClass()
c.child_method()
# let we don't have parent_method in ChildClass so if I call c.parent_method() it will call the parent_method() of parent class if present
c.parent_method()
"""


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
class Programmer(Employee):
    def __init__(self,name,id,lang):
    #     self.name=name
    #     self.id=id
        # We can replace the code from line-26 to line-27 by calling the constructor of parent class as in line-29
        super().__init__(name,id)
        self.lang=lang


Rohan=Employee("Rohan Das",420)
Harry=Programmer("Harry Das",420,"PYTHON")

print(Rohan.name)
"""
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)
"""

"""
NOTES:-

Super keyword in Python
The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.

Here's an example of how to use the super() keyword in a simple inheritance scenario:

class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
Output:
This is the child method.
This is the parent method.
In this example, we have a ParentClass with a parent_method and a ChildClass that inherits from ParentClass and overrides the child_method. When the child_method is called, it first prints "This is the child method." and then calls the parent_method using the super() keyword.

The super() keyword is also useful when a class inherits from multiple parent classes. In this case, you can specify the parent class from which you want to call the method.

Here's an example:

class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
Output:
This is the child method.
This is the parent method of ParentClass1.
In this example, the ChildClass inherits from both ParentClass1 and ParentClass2. The child_method calls the parent_method of the first parent class using the super() keyword.

In conclusion, the super() keyword is a useful tool in Python when you want to call a parent class method in a child class. It can be used in inheritance scenarios with a single parent class or multiple parent classes.
"""
