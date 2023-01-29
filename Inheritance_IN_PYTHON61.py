class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}.")

# Inheritance
class programmer(Employee):
    def showLanguage(self):
        print(f"The default language of {self.name} is python.")

e=Employee("Rohan Das",400)
e.showDetails()        
e1=Employee("Rohit Das",410)
e1.showDetails()    
# e1.showLanguage() # will give error    

# Inheritance
e3=programmer("Rupam",430)
e3.showDetails()
e3.showLanguage()

"""
NOTES:-

Inheritance in python
When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

Python Inheritance Syntax
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

Types of inheritance:
Single inheritance
Multiple inheritance
Multilevel inheritance
Hierarchical Inheritance
Hybrid Inheritance
We will see the explaination and example of each type of inheritance in the later tutorials



main.py
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default langauge is Python")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()

"""
