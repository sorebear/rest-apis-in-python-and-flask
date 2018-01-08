a = 5
b = 10
my_variable = 56
any_variable_name = 10

string_variable = "hello"
single_quotes = 'strings can have single quotes'
double_quotes = "they can also have double quotes"

# print(my_variable)
# print(string_variable)
# print("hello, world!")
# print(123)

##

def myPrintMethod(name):
    print("Hello " + name)
    print(name)

myPrintMethod("Caitlin")

def my_multiply_method(number_one, number_two):
    return number_one * number_two

def square_it(number):
    return number * number

result = my_multiply_method(5,5)

print(result)
print("4 Squared is:", square_it(4))