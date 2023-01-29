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