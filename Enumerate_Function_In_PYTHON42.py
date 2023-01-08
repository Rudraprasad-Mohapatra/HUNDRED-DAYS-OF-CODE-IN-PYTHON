marks=[12,56,32,98,12,45,1,4]

# concept-1
# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Harry,Awesome")
#     index+=1    

# enumerate()
#  Enumerate() is an built in function which allows loop all over a sequence like list,tuple or string and get the index and elementValue at same time 
# marks=(2,5,6)
# for index,mark in enumerate(marks,start=1):
for index,mark in enumerate(marks,start=1): #By mentioning start=1 index will start from '1' instead of '0' i.e. 0th index element will be 1st index element.Index will be start from 1 no element value will change.
    print(index,mark,type (marks))
    if(index==3):
        print("Harry,awesome!")

