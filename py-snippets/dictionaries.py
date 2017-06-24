# Making a dictionary
alien_0 = {'color': 'green', 'points': 5}


# Getting the value associated with a key
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# Getting the value with get()
alien_0 = {'color': 'green'}
alien_color = alien_0.get('color')
alien_points = alien_0.get('points', 0)
print(alien_color)
print(alien_points)


# Adding a key-value pair
alien_0 = {'color': 'green', 'points': 5}
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5
# Adding to an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5


# Modifying values in a dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
# Change the alien's color and point value.
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0)


# Deleting a key-value pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


# Looping through all key-value pairs
# Store people's favorite languages.
fav_languages = {
     'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',
     }
# Show each person's favorite language.
for name, language in fav_languages.items():
    print(name + ": " + language)
# Looping through all the keys
# Show everyone who's taken the survey.
for name in fav_languages.keys():
    print(name)
#Looping through all the values
# Show all the languages that have been chosen.
for language in fav_languages.values():
    print(language)
# Looping through all the keys in order
# Show each person's favorite language, in order by the person's name.
for name in sorted(fav_languages.keys()):
    print(name + ": " + language)


# Finding a dictionary's length
num_responses = len(fav_languages)


# Storing dictionaries in a list
# Start with an empty list.
users = []
# Make a new user, and add them to the list.
new_user = {
 'last': 'fermi',
 'first': 'enrico',
 'username': 'efermi',
 }
users.append(new_user)
# Make another new user, and add them as well.
new_user = {
 'last': 'curie',
 'first': 'marie',
 'username': 'mcurie',
 }
users.append(new_user)
# Show all information about each user.
for user_dict in users:
    for k, v in user_dict.items():
        print(k + ": " + v)
        print("\n")
# You can also define a list of dictionaries directly, without using append():
# Define a list of users, where each user
# is represented by a dictionary.
users = [
 {
 'last': 'fermi',
 'first': 'enrico',
 'username': 'efermi',
 },
 {
 'last': 'curie',
 'first': 'marie',
 'username': 'mcurie',
 },
]
# Show all information about each user.
for user_dict in users:
     for k, v in user_dict.items():
         print(k + ": " + v)
         print("\n")


# Storing lists in a dictionary
# Store multiple languages for each person.
fav_languages = {
     'jen': ['python', 'ruby'],
     'sarah': ['c'],
     'edward': ['ruby', 'go'],
     'phil': ['python', 'haskell'],
}
# Show all responses for each person.
for name, langs in fav_languages.items():
     print(name + ": ")
     for lang in langs:
        print("- " + lang)


# Storing dictionaries in a dictionary
users = {
     'aeinstein': {
     'first': 'albert',
     'last': 'einstein',
     'location': 'princeton',
    },
     'mcurie': {
     'first': 'marie',
     'last': 'curie',
     'location': 'paris',
     },
    }
for username, user_dict in users.items():
    print("\nUsername: " + username)
    full_name = user_dict['first'] + " "
    full_name += user_dict['last']
    location = user_dict['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


# Preserving the order of keys and values
from collections import OrderedDict
# Store each person's languages, keeping
# track of who respoded first.
fav_languages = OrderedDict()
fav_languages['jen'] = ['python', 'ruby']
fav_languages['sarah'] = ['c']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['python', 'haskell']
# Display the results, in the same order they were entered.
for name, langs in fav_languages.items():
     print(name + ":")
     for lang in langs:
         print("- " + lang)


# A million aliens
aliens = []
# Make a million green aliens, worth 5 points
# each. Have them all start in one row.
for alien_num in range(1000000):
    new_alien = {}
    new_alien['color'] = 'green'
    new_alien['points'] = 5
    new_alien['x'] = 20 * alien_num
    new_alien['y'] = 0
    aliens.append(new_alien)
# Prove the list contains a million aliens.
num_aliens = len(aliens)
print("Number of aliens created:")
print(num_aliens)
