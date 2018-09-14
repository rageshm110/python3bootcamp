import os

os.system("clear")

my_string = "Winner! Winner! Chicken dinner!"
vowel_count = 0
for i in range(len(my_string)):
    char_check = my_string[i].upper()
    if(char_check == 'A' or char_check == 'E' or char_check == 'I' or char_check == 'O' or char_check == 'U'):
        vowel_count += 1
print ("Number of vowles in the string: {0}".format(vowel_count))
