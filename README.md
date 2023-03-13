## Scope
Scopes are the contexts in which names are looked up. There are three different scopes in Python: `local`, `enclosing`, `global`, and `built-in`. The scope of a name defines the area of the program where you can unambiguously access that name, such as variables, functions, objects, and so on. The scope of a name is determined by the place where it is declared. Names that are declared outside of all functions are in the `global` scope. This means that those names can be accessed inside or outside of functions. Names that are declared inside a function are in the `local` scope, and can only be accessed inside that function. The `enclosing` scope is a special scope that only exists for nested functions. If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. The `built-in` scope is the outermost scope in Python, and it is the scope that contains all of the built-in names in Python. The built-in scope is searched last, after the local, enclosing, and global scopes (LEGB).

## Example Local Scope
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

## Example Global Scope
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

## Example Enclosing Scope
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

## Example Global Scope Only-read
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

## Example Keyword `global`
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

## Built-in Scope
This are the names in the pre-defined built-in modules. These are always available in your Python programs. You can see the list of built-in names by typing `dir(__builtins__)` in the Python interpreter.

---

In python functions are `first class objects`. This means that functions can be passed as arguments to other functions, and can also be returned from other functions as well. Functions are also able to be defined inside other functions. This is all done to avoid code duplication and to allow programmers to create abstractions.

## Clousures
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

## Decorators (Hight order functions)
 **Decorators are a way to wrap a function**, and add extra functionalities to such a function. `A decorator is a function that takes another function as an argument and returns a function`

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
### Example 2 (Pythonic way -  sugar syntax @)
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
def upper(func: callable) -> callable:
    def wrapper(text: str) -> str:
        return func(text).upper()
    return wrapper

@upper
def message(text: str):
    return f'{text}, you have received a new message.'

print(message('John'))
```

Output:
```output
JOHN, YOU HAVE RECEIVED A NEW MESSAGE.
```

### Example 4 (Decorators with arguments) from (towardsdatascience.com/5-signs-youve-become-an-advanced-pythonista-without-even-realizing-it-2b1dd7ef57f3)

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
This is kinda like a cache (`memoization`), so that the function doesn't have to be called again if the arguments are the same.

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
```

## Example 2 (Fibonacci sequence)
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

## Encapsulation in Python
Encapsulation is the process of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. In Python, we denote private attributes using underscore as the prefix i.e single “ _ “ or double “ __ “. Single _ underscore is used by convention to avoid conflicts with subclasses. Double __ underscore is used to avoid conflicts with subclasses and naming conflicts in general.

### Example
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
red_car._Car__updateSoftware() # This is the way to access 'private' methods

```

Output:
```output
updating software
driving
updating software
```
## class property(fget=None, fset=None, fdel=None, doc=None)
This built-in function is a `factory function` that returns a property attribute. The property attribute has three methods, `fget()`, `fset()`, and `fdel()`. fget() is for getting a value of the attribute, fset() is for setting a value of the attribute, and fdel() is for deleting the attribute value. The doc argument is a string (like a comment).

### [Example from python docs](https://docs.python.org/3/library/functions.html?highlight=property#property "python docs")

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

## @property decorator
- `__init__` : This is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.
- `__str__` : This is a special method, which is used to print the "informal" or nicely printable string representation of an object.
- `__repr__` : This is a special method, which is used to print the "official" string representation of an object.
- `__del__` : This is a special method, which is called when an object gets destroyed. You normally do not call this method yourself, it is called internally by Python when the object is no longer needed.

### Example
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

## @classmethod and @staticmethod
The `@classmethod` and `@staticmethod` are built-in decorators in Python. They are used to define methods in a class. The difference between a `@classmethod` and a `@staticmethod` is:

### @staticmethod
A static method does not receive an implicit first argument. To declare a static method, use this idiom:

```python
class Class:
    @staticmethod
    def function(arg1, arg2, ...):
        ...
```

Static methods in Python are similar to those found in Java or C++. For compatibility reasons, a class method called `f` is treated as a static method if it is defined like this:

```python
class Class:
    def function(arg1, arg2, ...):
        ...
```
Static methods can be called either on the class (such as `C.f()`) or on an instance (such as `C().f()`). They cannot modify object state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.

```python
def regular_function():
    ...

class Class:
    method = staticmethod(regular_function)
```

### @classmethod
A classmethod receives the class as an implicit first argument.

To declare a class method, use this idiom:

```python
class Class:
    @classmethod
    def function(cls, arg1, arg2, ...): # cls is the class just like self is the instance
        ...
```

## Inheritance

### Example
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

## Multiple Inheritance
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

## Let's see a practical example of multiple inheritance
```python
class Person:
    def __init__(self, name: str, age: int, id_number: int):
        self.name: str = name
        self.age: int = age
        self.__id_number: int = 12345

    @property
    def id_number(self) -> int:
        return self.__id_number

    @id_number.setter
    def id_number(self, value: int) -> None:
        if value < 0:
            raise ValueError('ID number cannot be negative')
        if isinstance(value, int):
            self.__id_number = value
        else:
            raise TypeError('ID number must be an integer')

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError('Age cannot be negative')
        if isinstance(value, int):
            self.__age = value
        else:
            raise TypeError('Age must be an integer')
    
    def display(self) -> None:
        print(f'Name: {self.name}, Age: {self.age}')
    

class Student(Person):
    def __init__(self, name: str, age: int, id_number: int, marks: list):
        super().__init__(name, age, id_number)
        self.marks: list = marks

    def calculate(self) -> float:
        try:
            return sum(self.marks) / len(self.marks)
        except ZeroDivisionError:
            return 0

    
class Programmer(Person, Student):
    def __init__(self, name: str, age: int, id_number: int, marks: list, languages: list):
        super().__init__(name, age, id_number)
        self.languages: list = languages

    def display(self) -> None:
        print(f'Name: {self.name}, Age: {self.age}, Languages: {self.languages}')


p1 = Programmer('John', 20, 12345, [90, 95, 85, 80], ['Python', 'C++'])

p1.display()
```

Output:
```output
Name: John, Age: 20, Languages: ['Python', 'C++']
```

## Polymorphism
Polymorphism is an ability (in OOP) to use a common `interface` for multiple forms (data types).

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


