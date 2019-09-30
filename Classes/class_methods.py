class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):
        return "{} and {}".format(self.x, self.y) 

    def __add__(self, another_point):
        return Point(self.x +another_point.x, self.y +another_point.y)

    def __sub__(self, another_point):
        return Point(self.x-another_point.x, self.y-another_point.y)

    
p1 = Point(2, 3)
p2 = Point(3, 12)
p3 = p1+ p2

print(p1)
print(p3)
print(p1+p2)
print(p1-p2)


