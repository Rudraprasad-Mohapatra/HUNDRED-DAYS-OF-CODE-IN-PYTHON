# uses memoization technique
# import functools
# or
from functools import lru_cache
import time

# @functools.lru_cache(maxsize=None)
# or
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    print(f"Done for {n}")
    return n*5

print(fx(20))

print(fx(2))

print(fx(6))

# Here first 3 prints will take '3 sec' to print each one but the rest 3 prints below will take no time to print because the calculations are already done and stored in cache so using memoization it gives the result o that it does not recalculate the same thing again and again
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")

# Cache will be maintained for a single program,if you run the program again it first calculates and stores in the cache then reuse when see the function again in the same program
"""
NOTES:
Function Caching in Python
Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.

In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called. Here's an example:

import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))
# Output: 6765
As you can see, the functools.lru_cache decorator is used to cache the results of the fib function. The maxsize parameter is used to specify the maximum number of results to cache. If maxsize is set to None, the cache will have an unlimited size.

Benefits of Function Caching
Function caching can have a significant impact on the performance of a program, particularly for computationally expensive functions. By caching the results of a function, you can avoid having to recompute the results every time the function is called, which can save a significant amount of time and computational resources.

Another benefit of function caching is that it can simplify the code of a program by removing the need to manually cache the results of a function. With the functools.lru_cache decorator, the caching is handled automatically, so you can focus on writing the core logic of your program.

Conclusion
Function caching is a technique for improving the performance of a program by storing the results of a function so that you can reuse the results instead of recomputing them every time the function is called. In Python 3, function caching can be achieved using the functools.lru_cache decorator, which provides an easy and efficient way to cache the results of a function. Whether you're writing a computationally expensive program, or just want to simplify your code, function caching is a great technique to have in your toolbox.
"""