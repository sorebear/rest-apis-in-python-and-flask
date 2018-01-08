## Dictionaries are like Javascript Objects without Methods

my_set = {1, 3, 5}
my_dict = { 
    'name': 'Jose', 
    'age': 90, 
    'grades': [13, 45, 66, 90]
}

lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 45, 66, 23, 22) #This is a Tuple
}

universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

print(sum(lottery_player['numbers']))