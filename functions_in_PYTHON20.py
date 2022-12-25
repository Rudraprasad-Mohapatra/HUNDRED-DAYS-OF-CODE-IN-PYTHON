# two types of function 1.Built-in function 2.Userdefined function
def calculateGmean(a1,b1):
    gmean=(a1*b1)/(a1+b1)
    print(gmean)

def checking_Num(a,b):
    if(a>b):
        print(a,"is greater than",b)
    else:
        print(b,"is greater than",a)  

# def addTwoNumWithInput(a,b):  #Writing only this sigle line without dfinition will give error
# But let we want now interpreter should not give error and move forward and I will define it latter then we have to use "pass", So code will be:-
def addTwoNumWithInput(a,b):
    pass

    
a=9
b=8
calculateGmean(a,b)
checking_Num(a,b)