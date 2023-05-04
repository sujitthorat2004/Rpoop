#ass2:Demonstration of different types of inheritance in python

#Single Inheritance - class inherites from only one parent class
#multi-level -inheritance - class inherites from more than one poarent class
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def get_info(self):
        print(f"{self.name} is a {self.species} and is {self.age} years old.")
#the init method initialise the attribute of class
class Mammal(Animal):
    def __init__(self, name, species, age, gestation_period):
        super().__init__(name, species, age)
        self.gestation_period = gestation_period

    def give_birth(self):
        print(f"{self.name} is giving birth with a gestation period of {self.gestation_period} months.")


#super() calls method of parent class
class Reptile(Animal):
    def __init__(self, name, species, age, is_cold_blooded):
        super().__init__(name, species, age)
        self.is_cold_blooded = is_cold_blooded

    def regulate_body_temperature(self):
        if self.is_cold_blooded:
            print(f"{self.name} is regulating its body temperature through basking in the sun.")
        else:
            print(f"{self.name} is regulating its body temperature through sweating and panting.")

class Bird(Animal):
    def __init__(self, name, species, age, wingspan):
        super().__init__(name, species, age)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} meters.")

class MammalWithHorns(Mammal):
    def __init__(self, name, species, age, gestation_period, horn_length):
        super().__init__(name, species, age, gestation_period)
        self.horn_length = horn_length

    def fight(self):
        print(f"{self.name} is fighting with its horns that are {self.horn_length} meters long.")

class ReptileWithShell(Reptile):
    def __init__(self, name, species, age, is_cold_blooded, shell_type):
        super().__init__(name, species, age, is_cold_blooded)
        self.shell_type = shell_type

    def protect(self):
        print(f"{self.name} is using its {self.shell_type} shell to protect itself.")

lion = Mammal("Simba", "lion", 5, 4)
lion.get_info()
lion.give_birth()

print("\n")

turtle = ReptileWithShell("Michelangelo", "turtle", 20, True, "hard")
turtle.get_info()
turtle.regulate_body_temperature()
turtle.protect()

goat = Mammal("Meera","goat",3,0 )
goat.get_info()


# class Vehicle:
#     def __init__(self,name,company):
#         self.name=name
#         self.company = company
#
#     def get_info(self):
#         print(f"{self.name} is of {self.comapny}.")
#
#     print("\n")
#
# bmw = Vehicle("x20","Buggati")
# bmw.get_info()