# usage of async and how to get the runining output learning asynchronous programming very essential.

# >>> import asyncio
# >>> 
# >>> class FakeLLMStream:
# ...     def __init__(self, prompt):
# ...         self.prompt = prompt
# ...         self.responses = ["Hello", ", ", "I ", "am ", "a ", "chatbot.", " 🤖"]
# ...     async def __aenter__(self):
# ...         print("Connecting to LLM agent...")
# ...         await asyncio.sleep(1)  # Simulate connection delay
# ...         return self
# ...     async def __aexit__(self, exc_type, exc, tb):
# ...         print("\nDisconnected from LLM agent.")
# ...     async def aiter_tokens(self):
# ...         for token in self.responses:
# ...             await asyncio.sleep(0.3)  # Simulate delay between tokens
# ...             yield token
# ... 
# >>> async def stream_response_from_llm(prompt: str):
# ...     async with FakeLLMStream(prompt) as stream:
# ...         async for token in stream.aiter_tokens():
# ...             print(token, end="", flush=True)
# ... 
# >>> 
# >>> if __name__ == "__main__":
# ...     asyncio.run(stream_response_from_llm("Tell me something cool"))
# ... 
# Connecting to LLM agent...
# Hello, I am a chatbot. 🤖-----------------------> THIS OUTPUT CAME AFTER 0.3 ms
# Disconnected from LLM agent.

#COMPREHENSIONS:
# >>> [x for x in range(10) if x%2 == 0]#list comprehension
# [0, 2, 4, 6, 8]
# >>> [x for x in range(10) if x%2 != 0]
# [1, 3, 5, 7, 9]
# >>> {x for x in range(10) if x%2 == 0}#set comprehension
# {0, 2, 4, 6, 8}
# >>> arr = [2,3,4,2,5,6,3,4]
# >>> [x for x in arr if x%2 == 0]
# [2, 4, 2, 6, 4]
# >>> {x for x in arr if x%2 == 0}
# {2, 4, 6}

# >>> (x for x in arr if x % 2 == 0)#generator for lazy evaluationa nd not storing the final response
# <generator object <genexpr> at 0x7f6a22fc7760>

# >>> evens_gen = (x for x in arr if x % 2 == 0)
# >>> 
# >>> for num in evens_gen:
# ...     print(num)  # Outputs: 2 4 2 6 4 (one by one)
# ... 
# 2
# 4
# 2
# 6
# 4

#ERROR HANDLING:
# >>> arr = [2, 0, 4, 5]
# >>> 
# >>> try:
# ...     result = [10 / x for x in arr]        # ZeroDivisionError when x == 0
# ... except ZeroDivisionError as e:
# ...     print("Caught:", e)
# ... else:
# ...     print(result)
# ... finally:
# ...     print("Comprehension finished")
# ... 
# Caught: division by zero
# Comprehension finished


# OOPs in Python:
'''
1) --------------class and object----------------:

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an object
d1 = Dog("Bruno")
d1.bark()

2) ----------------constructor----------------:

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

3)------------------class variable and instance variable------------------:

class Student:
    school = "ABC School"  # Class variable (shared)

    def __init__(self, name):
        self.name = name  # Instance variable (unique)

s1 = Student("Alice")
s2 = Student("Bob")
print(s1.school)  # Same for both

4)-------------------Ecapsulation:  '__' for private and '_' for protected----------------:

Type	      Syntax Example	         Accessible From
Public	       self.balance	                Anywhere
Protected	   self._balance	        Class + Subclasses
Private	       self.__balance	      Only inside the class (name mangled)

class Account:
    def __init__(self, balance, code):
        self._balance = balance         # Protected variable
        self.__secret_code = code       # Private variable
    def show_account_data(self):
        print("[Account] Balance (protected):", self._balance)
        print("[Account] Secret Code (private):", self.__secret_code)


class Bank(Account):
    def __init__(self, balance, code):
        super().__init__(balance, code)
    def access_protected(self):
        print("[Bank] Accessing protected _balance:", self._balance)  # ✅ Allowed
    def access_private(self):
        # ❌ This will raise an error due to name mangling
        print("[Bank] Trying to access __secret_code:", self.__secret_code)


acc = Account(1000, "XYZ123")
bank = Bank(5000, "ABC999")

print("=== Direct access from outside ===")
# ✅ Can access protected (though not recommended)
print("Outside access to protected _balance:", acc._balance)

# ❌ Cannot access private directly
try:
    print("Outside access to private __secret_code:", acc.__secret_code)
except AttributeError as e:
    print("ERROR:", e)

# ✅ But can use name mangling to access private (not recommended)
print("Outside access to private with name mangling:", acc._Account__secret_code) #### obj._className__privateVar

print("\n=== Access inside Account class ===")
acc.show_account_data()

print("\n=== Access inside Bank subclass ===")
bank.access_protected()

# ❌ Will raise error
try:
    bank.access_private()
except AttributeError as e:
    print("ERROR:", e)


5)----------------------Inheritance----------------------: Done in Amount and Bank class.

6)----------------------super()----------------------:
>>> class greet:
...    def greet(self):
...        print("Hi, it's raining!!!!")
... 
... 
>>> class Child(greet):
...     def greet(self):
...         super().greet() ##here I am calling the parent class function.
...         print("Hello from child")
... 
>>> 
>>> obj1 = greet()
>>> obj2 = Child()
>>> 
>>> obj2.greet()
Hi, it's raining!!!!
Hello from child
>>> 

7) -----------------Polymorphism: one name different function.---------------------:
>>> class Bird:
...    def move(self):
...        print("Bird is flying!!")
... 
>>> class Animal:
...    def move(self):
...        print("Animal is runing!!")
... 
>>> o1 = Bird()
>>> o2 = Animal()
>>> o1.move()
Bird is flying!!
>>> o2.move()
Animal is runing!!

8) ------------------Abstraction: hiding the functionality and giving flexibility to give the flexibility.---------------------

>>> from abc import ABC, abstractmethod
>>> 
>>> class Shape(ABC):
...     @abstractmethod
...     def area(self):
...         pass
... 
>>> 
>>> class Square(Shape):
...     def __init__(self, side):
...         self.side = side
...     def area(self):
...         return self.side * self.side
... 
>>> class Triangle(Shape):
...     pass  # ❌ Error: Must implement area()
... 
>>> shape = Shape()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Shape with abstract method area
>>> tri = Triangle()=======>  as you have not added the functionality inside the abstract method therefore this Triangle is also the abstract class and can't instanciate. 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Triangle with abstract method area
>>> 
>>> 
>>> def print_area(shape: Shape):
...     print("Area is:", shape.area())
... 
>>> s = Square(4)
>>> print_area(s)
Area is: 16


9) -----------------------------------------TYPES OF METHOD IN A CLASS-------------------------------------------

methods can be classmethod, staticmethod, instance method
        1. Instance method: You use it when you want to perform an action specific to the object.  def f(self, ...):
        2. Class Method: You use this when:----> 
                @classmethod
                def f(cls,..):
                You need to work with class-level data (e.g. users list)
                Or you want to build a custom constructor
        3. Static Method: You use this when:----> 
                @staticmethod
                def f(...):
                The method is related to the class logically
                But doesn’t need access to class or instance data

                    Task:
                    Create a class Product with:
                    instance variables: name, price
                    instance method: show_info() → prints product name & price
                    class method: set_discount_rate(rate) → sets a class-level discount
                    static method: is_expensive(price) → returns True if price > 1000

                    File_name = task-1-classMethod-types.py

10) Inheritance and Composition:

        ->Composition is when one class contains an instance of another class. It represents a "has-a" relationship.

        class Engine:
            def start(self):
                print("Engine started")
        class Car:
            def __init__(self):
                self.engine = Engine()  # Car "has a" Engine object
            def start(self):
                self.engine.start()  # Calls the Engine's start method


        ->Inheritance is when a class extends another class, inheriting its behavior and properties. It represents an 
        "is-a" relationship.

        class Vehicle:
            def start(self):
                print("Vehicle started")

        class Car(Vehicle):#--------------->inheriting vehicle
            pass  # Inherits start method from Vehicle

        car = Car()
        car.start()  # Inherited method


============================================================================================================
Task for OOPs: Build a class hierarchy for Person, Employee, and Manager with:

Shared attributes: name, age

Method override for get_role()

Use super() in Manager

File Name = task-2-OOPs.py 
=============================================================================================================
'''
#META PROGRAMMING:

# Metaprogramming is writing programs that can:
# Create,
# Modify,
# Inspect,
# Or extend other code (including functions, classes, or modules) at runtime.

# TYPE-1: DECORATOR BASED METAPROGRAMMING:
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with {args} and {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} returned {result}")
#         return result
#     return wrapper

# @logger
# def add(x, y):
#     return x + y # NOW THIS WILL WORK ACCORDING TO LOGGER DECORATOR

# >>> add(2, 3)
# Calling add with (2, 3) and {}
# add returned 5
# 5


# NOW SEE HOW TOOL DECORATOR IS MAKE INTERNALLY VIA LANGCHAIN:

# tool_registry = {}---------------------> HERE ALL THE TOOLS ARE STORED.

# def tool(func):
#     func._is_tool = True------------------>HERE CHECKING IF A FUNCTION IS UNDER TOOL DECORATOR 
#     return func

# class ToolMeta(type):
#     def __new__(cls, name, bases, dct):
#         for attr, val in dct.items():
#             if callable(val) and getattr(val, "_is_tool", False):----------------->IF val IS A FUNCTION AND IS IN TOOL DECORATOR THEN STORE IN tool_registory COLLECTION.
#                 tool_registry[attr] = val
#         return super().__new__(cls, name, bases, dct)

# class MyTools(metaclass=ToolMeta):

#     @tool
#     def greet(self, name):
#         return f"Hello, {name}"

# tools = MyTools()
# print(tool_registry['greet'](tools, "Suwarna"))  # Hello, Suwarna




#TYPE-2: CLASS CREATION WITH type()
# This type() function is used to check the type of the object but it is also a metaclass and used to 
# create a class  without using the keyword class and used for metaprogramming, auto-registoring and tool calling in AI.
# type(class_name, bases, dict)--------> bases== is the parent class it inherits if it

# >>> def say_hello(self):
# ...     print(f"Hello from {self.name}!")
# ... 
# >>> # Creating class dynamically
# >>> Person = type('Person', (object,), {
# ...     'name': 'Swarna',#---------------------> this is the class variable 
# ...     'say_hello': say_hello #------------------> this is the function similarly you can make the constructors too.
# ... })
# >>> 
# >>> p = Person()
# >>> p.say_hello()  # Output: Hello from Swarna!
# Hello from Swarna!
# >>> 
#
# MANY MORE WAYS TO USE type() FUNCTION.


# METACLASS:

# __new__ → Used to modify class attributes before the class is created.
# __init__ → Used after the class is created, useful for class registration.

# class Meta(type):
#     def __new__(cls, name, bases, dct):
#         print(f"Creating class: {name}")
#         print(f"Bases: {bases}")
#         print(f"Attributes: {list(dct.keys())}")
#         return super().__new__(cls, name, bases, dct)
#     def __init__(cls, name, bases, dct):
#         print(f"Meta.__init__ called for {name}")
#         super().__init__(name, bases, dct)

# class Base: pass

# class MyClass(Base, metaclass=Meta):
#     x = 42
#     person_name = "Suwarna Shukla"
#     age = 22
#     phone = "mi"
#     def hello(self): pass

# OUTPUT:
#
# Creating class: MyClass
# Bases: (<class '__main__.Base'>,)
# Attributes: ['__module__', '__qualname__', 'x', 'person_name', 'age', 'phone', 'hello']
# Meta.__init__ called for MyClass
# >>> 


# TOOL CALLLING IN AGENTIC AI

# >>> TOOL_REGISTRY = {}
# >>> 
# >>> class ToolMeta(type):
# ...     def __init__(cls, name, bases, dct):
# ...         if name != 'BaseTool':  # Don't register base
# ...             TOOL_REGISTRY[name] = cls
# ...         super().__init__(name, bases, dct)
# ... 
# >>> class BaseTool(metaclass=ToolMeta):
# ...     pass
# ... 
# >>> class MyTool(BaseTool):
# ...     pass
# ... 
# >>> class AnotherTool(BaseTool):
# ...     pass
# ... 
# >>> print(TOOL_REGISTRY)
# {'MyTool': <class '__main__.MyTool'>, 'AnotherTool': <class '__main__.AnotherTool'>}




####FUNCTION CALLING USING TOOL CALLING:




#=============================================================================================================================

# ITERATOR:

class Countdown:
    def __init__(self, n): 
        self.n = n  # Starting number
    def __iter__(self): 
        return self  # Returns the object itself as an iterator
    def __next__(self):
        if self.n == 0:
            raise StopIteration  # Signals end of iteration
        self.n -= 1
        return self.n + 1  # Return current value

#OUTPUT:

# >>> c = Countdown(3)
# >>> next(c)
# 3
# >>> next(c)
# 2
# >>> next(c)
# 1

# >>> list(Countdown(10))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]-----------> working itself with the help of iter and next


# GENERATORS:
# A generator is a simpler way to create iterators.

# ✅ How to make a generator?
# Use the yield keyword in a function.

# Feature	              Iterator Class	                            Generator Function
# Structure	       Class with __iter__, __next__	               Function with yield
# Memory usage	      Manual control	                          Efficient (pause/resume)
# Use case	        More control, complex state	                      Simpler, readable



#=========================================================================================================================

# CONTEXT MANAGER:

# A context manager is a Python construct that sets something up and tears it down — typically used to manage resources 
# like files, database connections, locks, etc.
# It’s most commonly used with the with statement.


# CUSTOM CONTEXT MANAGER (CLASS-BASED)
class MyContext:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")
        if exc_type:
            print(f"Error caught: {exc_type.__name__} - {exc_val}")
        return True  # suppresses the error

with MyContext():
    print("Inside block")
    1 / 0  # Causes ZeroDivisionError

# OUTPUT:

# Entering
# Inside block
# Exiting
# Error caught: ZeroDivisionError - division by zero


# def __exit__(self, exc_type, exc_val, exc_tb):
#     ...

# These parameters represent information about any exception that occurred inside the with block:

# Parameter	Meaning
# exc_type	The exception class/type (e.g., ZeroDivisionError)
# exc_val	The exception instance/message (e.g., ZeroDivisionError('div by 0'))
# exc_tb	The traceback object (info about where the error happened)



# CONTEXT MANAGER USING @custommanager DECORATOR (FUNCTION BASED CUSTOM MANAGER):

# The error is happening because you're doing division outside the context block, and you're not using yield, which is required for a function decorated with @contextmanager.

# ❌ What's wrong in your code:

# @contextmanager
# def divide(num: int, dino: int):
#     return num/dino  # ❌ Not using yield


# >>> from contextlib import contextmanager
# >>> 
# >>> @contextmanager
# ... def divide(num: int, dino: int):
# ...     try:
# ...         result = num / dino
# ...         yield result
# ...     except ZeroDivisionError as e:
# ...         print("Division by zero is not allowed.")
# ...         yield None
# ... 
# >>> 
# >>> divide(10,0)----------------> HERE I AM JUST USING CONTEXT MANAGER OBJECT NOT THE CODE INSIDE THE CONTEXT MANAGER.
# <contextlib._GeneratorContextManager object at 0x7f40f8ee9960>
# >>> 
# >>> 
# >>> 
# >>> with divide(10, 2) as result:-------> WITH IS REQUIRED TO USE THE CODE INSIDE THE CONTEXT MANAGER
# ...     print("Result:", result)
# ... 
# Result: 5.0
# >>> with divide(10, 0) as result:
# ...     print("Result:", result)
# ... 
# Division by zero is not allowed.
# Result: None



#FOR ASYNC CONTEXTMANAGER: @asynccontextmanager
#Used with async with for resources that require asynchronous setup and teardown.

import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def resource():
    print("Connecting...")
    await asyncio.sleep(10)
    yield "Resource ready"
    print("Disconnected.")

async def main():
    async with resource() as res:
        print(res)

asyncio.run(main())

# >>> asyncio.run(main())
# Connecting...
# Resource ready
# Disconnected.


#=======================================================================================================================

# CONCURRENCY AND PARALLELISM:------->[X --> not understood problem but little less important so leave for now]

#            Is your task I/O-bound?
#                       |
#          Yes ----------------- No (CPU-bound)
#           |                         |
# Use threading or              Use multiprocessing or
# ThreadPoolExecutor         ProcessPoolExecutor



#THREADING:

# BY THREADING MODULE:

# >>> import threading, time
# >>> 
# >>> def worker():
# ...     print("Start")
# ...     time.sleep(1)
# ...     print("Done")
# ... 
# >>> t1 = threading.Thread(target=worker)
# >>> t2 = threading.Thread(target=worker)
# >>> t1.start(); t2.start()
# Start
# Start
# >>> t1.join(); t2.join()
# Done
# Done


# BY HIGHER LEVEL API:

from concurrent.futures import ThreadPoolExecutor #memory is shared by each thread
import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(task, "Thread-A")
    executor.submit(task, "Thread-B")

# ... 
# Thread-A started
# <Future at 0x7fa11ab28790 state=running>
# Thread-B started
# <Future at 0x7fa11a867df0 state=running>
# Thread-A finished
# Thread-B finished


# MULTIPROCESSING

# >>> import multiprocessing
# >>> import time
# >>> 
# >>> def worker(num):
# ...     print(f"Worker {num} started")
# ...     time.sleep(2)
# ...     print(f"Worker {num} finished")
# ... 
# >>> if __name__ == "__main__":
# ...     p1 = multiprocessing.Process(target=worker, args=(1,))
# ...     p2 = multiprocessing.Process(target=worker, args=(2,))
# ...     
# ...     p1.start()
# ...     p2.start()
# ...     
# ...     p1.join()
# ...     p2.join()
# ... 
# Worker 1 started
# Worker 2 started

# Worker 1 finished
# Worker 2 finished
# >>> 

# BY HIGHER LEVEL API:

from concurrent.futures import ProcessPoolExecutor  #each task have individual memory resorces they don't share.
import time

def square(n):
    return n * n

with ProcessPoolExecutor() as executor:
    results = executor.map(square, [1, 2, 3, 4])
    print(list(results))

# ... 
# [1, 4, 9, 16]
# >>> 


#==========================================================================================================================

# ASYNCHRONOUS PROGRAMMING:

# asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and 
# web-servers, database connection libraries, distributed task queues, etc.


'''
Key Terms to know:

1. Synchronous Programming: Sequential task execution; each task waits for the previous one to complete.-----------> Inefficient means 
CPU's resources are unused when one task needs waiting

2. Asynchronous Programming: Tasks can run independently of main loop; non-blocking operations enhance efficiency.-----------> Efficient and mostly used

3. Concurrency: Managing multiple tasks simultaneously, often through interleaving; doesn't imply simultaneous execution.

4. Parallel Programming: Executing multiple tasks simultaneously on different processors or cores to speed up computations.

Relation to asyncio: [for ASYNCHRONOUS PROGRAMMING + CONCURRENT PROGRAMMING]

Python's asyncio library is designed for writing concurrent code using the async and await syntax. 

It enables asynchronous programming by allowing a single thread to manage multiple I/O-bound tasks efficiently. 

While asyncio facilitates concurrency through asynchronous programming, it doesn't provide parallel execution for CPU-bound tasks. 

For parallelism, Python offers the multiprocessing module, which allows tasks to run on multiple CPU cores.


The asyncio package in Python is a library designed for writing concurrent code using the async and await syntax. It serves as the 
foundation for building asynchronous frameworks that handle tasks such as network operations, web servers, and database connections. 

Central to asyncio is the event loop, which orchestrates the execution of asynchronous tasks, callbacks, and handles I/O events, 
ensuring efficient task management.


__init__.py file in the asyncio package orchestrates the importation of various submodules and consolidates their public interfaces, 
providing a cohesive and unified API for asynchronous programming in Python.

So in short Asynchronous programming where you can do CPU bound operation while you are waiting for I/O operation.
'''

'''
Fundamentals of Asyncio Package:

1. Event Loop: Core that manages distributed tasks.It have the work to execute which is ready to execute and if some process is waiting 
               for something like data or something that event loop execute it when that function is ready for it.

2. Coroutines: Just the async function is the coroutine and the simple function calling is coroutine object and running the coroutine 
               that is the async function is called running the evnt loop.

        >>> import asyncio
        >>> 
        >>> async def main(): #----------------> coroutine
        ...     print("Starting coroutine")
        ... 
        >>> main() #--------------> simply running asynchronous function is coroutine object
        <coroutine object main at 0x7f7a7ff0ac00>
        >>> 
        >>> asyncio.run(main()) #----------------> running the coroutine object using asyncio is called running of event loop.
        Starting coroutine
        >>> 

    Now you might be thinking that the why we need asyncio.run() to run the coroutine object the problem is that the function need to be waited 
    for the data or something and simply running main() won't wait can will leads to error so we need this run() function.

        >>> import asyncio 
        >>> 
        >>> async def person(name):
        ...     print("Fetching data...")
        ...     await asyncio.sleep(2)
        ...     print("Data Fetched")
        ...     return {"name": name}
        ... 
        >>> async def main():------------------------------> this is the main coroutine 
        ...     print("Start coroutine")
        ...     detail = person("Suwarna Shukla")
        ...     result = await detail--------------------------> a coroutine does not start executing until await is called=======> so it will run 74, 75, and the 76th line this person(name) function is called so without this sync person function is not called.
        ...     print(f"Recieve Result: {result}")
        ...     print("End of coroutine")
        ... 
        >>> asyncio.run(main())------------------------------> therefore we use main here 
        Start coroutine
        Fetching data...
        Data Fetched
        Recieve Result: {'name': 'Suwarna Shukla'}
        End of coroutine
        >>> 

       Multiple tasks are created but they are not runned concorrently so they are just running synchronously 
       so we did not got the performance efficiency both task is taking sepearet 2-2 seconds.

        >>> async def main():
        ...     print("Start coroutine")
        ...     detail1 = person("Suwarna Shukla")---------------->TASK-1
        ...     detail2 = person("Sonal")------------------------->TASK-2
        ...     result1 = await detail1
        ...     result2 = await detail2
        ...     print(f"Recieve Result: {result1}")
        ...     print(f"Recieve Result: {result2}")
        ...     print("End of coroutine")
        ... 
        >>> asyncio.run(main())
        Start coroutine
        Fetching data...
        Data Fetched
        Fetching data...
        Data Fetched
        Recieve Result: {'name': 'Suwarna Shukla'}
        Recieve Result: {'name': 'Sonal'}
        End of coroutine

        
'''

'''
3. Task Creation: Task are created to run the coroutines concurrently.

'''
# async def person(name):
#     print("Fetching data...")
#     await asyncio.sleep(2)
#     print("Data Fetched")
#     return {"name": name}
# async def main():
#     print("Start coroutine")
#     detail1 = person("Suwarna Shukla")
#     detail2 = person("Sonal")
#     result1 = await detail1
#     result2 = await detail2
#     print(f"Recieve Result: {result1}")
#     print(f"Recieve Result: {result2}")
#     print("End of coroutine")


import asyncio
from datetime import datetime

async def person(name):
    print("Fetching data")
    await asyncio.sleep(2)
    print("Data Fetched")
    return {"name": name}


# async def main(): -----------------> this show as how task created inidividually we can create all at onces in single line via gather
#     print("Start coroutine")
#     # If done this way then concurrency won't be followed leads to synchronous programming to overcome this we need to make task
#     # detail1 = person("Suwarna Shukla")
#     # detail2 = person("Sonal")
#     # detail3 = person("tuntun")
#     current_time = datetime.now().time()
#     print(current_time)
#     detail1 = asyncio.create_task(person("Suwarna Shukla"))#------->used create concurrent task and if you create later then it will work like synchronous task
#     detail2 = asyncio.create_task(person("Sonal"))
#     detail3 = asyncio.create_task(person("tuntun"))
#     result1 = await detail1
#     result2 = await detail2
#     result3 = await detail3 
#     current_time1 = datetime.now().time()
#     print(result1, result2, result3)
#     print(current_time1)

# asyncio.run(main())

#Time Difference: 0:00:02.002712--------------> See here concurrency works here in 2 sec all the 3 tasks occured in between when one task need to wait for 2 sec.


'''
async def main():
    print("Start coroutine")
    current_time = datetime.now().time()
    print(current_time)
    detail1 = asyncio.create_task(person("Suwarna Shukla"))
    detail2 = asyncio.create_task(person("Sonal"))
    result1 = await detail1
    result2 = await detail2
    detail3 = asyncio.create_task(person("tuntun"))-----------------> This now work as synchronous task as both the task created and executed then this task3 is 
                                                                      created and then executed via await
    result3 = await detail3 
    current_time1 = datetime.now().time()
    print(result1, result2, result3)
    print(current_time1)

'''

# async def main():
#     print("Start coroutine")
#     task = await asyncio.gather(person("Sona"),person("Mona"), person("Dona"))#-------> This gather is used to create the task and also execute it also 
#                                                                                         #so create_task and await task both happen in this function itself.
#     #result = await task
#     print(task)
#     print("Coroutine completed")

# asyncio.run(main())

# This is prone to errors as if one of the task fails then all will fail and error handling is not good so we have TASK GROUP 
# So, this TaskGroup() cancels all the other task if one task fails so that it don't make the system in bad state.

# async def main():
#     tasks = []
#     async with asyncio.TaskGroup() as tg:#--------------> Available in 3.11 not in 3.10
#         for n in enumerate(["Suwarna", "Sonal", "Tuntun"]):
#             task = tg.create_task(person(n))
#             tasks.append(task)

#         results = [task.result() for task in tasks]
#         for result in results:
#             print(f"Recieved result: {result}")


# asyncio.run(main())


'''
4. FUTURES: It is a promise of the future result.

asyncio.isfuture(obj)

Return True if obj is either of:
-->an instance of asyncio.Future,
-->an instance of asyncio.Task,
-->a Future-like object with a _asyncio_future_blocking attribute.

'''
import asyncio 

async def set_future_result(future, value):
    print(f"Future had bydefault value: {value}")
    await asyncio.sleep(2)
    value = "Hello !!! actually the message is complete this topic end of the day."
    future.set_result(value)
    print(f"Set the future's result to: {value}")

async def main():
    loop = asyncio.get_running_loop() # Get the event loop----can be called from the coroutine ony.
    future = loop.create_future() #Create a future object
    asyncio.create_task(set_future_result(future, "Future result is ready"))
    result = await future # wait for the future to get a result
    print(f"Recieve the future's result: {result}")

asyncio.run(main())

# import asyncio -------------> This is how we work without future so we can set the value only when the task is complete so we should use future which help to give the placeholder.

# async def set_result():
#     await asyncio.sleep(2)
#     print("Set the result: Future result is ready")
#     return "Future result is ready"

# async def main():
#     task = asyncio.create_task(set_result())  # Start the task
#     result = await task  # Wait for task to complete
#     print(f"Received the result: {result}")

# asyncio.run(main())


'''
python-advance-py3.10bluebash@bluebash-ThinkPad-E14-Gen-3:~/Documents/python_advance$ python3 asynchronous_programming.py
Future had bydefault value: Future result is ready
Set the future's result to: Hello !!! actually the message is complete this topic end of the day.
Recieve the future's result: Hello !!! actually the message is complete this topic end of the day.



Aspect	                                      Using Future	                                         Without Future (task.result())
Purpose	            Acts as a placeholder for a value that arrives later.	                    Just waits for the task to finish and returns the result.
When Used?	        When a function does not return a value directly but will set it later.	    When a function can return a value normally.
Control	            future.set_result(value) can be called whenever needed.	                    The result is available only when the task finishes.
Blocking?	        await future waits until the future gets a result.	                        await task simply waits for task completion.
'''

'''
SYNCHRONOUS: code written normally (without asyncio, threads, or processes) is synchronous. So we normally do synchronous programming

'''



import asyncio