# Making a list
users = ['val', 'bob', 'mia', 'ron', 'ned']


# Getting the first element
first_user = users[0]
# Getting the second element
second_user = users[1]
# Getting the last element
newest_user = users[-1]


# Changing an element
users[0] = 'valerie'
users[-2] = 'ronald'


# Adding an element to the end of the list
users.append('amy')
# Starting with an empty list
users = []
users.append('val')
users.append('bob')
users.append('mia')
# Inserting elements at a particular position
users.insert(0, 'joe')
users.insert(3, 'bea')


# Deleting an element by its position
del users[-1]
# Removing an item by its value
users.remove('mia')


# Pop the last item from a list
most_recent_user = users.pop()
print(most_recent_user)
#Pop the first item in a list
first_user = users.pop(0)
print(first_user)


# Find the length of a list
num_users = len(users)
print("We have " + str(num_users) + " users.")


# Sorting a list permanently
users.sort()
#Sorting a list permanently in reverse alphabetical order
users.sort(reverse=True)
# Sorting a list temporarily
print(sorted(users))
print(sorted(users, reverse=True))
# Reversing the order of a list
users.reverse()


# Printing all items in a list
for user in users:
    print(user)
# Printing a message for each item, and a separate message afterwards
for user in users:
    print("Welcome, " + user + "!")
    print("Welcome, we're glad to see you all!")


# Printing the numbers 0 to 1000
for number in range(1001):
    print(number)
# Printing the numbers 1 to 1000
for number in range(1, 1001):
    print(number)
# Making a list of numbers from 1 to a million
numbers = list(range(1, 1000001))


# Finding the minimum value in a list
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)
# Finding the maximum value
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
oldest = max(ages)
# Finding the sum of all values
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
total_years = sum(ages)


# Getting the first three items
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
first_three = finishers[:3]
# Getting the middle three items
middle_three = finishers[1:4]
# Getting the last three items
last_three = finishers[-3:]


# Making a copy of a list
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
copy_of_finishers = finishers[:]


# Using a loop to generate a list of square numbers
squares = []
for x in range(1, 11):
     square = x**2
     squares.append(square)
# Using a comprehension to generate a list of square numbers
squares = [x**2 for x in range(1, 11)]
#Using a loop to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
 upper_names.append(name.upper())
#Using a comprehension to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = [name.upper() for name in names]


# Build a list and print the items in the list
dogs = []
dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')
for dog in dogs:
    print("Hello " + dog + "!")
print("I love these dogs!")
print("\nThese were my first two dogs:")
old_dogs = dogs[:2]
for old_dog in old_dogs:
    print(old_dog)
del dogs[0]
dogs.remove('peso')
print(dogs)