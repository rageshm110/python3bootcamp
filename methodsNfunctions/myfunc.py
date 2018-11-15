def myfunc(**kwargs):
    if 'sweet' in kwargs:
        print ("My choice of sweet is {}".format(kwargs['sweet']))
    else:
        print ("I did not find any sweet in here.")

myfunc(fruit='Orange', sweet='chocolate')