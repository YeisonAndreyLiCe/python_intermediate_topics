# Python Intermediate Topics

## Table of Contents

- [Python Intermediate Topics](#python-intermediate-topics)
  - [Table of Contents](#table-of-contents)
  - [Slices](#slices)
  - [Scope](#scope)
    - [Example Local Scope](#example-local-scope)
    - [Example Global Scope](#example-global-scope)
    - [Example Enclosing Scope](#example-enclosing-scope)
    - [Example Global Scope Only-read](#example-global-scope-only-read)
    - [Example Keyword `global`](#example-keyword-global)
    - [Built-in Scope](#built-in-scope)
  - [Modules](#modules)
    - [if **name** == "**main**":](#if-__name__--__main__)
  - [Packages](#packages)
  - [Python Virtual Environments](https://github.com/YeisonAndreyLiCe/virtual_environments)
    <!-- - [Exceptions](#exceptions) -->
    <!-- - [Iterators](#iterators) -->
  - [Closures](#closures)
  - [Decorators](#decorators-higher-order-functions)
  - [Generators](#generators)
  - [Context Managers](#context-managers)
  <!-- - [Regular Expressions](#python-regular-expressions) -->
  - [Object Oriented Programming](#object-oriented-programming)
    - [Classes](#classes)
    - [Objects](#objects)
    - [Constructor](#constructor-init)
    - [self](#self)
    - [Attributes](#attributes-Properties-have)
    - [Methods](#methods-Behaviours-do)
      - [Instance Methods](#instance-methods)
      - [Class Methods (@classmethod)](#@classmethod)
      - [Static Methods (@staticmethod)](#@staticmethod)
    - [The four pillars of OOP](#the-four-pillars-of-oop)
      - [Encapsulation in Python](#encapsulation-in-python)
        - [@property](#@property-decorator)
      - [Inheritance](#inheritance)
        - [Multiple Inheritance](#multiple-inheritance)
      - [Polymorphism](#polymorphism)
      - [Abstraction](#abstraction)
  - [Splat Operator](#splat-operator-*-and-double-splat-operator-**)
  - [Multiple Arguments (\*args)](#multiple-arguments)
  - [Keyword Arguments (\*\*kwargs)](#keyword-arguments)
  - [Unpacking Arguments](#unpacking-arguments)
  - [Lambda Expressions](#lambda-functions)
  - [Map](#map)
  - [Filter](#filter)
  - [Reduce](#reduce)
  - [Sort and Lambda](#sort-and-lambda)
  - [Ternary Operator](#ternary-operator)
  - [List Comprehensions](#list-comprehensions)
  - [Dictionary Comprehensions](#dictionary-comprehensions)
  - [Set Comprehensions](#set-comprehensions)
  - [References](#references)

## Slices

```python
# Slices
# [start:stop:step]
# start: index to start slice
# stop: index to stop slice
# step: size of the jump

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get first element
print(my_list[0]) # 1

# Get last element
print(my_list[-1]) # 10

# Get first 3 elements
print(my_list[:3]) # [1, 2, 3]

# Get last 3 elements
print(my_list[-3:]) # [8, 9, 10]

# Get elements from index 3 to 6
print(my_list[3:7]) # [4, 5, 6, 7]

# Get elements from index 0 to 8 with step 2
print(my_list[0:9:2]) # [1, 3, 5, 7, 9]
```

## Scope

Scopes are the contexts in which names are looked up. There are three different scopes in Python: `local`, `enclosing`, `global`, and `built-in`. The scope of a name defines the area of the program where you can unambiguously access that name, such as variables, functions, objects, and so on. The scope of a name is determined by the place where it is declared. Names that are declared outside of all functions are in the `global` scope. This means that those names can be accessed inside or outside of functions. Names that are declared inside a function are in the `local` scope, and can only be accessed inside that function. The `enclosing` scope is a special scope that only exists for nested functions. If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. The `built-in` scope is the outermost scope in Python, and it is the scope that contains all of the built-in names in Python. The built-in scope is searched last, after the local, enclosing, and global scopes (LEGB).

### Example Local Scope

```python
def my_func():
    x = 10
    print(x)

my_func()
print(x)
```

Output:

```output
10
Traceback (most recent call last):
  File "scope.py", line 7, in <module>
    print(x)
NameError: name 'x' is not defined
```

### Example Global Scope

```python
x = 10

def my_func():
    print(x)

my_func()
print(x)
```

Output:

```output
10
10
```

### Example Enclosing Scope

```python
def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer:', x)

outer()
```

Output:

```output
inner: nonlocal
outer: nonlocal
```

note that the `nonlocal` keyword is used to declare that `x` is not a local variable. Hence, when we assign a value to `x` inside the nested function, that change is reflected in the local variable in the enclosing function.

### Example Global Scope Only-read

```python
x = 10

def my_func():
    x = 20
    print(x)

my_func()
print(x)
```

Output:

```output
20
10
```

### Example Keyword `global`

```python
x = 10

def my_func():
    global x
    x = 20
    print(x)

my_func()
print(x)
```

Output:

```output
20
20
```

Note that the `global` keyword is used to declare that `x` is a global variable - hence, when we assign a value to `x` inside the function, that change is reflected when we use the value of `x` in the main block.

### Built-in Scope

This are the names in the pre-defined built-in modules. These are always available in your Python programs. You can see the list of built-in names by typing `dir(__builtins__)` in the Python interpreter.

---

## Modules

A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended. Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`. A module can be imported by another program to make use of its functionality. We can define our most used functions in a module and import it, instead of copying their definitions into different programs.

### if `__name__ == "__main__"`

This is used to execute some code only if the file was run directly, and not imported. That is, if the file is imported, the code is not run. This is because when you import a module, the code in the module is executed, just like any other script. So if we want to have some code that we only want to run when the module is run directly, we can use this construct.

```python
if __name__ == "__main__":
    # execute only if run as a script
    main() # call the main function that has the code we want to run
```

## Packages

A package is a hierarchical file directory structure that defines a single Python application environment that consists of modules and subpackages and sub-subpackages, and so on. A package must contain a special file called `__init__.py` in order for Python to consider it as a package (this is mandatory for versions 2.7 below). This file can be left empty but we generally place the initialization code for that package in this file.

```python
# __init__.py
from . import module1, module2, module3 ...
```

Doing this will allows us to use namespaced modules, such as `package.module1`, `package.module2`, etc.

---

In python functions are `first class objects`. This means that functions can be passed as arguments to other functions, and can also be returned from other functions as well. Functions are also able to be defined inside other functions. This is all done to avoid code duplication and to allow programmers to create abstractions.

## Closures

> "By default, after the function finishes execution, it returns to a blank state. This means its memory is wiped of all of its past arguments". [Bex T (Medium), 2023](https://towardsdatascience.com/5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it-2b1dd7ef57f3 "5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it")

```python
def func(x):
    return x ** 2

print(func(2))
print(x)
```

Output:

```output
4
Traceback (most recent call last):
  File "closure.py", line 6, in <module>
    print(x)
NameError: name 'x' is not defined
```

A closure is a function object that remembers values in enclosing scopes.

> "By defining a variable in the enclosing scope of some inner function, you can store it in the inner function’s memory even after the function returns." [Bex T (Medium), 2023](https://towardsdatascience.com/5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it-2b1dd7ef57f3 "5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it")

In Python, these non-local variables are read-only by default and we must declare them explicitly as `nonlocal` (in Python 3) in order to modify them.

### Example from [Bex T (Medium)](https://towardsdatascience.com/5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it-2b1dd7ef57f3 "5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it")

```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

count = counter()
print(count())
print(count())
print(count())
```

Output:

```output
1
2
3
```

## Positional and keyword arguments (\*args, \*\*kwargs)

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, a=1, b=2, c=3)
```

Output:

```output
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
{'a': 1, 'b': 2, 'c': 3}
```

## Decorators (Higher order functions)

**Decorators are a way to wrap a function**, and add extra functionalities to such a function. `A decorator is a function that takes another function as an argument and returns a function`

```python
def decorator_function(original_function):
    # args and kwargs are used to accept any
    # number of positional and keyword arguments
    def wrapper_function(*args, **kwargs):
        # do something before
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def f(x):
    return x ** 2

print(f(2)) -> print(decorator_function(f)(2))
```

### wraps

without `@wraps` the name of the function will be `wrapper_function`

```python
def mock_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper_function

@mock_decorator
def f(x):
    '''Docstring'''
    return x ** 2

print(f.__name__)
print(f.__doc__)
```

Output:

```output
wrapper_function
None
```

```python
from functools import wraps

def mock_decorator(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper_function

@mock_decorator
def f(x):
    '''Docstring'''
    return x ** 2

print(f.__name__)
print(f.__doc__)
```

Output:

```output
f
Docstring
```

### Example

```python
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)
decorated_display()
```

Output:

```python
wrapper executed this before display
display function ran
```

### Example 2 (Pythonic way - sugar syntax @)

```python
def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

display()
```

Output:

```python
wrapper executed this before display
display function ran
```

---

### Example 3 (Passing arguments to decorator)

```python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display()

display_info('John', 25)
```

Output:

```output
wrapper executed this before display
display function ran
wrapper executed this before display_info
display_info ran with arguments (John, 25)
```

### Example a little more illustrative

```python
from typing impot(
    Callable,
    TypeVar,
    ParamSpec,
)

T = TypeVar('T')
P = ParamSpec('P')

def upper(func: Callable[P, str]) -> Callable[P, str]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> str:
        return func(*args, **kwargs).upper()
    return wrapper

@upper
def message(text: str) -> str:
    return f'{text}, you have received a new message.'

print(message('John'))
```

Output:

```output
JOHN, YOU HAVE RECEIVED A NEW MESSAGE.
```

### Example 4 (Decorators with arguments) from [Bex T (Medium), 2023](https://towardsdatascience.com/5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it-2b1dd7ef57f3 "5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it")

```python
def stateful_function():
    cache = {}
    def wrapper_function(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper_function

@stateful_function
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### cache

````python
import time
from functools import cache

def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time: {end - start}')
        return result
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@timer
def fibonacci_timer(n):
    return fibonacci(n)
````

This is kinda like a cache (`memoization`), so that the function doesn't have to be called again if the arguments are the same.

```python
def timer(function):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time: {end - start}')
        return result
    return wrapper
```
## Generators

Generators are a special class of functions that simplify the task of writing iterators. Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the `yield` statement whenever they want to return data. Each time `next()` is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

Generators are iterators, a kind of iterable you can only iterate over once. It’s because they do not store all the values in memory, they generate the values on the fly, that allows processing of large amounts of data efficiently.

### Example

```python
def read_large_file(filename):
    with open(filename) as file:
        while True:
            chunk = file.read(1000)
            if not chunk:
                break
            yield chunk

for chunk in read_large_file('file.txt'):
    print(chunk)
````

### Example 2 (Fibonacci sequence)

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for i in fibonacci(10):
    print(i)
```

Output:

```output
0
1
1
2
3
5
8
13
21
34
```

## Context Managers

Context managers are used to allocate and release resources precisely when you want to. They are very useful when you are working with external resources like files, network connections, etc. Context managers are normally implemented using a class that implements the special methods `__enter__()` and `__exit__()`. The `__enter__()` method is invoked when the `with` statement is encountered. The `__exit__()` method is invoked at the end of the `with` block.

### Example

```python
class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with OpenFile('sample.txt', 'w') as f:
    f.write('Testing')

with open('sample.txt', 'r') as f:
    print(f.read())
```

Example 2 (Timer) [Bex T (Medium), 2023](https://towardsdatascience.com/5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it-2b1dd7ef57f3 "5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it")

```python
import time

class Timer:
    def __init__(self):
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.end = time.time()

    def elapsed_time(self):
        return self.end - self.start

with Timer() as timer:
    print('This should take approximately 2 seconds')
    time.sleep(2)

print('Elapsed time: {}'.format(timer.elapsed_time()))
```

Note that the `__exit__()` method can optionally return a Boolean value. If it returns `True`, any exception raised within the `with` block is suppressed and execution proceeds as if no exception had occurred. If it returns `False`, any exception raised within the `with` block is not suppressed and execution proceeds normally.

### Example 3 (Locking) [Bex T (Medium), 2023](https://towardsdatascience.com/5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it-2b1dd7ef57f3 "5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it")

```python

lock = threading.Lock()

class LockedContext:
    def __init__(self, lock):
        self.lock = lock

    def __enter__(self):
        print('acquiring lock')
        self.lock.acquire()

    def __exit__(self, exc_type, exc_val, traceback):
        print('releasing lock')
        self.lock.release()

with LockedContext(lock):
    print('Lock acquired')

# The lock is automatically released when the with block ends, even if an error occurs
```

---

## Object Oriented Programming

### Classes

Classes are blueprints of objects. They are used to create objects. A class is a collection of attributes and methods. Attributes are the variables that belong to a class or class' instance. Methods are the functions that belong to a class.

### Objects (Instances)

Objects are the instances of a class. They are used to access the attributes and methods of a class. It is created using the constructor of the class. An object contains the data of a class and the methods that operate on that data.

### Constructor (init)

A constructor is a special method that is used to initialize the attributes of a class. It is called when an object of a class is instantiated. The constructor is called `__init__()` in Python. It is used to set the initial values of the attributes of a class. The constructor is called implicitly when an object is created. It is not necessary to call the constructor explicitly.

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self):
        print('driving')

red_car = Car('red', 10000) # __init__() is called implicitly.
```

### self

The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class. It does not have to be named `self` , you can call it whatever you like, but it has to be the first parameter of any function in the class.

### Attributes (Properties) (have)

Attributes are the variables that belong to a class or class' instances. They are used to store the data of a class or class' instance. Instances' attributes are defined inside the constructor using the `self` keyword, class' attributes are defined outside the constructor and are shared by all instances of the class. The attributes of a class can be modified by a instance or by the class itself.

### Methods (Behaviors) (do)

#### Instance Methods

Instance methods are the methods that belong to a instance. They are used to define the behaviors of the instance. The first parameter in a instance method is `self` , which is a reference to the current instance of the class. Instance methods have access to the attributes of the instance. Instance methods can be called using the instance name only.

#### @classmethod

The classmethods are decorated with `@classmethod` . The first parameter in a classmethod is `cls` , which is a reference to the class itself. Classmethods are used to create factory methods. Factory methods are used to create instances of a class using different ways of instantiation. Methods of a class have access to the attributes of the class. Methods of a class can be called using the class name or the instance name.

#### @staticmethod

The staticmethods are decorated with `@staticmethod` . Staticmethods are used to create utility functions. They are not bound to the class or its object. They are decorated with `@staticmethod` . Staticmethods can be called using the class name or the instance name. Staticmethods have no access to the attributes of the class or its instance.

#### Association

An attribute can be an instance of another class. This is called association.

## The Four Pillars of OOP

### Encapsulation in Python

Encapsulation is the process of wrapping data and the methods that work on data within one unit (class). This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. Attributes can be private, protected or public. Private attributes can only be accessed within the class. Protected attributes can be accessed within the class and its subclasses. Public attributes can be accessed from anywhere.  
In Python, we denote private attributes using underscore as the prefix i.e single “ \_ “ or double “ \_\_ “.

#### Example

```python
class Car:
    def __init__(self):
        self.__color: str = 'red'
        self.__updateSoftware()

    def drive(self) -> None:
        print('driving')

    def __updateSoftware(self) -> None:
        print('updating software')

red_car = Car()
red_car.drive()
red_car.__updateSoftware()
```

Output:

```output
updating software
driving
Traceback (most recent call last):
  File "encapsulation.py", line 15, in <module>
    red_car.__updateSoftware()
AttributeError: 'Car' object has no attribute '__updateSoftware'. Did you mean: '_Car__updateSoftware'?
```

```python
red_car = Car()
red_car.drive()
red_car._Car__updateSoftware() # This is the way to access 'private' methods
```

Output:

```output
updating software
driving
updating software
```

#### class property(fget=None, fset=None, fdel=None, doc=None)

This built-in function is a `factory function` that returns a property attribute. The property attribute has three methods, `fget()`, `fset()`, and `fdel()`. fget() is for getting a value of the attribute, fset() is for setting a value of the attribute, and fdel() is for deleting the attribute value. The doc argument is a string (like a comment).

#### [Example from python docs](https://docs.python.org/3/library/functions.html?highlight=property#property "python docs")

```python
class C(object):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")
```

#### @property decorator

- `__init__` : This is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.
- `__str__` : This is a special method, which is used to print the "informal" or nicely printable string representation of an object.
- `__repr__` : This is a special method, which is used to print the "official" string representation of an object.
- `__del__` : This is a special method, which is called when an object gets destroyed. You normally do not call this method yourself, it is called internally by Python when the object is no longer needed.

#### Example

```python
class Celsius:
    def __init__(self, temperature: float = 0):
        self.temperature: float = temperature

    def to_fahrenheit(self) -> float:
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self) -> float:
        """Get the current temperature."""
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

c = Celsius(37)
print(c.temperature)
c.temperature = 37
print(c.to_fahrenheit())
```

Output:

```output
Setting value
Getting value
37
Setting value
Getting value
98.60000000000001
```

The @property decorator turns the temperature() method into a “getter” for a read-only attribute with the same name, and it sets the docstring for temperature to “Get the current temperature.”

The temperature() method is still accessible, but it’s now accessed as an attribute. The temperature attribute is now a “property object” with getter and setter methods.

### Inheritance

Following the DRY (don't repeat yourself) principle, the idea of pass attributes and methods from a generic class to a more specific class, such as attributes and methods can be accessed from the child class using the `super()` function. The `super()` function returns an object that represents the parent class.

#### Example

```python
class Animal:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def eat(self) -> None:
        print(f'{self.name} is eating')

    def drink(self) -> None:
        print(f'{self.name} is drinking')

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed: str = breed

    def bark(self) -> None:
        print(f'{self.name} is barking')

```

#### Multiple Inheritance

In Python, a class can inherit from multiple base classes. This is called multiple inheritance. A class derived from multiple classes is called a `derived class`.

### Example

```python
class Base1:
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")

class Base2:
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")

class Derived(Base1, Base2):
    def __init__(self):

        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)

ob = Derived()
ob.printStrs()
```

Output:

```output
Base1
Base2
Derived
Geek1 Geek2
```

### Polymorphism

> The behavior of polymorphism allows us to specify common methods at an "abstract" level and implement them in particular instances. It is the process of using an operator or function in different ways for different data inputs. (coding dojo: [python oop](https://login.codingdojo.com "python oop"))

Polymorphism is an ability (in OOP) to use a common `interface` for multiple forms (data types). A child class can have a different implementation of the same method from the parent class. The implementation in the child class overrides the implementation in the parent class. The `super()` function can be used to call the method from the parent class and the child class can extend the functionality of the method.

### Example

```python
class Parrot:
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin:
    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
```

Output:

```output
Parrot can fly
Penguin can't fly
```

### Abstraction

Abstraction is a process of hiding the implementation details from the user, only the functionality will be provided to the user. In Python, we can achieve abstraction using `abstract classes` and `interfaces`.

---

## Splat Operator `*` and Double Splat Operator `**`

Splat operator is a kid of unpacking operator (destructuring js). It can be used to allows an iterable to be unpacked into positional arguments in a function call. It can also be used to unpack an iterable into a list or dictionary. The splat operator is represented by `*` and the double splat operator is represented by `**`.

### Splat Operator

#### Example

```python
def add(x, y):
    return x + y

nums = [3, 5]
add(*nums) # 8
```

### Double Splat Operator

#### Example

```python
def display_names(first, second):
    print(f'{first} says hello to {second}')

names = {"first": "John", "second": "Bob"}
display_names(**names) # John says hello to Bob
```

## Multiple Arguments

### Example

```python
def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count, thing))

print_everything('apple', 'banana', 'cabbage')
```

Output:

```output
0. apple
1. banana
2. cabbage
```

## Keyword Arguments

### Example

```python
def table_things(**kwargs):
    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))

table_things(apple='fruit', cabbage='vegetable')
```

Output:

```output
apple = fruit
cabbage = vegetable
```

## Unpacking Arguments

### Example

```python
def print_three_things(a, b, c):
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))

mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)

mydict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
print_three_things(**mydict)
```

Output:

```output
a = aardvark, b = baboon, c = cat
a = apple, b = banana, c = cherry
```

## Lambda Functions

Lambda functions are small anonymous functions. A lambda function can take any number of arguments, but can only have one expression. Lambda functions are used along with built-in functions like `filter()`, `map()` etc. Lambda functions are used to implement functionality that can be represented in a single line of code.

### Example

```python
# lambda arguments : expression
double = lambda x: x * 2
print(double(5)) # 10
```

## Map

The `map()` function executes a specified function for each item in an iterable. The item is sent to the function as a parameter. The `map()` function returns a map object (which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

### Example

```python
def multiply(x):
    return x * 2

numbers = [1, 2, 3, 4]
result = map(multiply, numbers)
print(list(result)) # [2, 4, 6, 8]
```

Now with lambda function

```python
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result)) # [2, 4, 6, 8]
```

## Filter

Filter creates a list of elements for which a function returns true. The `filter()` method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

### Example

```python
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result)) # [2, 4, 6]
```

## Reduce

The `reduce()` function is defined in the `functools` module. It takes a function and an iterable as arguments, and returns a single value calculated as follows: `reduce(function, sequence)` where function is a function that takes two arguments and sequence is an iterable.

### Example

```python
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result) # 10
```

## Sort and lambda

### Example

```python
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a) # [(10, -1), (0, 2), (4, 3), (9, 9)]
```

## Ternary Operator

The ternary operator is a shorthand for an if-else statement. It is used to evaluate a condition and assign a value to a variable based on the condition. The syntax of the ternary operator is `value = true-expr if condition else false-expr`.

### Example

```python
a, b = 10, 20
minimum = a if a < b else b
print(minimum) # 10
```

## List Comprehension

List comprehension is an elegant way to define and create lists based on existing lists. List comprehension is generally more compact and faster than normal functions and loops for creating list. It consists of an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

### Example

```python
[print(x) for x in range(10)] # 0 1 2 3 4 5 6 7 8 9
```

### List Comprehension with If

```python
[print(x) for x in range(10) if x % 2 == 0] # 0 2 4 6 8
```

### List Comprehension with If-Else

```python
[print(x) if x % 2 == 0 else print('odd') for x in range(10)] # odd 1 odd 3 odd 5 odd 7 odd 9
```

### Nested List Comprehension

```python
[[print(x, y) for x in range(3)] for y in range(3)] # 0 0 1 0 2 0 1 1 1 1 2 1 2 2 2 2
```

```python
[[print(x, y) for x in range(3)] if y % 2 == 0 else [print(x, y) for x in range(3)] for y in range(3)]
# 0 0 1 0 2 0 1 1 1 1 2 1 0 2 1 2 2 2
```

### Nested for in List Comprehension

```python
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [num for elem in my_list for num in elem]
print(new_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Dictionary Comprehension

Dictionary comprehension is an elegant and concise way to create a new dictionary from an iterable in Python. Dictionary comprehension consists of an expression pair (key: value) followed by a `for` clause inside curly braces `{}`.

### Example

```python
squares = {x: x * x for x in range(6)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Set Comprehension

Set comprehension is an elegant and concise way to create a new set from an iterable in Python. Set comprehension consists of an expression followed by a `for` clause inside curly braces `{}`.

### Example

```python
squares = {x * x for x in [1, 1, 2]}
print(squares) # {1, 4}
```

## References

- [Bex T (Medium)](https://towardsdatascience.com/5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it-2b1dd7ef57f3)
- [Coding Dojo: Python Fundamentals](https://www.codingdojo.com)
- [Platzi: Escuela de desarrollo back-end con Python](https://platzi.com/ruta/web-python/)
- [Python Documentation](https://docs.python.org/3/)
  <!-- * [w3schools](https://www.w3schools.com/python/) -->
  <!-- * [Python Tutorial](https://www.tutorialspoint.com/python/index.htm) -->
  <!-- * [Python Tutorial](https://www.programiz.com/python-programming)
- [Python Tutorial](https://www.learnpython.org/) -->
