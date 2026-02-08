import time
# wrapper function - to modify the behavior of a function without changing its code
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Functions {func.__name__} took : {end_time - start_time:.4f} seconds to execute.")
        return result

    return wrapper

@timer
def execute_function(n):
    return f"the sum is {sum(range(n))}"

print(execute_function(1000000))


# @property decorator - to access private attributes of a class (self._attribute) without using getter and setter methods
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


# @staticmethod decorator - to define a method that does not require access to the instance (self) or class (cls) variables
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

ops = MathOperations()
ops.add(5, 3)

# @classmethod decorator - to define a method that requires access to the class (cls) variables but not the instance (self) variables
class Circle:
    pi = 3.14159

    @classmethod
    def area(cls, radius):
        return cls.pi * radius ** 2

print(Circle.area(5))

# functools.wraps decorator - to preserve the original function's metadata (name, docstring) when using a wrapper function
from functools import wraps
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed successfully.")
        return result

    return wrapper

@log_execution
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"
print(greet("Alice"))

# lru_cache decorator - to cache the results of a function based on its arguments, improving performance for expensive function calls
from functools import lru_cache
@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(30))

#data class decorator - to automatically generate special methods like __init__, __repr__, and __eq__ for a class based on its attributes
from dataclasses import dataclass

@dataclass
class product:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity
p1 = product("Laptop", 999.99, 2)
print(p1)

