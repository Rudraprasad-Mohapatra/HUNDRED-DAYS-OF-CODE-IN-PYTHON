def welcome():
    print("Hey you are welcome from Harry")
print(__name__) #When it will run from here it will print __main__ otherwise if we import the module it will print Harryy i.e Here we are saying when __name__ is equal with __main__ i.e we are running this file then only run the welcome() otherwise don't run the welcome() when this file is imported to some other file.
if __name__== "__main__":
    welcome()

    