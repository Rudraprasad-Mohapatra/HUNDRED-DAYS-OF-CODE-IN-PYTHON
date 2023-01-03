# finally clause
# try:
#     l={1,5,6,7}
#     i=int(input("Enter the index: "))
#     print(l[i])
# except:
#     print("Some Error Occurred")

# finally:
#     print("I am always Executed")

def func1(a):
    try:
        l = {1, 5, 6, 7}
        i = a
        print(l[i])
        return 1

    except:
        print("Some Error Occurred")
        return 0

    finally:
        print("I am always Executed") #due to the use of finally the function will not terminate after return 

x=func1(3)
print(x)