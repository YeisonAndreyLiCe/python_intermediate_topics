# generators are sugar syntax for iterators.

def my_generator():
    
    print("This is the first yield")
    n  = 0
    yield n # yield is a keyword that allows you to return a value from a function, without having to store it in a variable. works like return, but it doesn't stop the function.

    print("This is the second yield")
    n = 1
    yield n

    print("This is the third yield")
    n = 2
    yield n

""" a  = my_generator()
print(next(a))
print(next(a))
print(next(a))
print(next(a)) """


# Generator expressions
# A generator expression is a way to create a generator object.
my_list = [1, 2, 3, 4, 5]
my_generator = (x**2 for x in my_list)
print(my_generator)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
