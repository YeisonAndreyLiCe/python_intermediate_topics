## Decorator (Hight order functions)
In python functions are `first class objects`. This means that functions can be passed as arguments to other functions, and can also be returned from other functions as well. Functions are also able to be defined inside other functions. This is all done to avoid code duplication and to allow programmers to create abstractions. **Decorators are a way to wrap a function**, and add extra functionalities to such a function. `A decorator is a function that takes another function as an argument and returns a function`

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

