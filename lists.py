

# LIsts are ordered sequences that can hold a variety of object types
# they use [] and , to separate objects in list
# ex: [1,2,3,4] | ["Ragesh","TechM", 4] | ["Adhik", [2007, 20, 05]]

# lists supports indexing and slicing. Lists can be nested
# and also have a variety of useful methods that can be called
# off of them.

# list of integers
import os

my_list = [1, 2, 3]

#
my_mixed_list = ["string", 300, 5.3]

print(len(my_list))
print(my_list[1:])
print(my_list[::-1])

# lists are mutable data structure
my_list[0] = 4
print(my_list)
my_list.append(5)
print(my_list)

# remove items from the list
my_list.pop() # pop will remove item from back of the list
print("my_list: {0}".format(my_list))

# we can use indexing to pop items from specific locations
my_list.pop(0)
print("my_list: {0}\tHere the first element got removed.".format(my_list))


# sorting a list
my_list_unsorted = [1, 2, 3, 6, 56, 22, 45, 32]
my_list_unsorted.sort()
print("my sorted list: {}".format(my_list_unsorted))

# reverse the list
my_list_unsorted.reverse()
print("my reversed list: {}".format(my_list_unsorted))s