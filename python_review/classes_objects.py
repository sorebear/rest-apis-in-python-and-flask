class LotteryPlayer:
    def __init__(self, name):
        self.name = name,
        self.numbers = (5, 9, 12, 3, 1, 21)
    
    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("John")

# print(player_one.name == player_two.name)

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    #By default, self is passed in to methods as the first argument
    def averageGrade(self):
        return sum(self.marks) / len(self.marks)

#Use this when you're not passing in parameters
    @staticmethod 
    def go_to_school():
        print("I'm going to school.")

anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
anna.marks.append(56)
anna.marks.append(33)
anna.marks.append(97)


anna.go_to_school()
rolf.go_to_school()
Student.go_to_school()