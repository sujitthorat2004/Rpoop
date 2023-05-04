#ass0:Finding the area and perimeter of different polygons
import math
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

class Triangle(Polygon):
    def __init__(self, sides):
        super().__init__(sides)

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        super().__init__([length, breadth, length, breadth])

    def area(self):
        return self.length * self.breadth

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class Pentagon(Polygon):
    def __init__(self, side):
        super().__init__([side] * 5)

    def area(self):
        s = sum(self.sides) / 2
        a = self.sides[0]
        return 1/4 * ((4 * a**2) - (self.sides[1]**2)) ** 0.5 * ((4 * a**2) - (self.sides[2]**2)) ** 0.5

class Hexagon(Polygon):
    def __init__(self, side):
        super().__init__([side] * 6)

    def area(self):
        return 3 * (3 ** 0.5) * (self.sides[0] ** 2) / 2

class Heptagon(Polygon):
    def __init__(self, side):
        super().__init__([side] * 7)

    def area(self):
        a = self.sides[0]
        return 7/4 * a**2 * (1 / math.tan(math.pi/7))

class Octagon(Polygon):
    def __init__(self, side):
        super().__init__([side] * 8)

    def area(self):
        a = self.sides[0]
        return 2 * (1 + math.sqrt(2)) * a**2


# create a triangle with sides 3, 4, 5
triangle = Triangle([3, 4, 5])
print(triangle.area()) # output: 6.0
print(triangle.perimeter()) # output: 12

# create a rectangle with length 4 and breadth 5
rectangle = Rectangle(4, 5)
print(rectangle.area()) # output: 20
print(rectangle.perimeter()) # output: 18

# create a square with side 3
square = Square(3)
print(square.area()) # output: 9
print(square.perimeter()) # output: 12

# create a pentagon with side 4
pentagon = Pentagon(4)
print(pentagon.area()) # output: 27.52763840942347
print(pentagon.perimeter()) # output: 20

# create a hexagon with side 6
hexagon = Hexagon(6)
print(hexagon.area()) # output: 93.53074360871938
print(hexagon.perimeter())# output:36

#create a hetagon with side 2
heptagon = Heptagon(2)
print(heptagon.area()) # output:14.535649776006357
print(heptagon.perimeter()) # output:14

#craete a octagon with side 5
octagon = Octagon(5)
print(octagon.area()) # output:120.71067811865474
print(octagon.perimeter()) #output: 40
