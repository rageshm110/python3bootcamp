def myfunc(my_string):
    out_str = ''
    my_char = ''
    for i in range(0,len(my_string)):
        if i%2 == 0:
            my_char = my_string[i].upper()
        else:
            my_char = my_string[i].lower()
        out_str += my_char
    return out_str

out = myfunc("This is crazy")
print(out)