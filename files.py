import os

os.system("clear")

file_dir = os.path.dirname(__file__)
rel_path = "myfile.txt"
#myfile = open('WorkFolder/myfile.txt')
#print("{}".format(myfile.read()))
abs_file_path = os.path.join(file_dir, rel_path)
#print("{}".format(abs_file_path))
#os.system("dir")

# myfile = open(abs_file_path)
# print("{}".format(myfile.read()))
# print("{}".format(myfile.read()))
# once the file is read the curser gets into end of file
# and in this case the second read wont return any data.
# inorder to read the file again we need to reset the curser.
# .seek(0)

# myfile.seek(0)
# print("{}".format(myfile.read()))
# myfile.seek(0)
# print("{}".format(myfile.readlines()))
# myfile.close()

# with open(abs_file_path, mode='r+') as my_new_file:
#     contents = my_new_file.read()
#     my_new_file.write("\nAn extra line. with new line\n")

# creating a file
with open('CreateAFile.txt', mode = 'a+') as godknows:
    godknows.write("I created this file.")

with open('CreateAFile.txt', mode = 'r') as gdf:
    print("{}".format(gdf.read()))
    print("-" * 10)

with open('CreateAFile.txt', mode = 'a') as ap:
    for i in range(10):
        ap.write("\nThis is line {}".format(i))
        i += 1

with open("CreateAFile.txt", mode = 'r') as re:
    print("{}".format(re.read()))