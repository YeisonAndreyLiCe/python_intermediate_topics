# Local scope : local variable
# Global scope :root


# closures : function inside a function

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print(x)
    return inner

my_func = outer()
my_func()
del(outer) # delete the outer function
my_func() # Even though the outer function is deleted, the inner function is still accessible.The nested function has access to the enclosing scope's variables even if they are not present in memory


# A closure is a function object that remembers values in enclosing scopes even when they are not present in memory.

""" In a closure:
    1. A nested function is required
    2. The nested function has access to the enclosing scope
    3. The outer function returns the nested function"""

# we can use a closure in a class with a method to do it in a fancy way.
# we can also use a closure in decorators.

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

time10 = make_multiplier_of(10)# lambda x : x * 10
time5 = make_multiplier_of(5) # lambda x : x * 5

print(time10(3)) # lambda 3 : 3 * 10
print(time5(5)) # lambda 5 : 5 * 10
print(time10(time5(5))) # lambda 5 : 5 * 10 * 5 ; recursive function  lambda x: x * lambda x: x * n

