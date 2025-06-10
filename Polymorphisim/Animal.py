'''
Duck typing - Another way to achieve polymorphisim besides Inheritance.
              Object must have the minimum necessary attributes/methods.
              "If it looks like duck and quacks like a duck, it must be a duck.
            but be careful — if a method is missing, it raises a runtime error.
'''
class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print('WOOF!')

class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Car(Animal):
    alive = False


    def speak(self):
        print("HONK!")

animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)