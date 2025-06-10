'''
Inheritance is a core concept in Object-Oriented Programming (OOP). It allows a child class to reuse, extend, or override features (methods and attributes) from a parent class.
Case 1: Parent class expects an argument:
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # ✅ Correct: passing required 'name'
        self.breed = breed
Case 2: Parent class has no parameters
class Animal:
    def __init__(self):
        print("Animal created")
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()  # ✅ Correct: no arguments needed
        self.breed = breed
'''
class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    pass
class Parrot(Animal):
    pass
class Hawk(Animal):
    pass

class Tiger(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed=breed

rabbit = Rabbit()
parrot = Parrot()
hawk = Hawk()
print(hawk.eat())
