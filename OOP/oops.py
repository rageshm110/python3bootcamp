#!/usr/bin/env python

# import modules used here -- sys is a very standard one

import sys

# Class defeinitions
class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # method for getting circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


# Gather our code in a main() function
def main():
    c = Circle()

    print("Radius is:", c.radius)
    print("Area is: ", c.area)
    print("Circumference is: ", c.getCircumference())

if __name__ == '__main__':
    main()