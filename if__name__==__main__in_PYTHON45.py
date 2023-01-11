""" import Harryy
Harryy.welcome()
# output will be 
------------------------------
Hey you are welcome from Harry
Hey you are welcome from Harry 
------------------------------
Cause of printing twice is due to import ,all the codes of import module is running so there is a call of welcome() so 1st line is for this and the second line is due to the call of welcome() from this file.
"""
# So How to avoid The above problem So we have to use a statement i.e.    if __name__== "__main__": inside the imported module/file like, Here we don't want to run welcome() in the module so inside the scope of the if __name__== "__main__": write the welcome() instead of written simply in "Harryy.py"
import Harryy
# print(__name__)
Harryy.welcome() #Now it will print only once


# Go to Harryy.py for better Understanding
# __name__== "__main__" idom is a common pattern used in pythonscripts to determine whether the scriptsis being run directly or being imported as a module into another script.

"""
The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set to the name of the module.

Here's an example of how the if __name__ == __main__ idiom can be used:

def main():
    # Code to be run when the script is run directly
    print("Running script directly")

if __name__ == "__main__":
    main()
In this example, the main function contains the code that should be run when the script is run directly. The if statement at the bottom checks whether the __name__ variable is equal to __main__. If it is, the main function is called.

Why is it useful?
This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script. For example, consider the following script:

def main():
    print("Running script directly")

if __name__ == "__main__":
    main()
If you run this script directly, it will output "Running script directly". However, if you import it as a module into another script and call the main function from the imported module, it will not output anything:

import script

script.main()  # Output: "Running script directly"
This can be useful if you have code that you want to reuse in multiple scripts, but you only want it to run when the script is run directly and not when it's imported as a module.

Is it a necessity?
It's important to note that the if __name__ == "__main__" idiom is not required to run a Python script. You can still run a script without it by simply calling the functions or running the code you want to execute directly. However, the if __name__ == "__main__" idiom can be a useful tool for organizing and separating code that should be run directly from code that should be imported and used as a module.

In summary, the if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script. It allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script.

"""