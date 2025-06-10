'''
Abstract class - An abstract class is blueprint for other classes. A class that cannot be instantiated on its own.
It is used to define a common interface that all its subclasses must implement.
Like "Template"- you define the structure but leave the details to the subclasses
- It helps to enforce consistency across subclasses
- Provides base methods or attributes
- Requires children to use inherited abstract methods. 
- Help implement polymorphisim and code reusability
- Prevent creating incomplete objects.

To work with abstarct classes we need to import abc(abstract base classes)
'''

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
        
#vehicle = Vehicle() # This will cause type error because an abstract class can't instantiate on its own
'''
In the abstact class we have two methods go, and stop. This two methods has to be implemented in child class vehicle also.
Else it will get failed. 
'''
class Car(Vehicle): # class car must implement all abstract methods
    def go(self):
        print("You drive the car")

    def stop(self):
        print("Stop the car")

car = Car()

car.go()
car.stop()