for i in range(12):
    if(i==10):
        continue
    if(i==11):
        break
    print("5 x ",i,"=",(5*(i))) 


# Emulate do-while loop
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break

