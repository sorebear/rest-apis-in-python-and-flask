def my_method(arg1, arg2):
    return arg1 + arg2

my_method(5, 6)

def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6

def my_list_addition(list_arg):
    return sum(list_arg)

my_long_method(3, 5, 7, 12, 14, 55)

my_list_addition([3, 5, 7, 12, 14, 55])

def addition_simplified(*args):
    return sum(args)

addition_simplified(3, 5, 7, 12, 14, 55)

## Naming Parameters

def named_params(name, location):
    print(name)
    print(location)

# Notice the order of arguments doesn't matter when named
named_params(location="Irvine, CA", name="Wally Baird")

##kwargs

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12, 34, 56, name="Jose", location="UK")

