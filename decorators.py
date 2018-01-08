# Decorators is a function run before another function

import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I'm the function!")

my_function()

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func():
            print("Before " + str(number))
            func()
            print("After {}".format(str(number)))
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(45)
def my_function_arguments():
    print("Hello")

my_function_arguments()