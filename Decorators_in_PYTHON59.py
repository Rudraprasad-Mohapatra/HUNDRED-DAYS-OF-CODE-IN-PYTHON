# def greet(fx):
#     def mfx():
#         print("Good Morning!")
#         fx()
#         print("Thanks for using this functions.")
#     return mfx


# @greet
# def hello():
#     print("Hello World!")


# hello()

#    or from line 9 to 11  and 13can be replaced by
# greet(hello)()


def add_greet(fx):
    # def mfx():Here we have not passed the parameters so using this will give error 
    def mfx(*args, **kwargs): #our parameters are passing now,  " *args means taking all parameters as tuples " and " **kwargs means taking all parameters in the form of dictionaries i.e key value pairs"
        print("Good Morning")
        fx(*args,**kwargs) #here our function should run with parameter *args and **kwargs ,fx(parametrs) is the replace ment of add(parameters)
        print("Thanks for using this function!")
    return mfx        


# @add_greet
def add(a, b):
    print(a+b)

# add(1,2) #parameters are not able to go to the function
# or the alternative code of line 33 will be
add_greet(add)(1,2) #make sure you are commenting @add_greet

"""
Notes:-

Python Decorators

Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:

@decorator_function
def my_function():
    pass
The @decorator_function notation is just a shorthand for the following code:

def my_function():
    pass
my_function = decorator_function(my_function)
Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.

Practical use case
One common use of decorators is to add logging to a function. For example, you could use a decorator to log the arguments and return value of a function each time it is called:

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
In this example, the log_function_call decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.

Conclusion
Decorators are a powerful and flexible feature in Python that can be used to add functionality to functions and methods without modifying their source code. They are a great tool for separating concerns, reducing code duplication, and making your code more readable and maintainable.

In conclusion, python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.
"""
