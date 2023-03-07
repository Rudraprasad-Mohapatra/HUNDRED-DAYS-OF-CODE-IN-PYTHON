import time
import asyncio
import requests

async def function1():
    print("func1")
    # # time .sleep(3)
    # await asyncio.sleep(1)
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram1.ico", "wb").write(response.content)
    
    print(time. time())
    return "harry"
async def function2():
    print("func2")
    # time .sleep(3)
    # await asyncio.sleep(1)
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram2.ico", "wb").write(response.content)
    
    print(time. time())
    return "harrybhai"
async def function3():
    print("func3")
    # time .sleep(3)
    # await asyncio.sleep(4)
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)
    
    print(time. time())
    return "harrybhaisahab"

# async def main():
#     asyncio.create_task(function2())
#     task = asyncio.create_task(function1()) #while running func2 it gets time and run it's code
#     # await function2()
#     await function3()
    
#     # asyncio.create_task(function3())

#If I want to run all things at a time I can do like 
async def main():
    L = await asyncio.gather(
        function2(),
        function1(),
        function3(),
        )
    print(L)

asyncio.run(main())

#Normal way of calling function
# function1()
# function2()
# function3()    
"""
Async IO in Python
Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

Syntax
Here is the basic syntax for creating an asynchronous function in Python:

import asyncio

async def my_async_function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"

async def main():
    result = await my_async_function()
    print(result)

asyncio.run(main())
Another way to schedule tasks concurrently is as follows:

L = await asyncio.gather(
        my_async_function(),
        my_async_function(),
        my_async_function(),
    )
print(L)
Async IO is a powerful programming pattern that allows for high-performance and concurrent I/O operations in Python. With the asyncio module and asynchronous functions, you can write efficient and scalable code that can handle large amounts of data and I/O operations without blocking the main thread. Whether you're working on web applications, network services, or data processing pipelines, async IO is an essential tool for any Python developer.
"""