# #ass0:Finding the area and perimeter of different polygons
# import math
# class Polygon:
#     def __init__(self, sides):
#         self.sides = sides

#     def perimeter(self):
#         return sum(self.sides)

# class Triangle(Polygon):
#     def __init__(self, sides):
#         super().__init__(sides)

#     def area(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         return (s*(s-a)*(s-b)*(s-c)) ** 0.5

# class Rectangle(Polygon):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#         super().__init__([length, breadth, length, breadth])

#     def area(self):
#         return self.length * self.breadth

# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)

# class Pentagon(Polygon):
#     def __init__(self, side):
#         super().__init__([side] * 5)

#     def area(self):
#         s = sum(self.sides) / 2
#         a = self.sides[0]
#         return 1/4 * ((4 * a**2) - (self.sides[1]**2)) ** 0.5 * ((4 * a**2) - (self.sides[2]**2)) ** 0.5

# class Hexagon(Polygon):
#     def __init__(self, side):
#         super().__init__([side] * 6)

#     def area(self):
#         return 3 * (3 ** 0.5) * (self.sides[0] ** 2) / 2

# class Heptagon(Polygon):
#     def __init__(self, side):
#         super().__init__([side] * 7)

#     def area(self):
#         a = self.sides[0]
#         return 7/4 * a**2 * (1 / math.tan(math.pi/7))

# class Octagon(Polygon):
#     def __init__(self, side):
#         super().__init__([side] * 8)

#     def area(self):
#         a = self.sides[0]
#         return 2 * (1 + math.sqrt(2)) * a**2


# # # create a triangle with sides 3, 4, 5
# # triangle = Triangle([3, 4, 5])
# # print(triangle.area()) # output: 6.0
# # print(triangle.perimeter()) # output: 12

# # # create a rectangle with length 4 and breadth 5
# # rectangle = Rectangle(4, 5)
# # print(rectangle.area()) # output: 20
# # print(rectangle.perimeter()) # output: 18

# # # create a square with side 3
# # square = Square(3)
# # print(square.area()) # output: 9
# # print(square.perimeter()) # output: 12

# # # create a pentagon with side 4
# # pentagon = Pentagon(4)
# # print(pentagon.area()) # output: 27.52763840942347
# # print(pentagon.perimeter()) # output: 20

# # # create a hexagon with side 6
# # hexagon = Hexagon(6)
# # print(hexagon.area()) # output: 93.53074360871938
# # print(hexagon.perimeter())# output:36

# # #create a hetagon with side 2
# # heptagon = Heptagon(2)
# # print(heptagon.area()) # output:14.535649776006357
# # print(heptagon.perimeter()) # output:14

# # #craete a octagon with side 5
# # octagon = Octagon(5)
# # print(octagon.area()) # output:120.71067811865474
# # print(octagon.perimeter()) #output: 40



# while True:
#     num_sides = int(input("Enter number of sides (3-8) for the polygon: "))
#     if num_sides < 3 or num_sides > 8:
#         print("Invalid input, please enter a number between 3 and 8.")
#         continue

#     # side_length = float(input("Enter the length of each side of the polygon: "))
#     # if side_length <= 0:
#     #     print("Invalid input, side length must be positive.")
#     #     continue

#     # if num_sides == 3:
#     #     polygon = Triangle([side_length] * 3)
#     if num_sides == 3:
#         while True:
#             a = float(input("Enter the length of side a of the triangle: "))
#             b = float(input("Enter the length of side b of the triangle: "))
#             c = float(input("Enter the length of side c of the triangle: "))
#             if a + b <= c or a + c <= b or b + c <= a:
#                 print("Invalid input, sides do not form a valid triangle.")
#             else:
#                 polygon = Triangle([a, b, c])
#                 break
#     elif num_sides == 4:
#         polygon = Rectangle(side_length, side_length)
#     elif num_sides == 5:
#         polygon = Pentagon(side_length)
#     elif num_sides == 6:
#         polygon = Hexagon(side_length)
#     elif num_sides == 7:
#         polygon = Heptagon(side_length)
#     else:
#         polygon = Octagon(side_length)

    # while True:
    #     calculation_type = input("Enter 'a' to calculate area, 'p' to calculate perimeter, or 'q' to quit: ")
    #     if calculation_type == 'a':
    #         print(f"The area of the {num_sides}-sided polygon is {polygon.area():.2f}.")
    #     elif calculation_type == 'p':
    #         print(f"The perimeter of the {num_sides}-sided polygon is {polygon.perimeter():.2f}.")
    #     elif calculation_type == 'q':
    #         break
    #     else:
    #         print("Invalid input, please enter 'a', 'p', or 'q'.")
            
    # exit_choice = input("Enter 'y' to enter a new polygon or any other key to quit: ")
    # if exit_choice != 'y':
    #     break






























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
    def __init__(self, length):
        self.length = length
        super().__init__([length] * 4)

    def area(self):
        return self.length ** 2

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side)

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

while True:
    num_sides = int(input("Enter number of sides (3-8) for the polygon: "))
    if num_sides < 3 or num_sides > 8:
        print("Invalid input, please enter a number between 3 and 8.")
        continue

    if num_sides == 3:
        a = float(input("Enter the length of side 1: "))
        b = float(input("Enter the length of side 2: "))
        c = float(input("Enter the length of side 3: "))
        polygon = Triangle([a, b, c])
    else:
        side_length = float(input("Enter the length of each side of the polygon: "))
        if side_length <= 0:
            print("Invalid input, side length must be positive.")
            continue

        if num_sides == 4:
            polygon = Rectangle(side_length)
        elif num_sides == 5:
            polygon = Pentagon(side_length)
        elif num_sides == 6:
            polygon = Hexagon(side_length)
        elif num_sides == 7:
            polygon = Heptagon(side_length)
        else:
            polygon = Octagon(side_length)

    while True:
        calculation_type = input("Enter 'a' to calculate area, 'p' to calculate perimeter, or 'q' to quit: ")
        if calculation_type == 'a':
            print(f"The area of the {num_sides}-sided polygon is {polygon.area():.2f}.")
        elif calculation_type == 'p':
            print(f"The perimeter of the {num_sides}-sided polygon is {polygon.perimeter():.2f}.")
        elif calculation_type == 'q':
            break
        else:
            print("Invalid input, please enter 'a', 'p', or 'q'.")
            
    exit_choice = input("Enter 'y' to enter a new polygon or any other key to quit: ")
    if exit_choice != 'y':
        break
