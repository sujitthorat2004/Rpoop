#Finding the area and perimeter of different polygons
import math

#polygon is the base class,so there is need to write only for area ,not for perimeter
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

#'self' is reference to instance of class which has same properties and methoids as same as class but has unique values for these properties 
class Triangle(Polygon):
    def __init__(self, sides):
        super().__init__(sides)

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

# init can initialise the attributes of the class with values given by user. 
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
        return 1.75 * (side[1])*(side[2])*cot(180/7)

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
print(hexagon.perimeter())



# class shapes:
#     def __init __(self,sides):
#         self.sides= sides
    
#     def perimeter(self):
#         return sum(self.sides)
    
# class Traingle(shapes):
#     super().__init__(sides)


#     def area(self):
    #   a,b,c = self.sides
    #   (a+b+c)/2 = s


