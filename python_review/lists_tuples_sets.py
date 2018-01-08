my_variable = "hello"

list_grades = [77, 80, 90] # allows you to add or remove elements
tuple_grades = (77, 80, 90) # immutable
set_grades = {77, 80, 90} # unique & unordered

set_grades.add(60)
set_grades.add(60)

## Set Operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9}

#print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print({1, 2, 3, 4}.difference({1, 2}))