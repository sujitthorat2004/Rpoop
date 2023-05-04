#ass3: Demonstration of compile time polymorphism(overloading) and run time polymorphism(overiding)
#Compile-time polymorphism (Method of Overloading)is achieved through method overloading, where multiple methods can have the same name with different parameters. When the code is compiled, the correct method is selected based on the number, type, and order of the arguments passed to it
class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def calculate_area(self, length, breadth):
        return length * breadth


class Circle(Shape):
    def calculate_area(self, radius):
        return 3.14 * radius ** 2

r = Rectangle()
print("Area of rectangle with length 4 and breadth 3:", r.calculate_area(4, 3))

c = Circle()
print("Area of circle with radius 5:", c.calculate_area(5))

#Runtime Polymorpohism(Method of Overiding):a child class in python inherits member functions and member variables from its parent class. And if we feel that the implementation of the parent class method is not relevant, then we can override that method in the child class.
class Animal:
    def speak(self):
        print("The animal speaks")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")

def animal_speak(animal):
    animal.speak()

d = Dog()
c = Cat()

animal_speak(d) # This will call the speak method in the Dog class
animal_speak(c) # This will call the speak method in the Cat class


# class shape:
#     def calculate_area(self):
#         pass
# class rectangle(shape):
#     def claculate_area(self,length,breadth):
#         return length*breadth
# p=rectangle()
# print("area of rectangel with length 2 and breadth 3 is:",p.calculate_area(2,3))