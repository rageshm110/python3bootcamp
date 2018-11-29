#!/usr/bin/python3

# Cylinder Volume and Sirface Area

class Cylinder():

    def __init__(self, radius, height):
        self.pi = 3.14
        self.radius = radius
        self.height = height
    
    def volume(self):
        return (self.pi * (self.radius**2) * self.height)

    def surface_area(self):
        return(2 * self.pi * self.radius * (self.radius + self.height))

def main():
    radius, height = map(int, input().split())

    cylinder = Cylinder(radius, height)

    print('Volume of cylinder: {0:.2f}'.format(cylinder.volume()))
    print('Surface area of cylinder: {0:.2f}'.format(cylinder.surface_area()))

if __name__ == '__main__':
    main()
