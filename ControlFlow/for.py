import os
os.system("clear")

my_iterable = [1, 2, 3]
for each_item in my_iterable:
    print("{}".format(each_item))

print("*" * 10)
my_list = list(range(0, 10, 1))
print("{}".format(my_list))

for each_item in my_list:
    if (each_item % 2 == 0):
        print ("{}".format(each_item))
    else:
        print("Odd Number: {}".format(each_item))

# tuple unpacking
my_tup_list = [(1,2), (3,4), (5, 6), (7, 8)]
for (a, b) in my_tup_list:
    print ("{}".format(a))
    print("{}".format(b))
