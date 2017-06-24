# Create a list with all chars of a string
test_string = "ciao mamma mia"
output = list(test_string)
print(output)

# Check if an item is in a list
test_list = [1, "ciao", 34, "bella"]
output = 35 in test_list
print(output)

# How many keys/items in a dict ?
test_dict = {23 : "Andrea", 45 : "Paolo"}
output = len(test_dict)
print(output)

# Create a list of all words in a string
test_string = "ciao mamma mia"
output = test_string.split()
print(output)

# Take a bunch or lists - values in a dict - and turn them into a single list
test_dict = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']}
output = []
for value in test_dict.values():
    output += value
print(output)

# Reverse a string
test_string = "Andrea il grande"
output = test_string[::-1]
print(output)

# Check a variable is an instance of a specific type of class
test_var = 1
output = isinstance(test_var, str)
print(output)

# Get nane of a calls
class TestClass: pass
test_intance = TestClass()
print(test_intance.__class__.__name__)

# Swap 2 values
a = 10
b = "ciao"
a, b = b, a
print("{} {}".format(a,b))

# Enumerate and iterable, creating tuples that count the position of each item
test_list = ["andrea", "paolo", "giovanna", "luca"]
output = list(enumerate(test_list))
print(output)

#   Set Opetations
#   Operation	                Equivalent	            Result
#   len(s)      	 	                                number of elements in set s (cardinality)
#   x in s	 	                                        test x for membership in s
#   x not in s	 	                                    test x for non-membership in s
#   s.issubset(t)	            s <= t	                test whether every element in s is in t
#   s.issuperset(t)	            s >= t	                test whether every element in t is in s
#   s.union(t)	                s | t                   new set with elements from both s and t
#   s.intersection(t)	        s & t                   new set with elements common to s and t
#   s.difference(t)            	s - t                   new set with elements in s but not in t
#   s.symmetric_difference(t)	s ^ t	                new set with elements in either s or t but not both
#   s.copy()	 	                                    new set with a shallow copy of s


# Combine 2 enumerable into a list of tuples, every one with the n-th element of each
test_enum1 = [1, 2, 3]
test_enum2 = "AND"
output = []
for index, value in enumerate(test_enum1):
    output.append((value, test_enum2[index]))
print(output)


