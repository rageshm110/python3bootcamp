#!/usr/bin/python

# Fill in the Line class methods to accept coordinates as a pair of
# tuples and return the slope and distance of the line.

class Line():

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (((x1-x2)**2 + (y1-y2)**2)**0.5)

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((y2-y1)/(x2-x1))


def main():
    coor1 = tuple(map(int, input().split()))
    coor2 = tuple(map(int, input().split()))
    line = Line(coor1, coor2)
    print('Distance: {0:.3f}'.format(line.distance()))
    print('Slope: {0:.2f}'.format(line.slope()))

if __name__ == '__main__':
    main()
