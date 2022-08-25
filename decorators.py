# We can use a closure to create a decorator. A decorator is a closure perse
# A decorator is a function that takes another function as an argument and returns a function.
# The decorator function can do some pre- and post-processing of the function it receives as an argument.
# The decorator function can modify the behavior of the function it receives as an argument.
# The decorator function can return a replacement function for the function it receives as an argument.
# The decorator function can return a different function than the function it receives as an argument.
# The decorator function can return the original function it receives as an argument.

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
    return wrapper

def salutation():
    print("Hello")

###############
def upper(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper

@upper
def message(text):
    return f'{text}, you have received a new message.'

if __name__ == '__main__':
    """ say_hello = decorator(salutation)
    say_hello() # --> Something is happening before the function is called \n Hello """

    # A pythonic to use a decorator is to use @ symbol to call the decorator function: sugar syntax
    @decorator
    def salutation():
        print("Hello World")

    salutation()

    #####
    print(message('Valentine'))