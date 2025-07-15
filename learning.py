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