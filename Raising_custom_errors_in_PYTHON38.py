# In python we use raise keyword to raise errors
# a=int(input("Enter any value between 5 and 9 "))

# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")

# # Defining custom exceptions
# Exception ServerOffError
x = input("Bhai ek command toh dede jaise program running quit ho jaye aur jo lowercase letter main bhi ho: ")
if (x.islower()):
    if (x == 'quit'):
        print("Bhai apne toh sahi command diya !\nMain program band kar raha hoon! \nTa...Ta..")
    else:
        raise InterruptedError(
            "Wrong command! lowercase letter main toh likha hey par command sahi nahi hey !")
else:
    raise KeyError(
        "Bhai,Wrong Command !Ek bar firse run karle aur input main sahi command ke saath !")
