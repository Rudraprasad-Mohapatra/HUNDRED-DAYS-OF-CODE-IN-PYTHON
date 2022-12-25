# This is like switch case statements
x=int(input("Enter the value of x "))
match x:
    case 0:
        print("I am",x)
    case 1:
        print("I am",x)    
    case 2:
        print("I am",x)    
    case 3:
        print("I am",x)    
    # case _:
    #     print("I am Default")    
    case _ if(x!=90): #After facing one case ,it will not go for other cases like other languages(c,cpp,java)
        print(x,"is not ninety!")
    case _ if(x!=80):
        print(x,"is not eighty!")   
