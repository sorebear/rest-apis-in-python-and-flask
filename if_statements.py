# should_continue = True
# if should_continue:
#     print("Hello")

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")

# if person in known_people:
#     print("You know {}!".format(person))
# else:
#     print("You don't know {}".format(person))

## Exercise

def who_do_you_know():
    # Ask the user for a list of people they know
    people_list = input("Enter people you know, seperated by commas: ")
    
    # Split the string into a list
    people_array = [person.strip() for person in people_list.split(",")]

    # Return that list
    print(people_array)
    return people_array


def ask_user(people_you_know):
    # Ask user for a name
    person_you_know = input("Enter one person you know: ")

    # See if their name is in the list of people they know
    if person_you_know in people_you_know:
        print("Hey, you do know {}".format(person_you_know))
    else:
        print("No, you don't know {}".format(person_you_know))

array = who_do_you_know()
ask_user(array)