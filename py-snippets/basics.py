
import sys

# Hello world
print("Hello world!")


# Hello world with a variable
msg = "Hello world!"
print(msg)


# Print python version
print(sys.version_info)


# Concatenation (combining strings)
first_name = 'albert'
last_name = 'einstein'
full_name = first_name + ' ' + last_name
print(">>> Concatenation: {}".format(full_name))


# Sort a string characters
str = 'ZENOVW'
str_norted = ''.join(sorted(a))


# Reverse a string
str = 'ZENOVW'
str_norted = str[::-1]


# Split string into words with delimited ":"
test_split = "ciao:mamma lala"
print(test_split.split(':'))


# Make a list
bikes = ['trek', 'redline', 'giant']


# Get the first item in a list
first_bike = bikes[0]


# Get the last item in a list
last_bike = bikes[-1]


# Looping through a list
for bike in bikes:
    print(bike)


# Adding items to a list
bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')
print(">>> Adding items to a list: {}".format(bikes))


# Making numerical lists
squares = []
for x in range(1, 11):
    squares.append(x**2)
print(">>> Making numerical lists: {}".format(squares))


# List comprehensions
squares = [x ** 2 for x in range(1, 11)]
print(">>> List comprehensions: {}".format(squares))


# Slicing a list
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print(">>> Slicing a list: {}".format(first_two))


# Copying a list
copy_of_bikes = bikes[:]


# Making a tuple
dimensions = (1920, 1080)


# A simple dictionary
alien = {'color': 'green', 'points': 5}


# Accessing a value
print("The alien's color is " + alien['color'])


# Adding a new key-value pair
alien['x_position'] = 0


# Looping through all key-value pairs
fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))


# Looping through all keys
fav_numbers = {'eric': 17, 'ever': 4}
for name in fav_numbers.keys():
    print(name + ' loves a number')


# Looping through all the values
fav_numbers = {'eric': 17, 'ever': 4}
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')


# Prompting for a value
name = input("What's your name? ")
print("Hello, " + name + "!")


# Prompting for numerical input
age = input("How old are you? ")
age = int(age)
pi = input("What's the value of pi? ")
pi = float(pi)


# A simple while loop
current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1


# Letting the user choose when to quit
msg = ''
while msg != 'quit':
    msg = input("What's your message? ")
    print(msg)


# A simple function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()


# Passing an argument
def greet_user2(username):
    """Display a personalized greeting."""
    print("Hello, " + username + "!")
greet_user2('jesse')


# Default values for parameters
def make_pizza(topping='bacon'):
    """Make a single-topping pizza."""
    print("Have a " + topping + " pizza!")
make_pizza()
make_pizza('pepperoni')


# Returning a value
def add_numbers(x, y):
    """Add two numbers and return the sum."""
    return x + y
sum = add_numbers(3, 5)
print(sum)


# Creating a dog class
class Dog():
    """Represent a dog."""
    def __init__(self, name):
        """Initialize dog object."""
        self.name = name

    def sit(self):
        """Simulate sitting."""
        print(self.name + " is sitting.")


my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
my_dog.sit()


# Inheritance
class SARDog(Dog):
    def search(self):
        """Simulate searching."""
        print(self.name + " is searching.")


my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()


# Reading a file and storing its lines
filename = 'siddhartha.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)


# Writing to a file
filename = 'journal.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")


# Appending to a file
filename = 'journal.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI love making games.")


# Catching an exception
prompt = "How many tickets do you need? "
num_tickets = input(prompt)
try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Please try again.")
else:
    print("Your tickets are printing.")
