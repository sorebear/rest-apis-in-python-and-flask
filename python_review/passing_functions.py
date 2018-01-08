def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

def is_even(x):
    return x % 2 == 0


my_list = [13, 56, 77, 484]
print(list(filter(lambda x: x != 13, my_list)))

print("My Lambda Function: " + str((lambda x: x * 3)(5)))
print("My Filtered List: ")
print(list(filter(is_even, my_list)))

