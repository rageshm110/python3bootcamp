#def square(num):
#    return num**2

#my_nums = [1, 2, 3, 4, 5]


#map(square, my_nums)


#for item in map(square, my_nums):
#    print(item)

def check_even(num):
    return num % 2 == 0

my_nums = [1, 2, 3, 4]

print(list(filter(check_even, my_nums)))