my_list = [0, 1, 2, 3, 4]
an_equal_list = [x * 2 for x in range(5)]

multiply_list = [x * 3 for x in range(10,30)]
print(multiply_list);

print(8 % 3)

even_list = [n for n in range(10) if n % 2 != 0]
print("Even List: ", even_list)

people_you_know = ["Rolf", " John", "anna", "GREG"]
normalised_people = [person.strip().lower() for person in people_you_know]
print(people_you_know, normalised_people)