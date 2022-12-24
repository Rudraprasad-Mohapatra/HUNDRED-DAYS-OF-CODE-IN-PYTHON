'''a=int(input("Enter your age "))
print("Your age is ",a)
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
if(a<18):
    print("You cannot drive")
    print("You cannot drive as you are below",a)
else:
    print("You can drive")    
    print("You can drive as you are above",a) '''

"""appleprice=10
budget=200
if(budget-appleprice >50):
    print("Alexa Add 1 kg apples to the cart")
else:
    print("do not add apples to cart.") """   

# Nested if statments(if inside another if)
num=int(input("Enter the value of num: "))
if(num<0):
    print(num,"is negative.")
elif(num==0):
    print("Number is zero.")
else:
    print(num,"is possitive.")
    if(num<18):
     print(num,"is less than 18")
       
print("Tum kuch bhi karlo main print hoke rahunga")            
