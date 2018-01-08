my_variable = "hello"

for char in my_variable: # iterables are strings, lists, sets, tuples, and more
    print(char)


my_list = [1, 3, 5, 7, 9]

for number in my_list:
    print(number ** 2)

user_wants_number = True

while user_wants_number == True:
    print(10)
    user_input = input("should We print again? (y/n)")
    if user_input == 'n':
        user_wants_number = False