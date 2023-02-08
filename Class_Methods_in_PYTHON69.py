class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    def changeCompany(cls, newCompany):#you can give any name inplace of cls .First argument is generally understood as the  object like self and second argument is the parameter and so on.
        cls.company = newCompany #it will change the company for the object

    #if you want ot change the company for whole class then use the decorator @classmethod
    @classmethod
    def CHANGECOMPANY(cls,newCompany):
        cls.company=newCompany    


e1=Employee()
e1.name="Harry"
e1.show()
print(Employee.company) #class comapny is apple now
e1.changeCompany("Tesla")
e1.show()   
print(Employee.company)#class company is apple but e1's company is Tesla

e1.CHANGECOMPANY("tesla")
print(Employee.company)#class company is tesla now
e1.show()