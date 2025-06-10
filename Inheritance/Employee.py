'''
super() is a built-in function used in inheritance to call a method from the parent (or superclass).
It's most commonly used to:
1.Reuse code from a parent class (especially __init__)
2.Avoid directly naming the parent class
3.Support multiple inheritance cleanly
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)  # Direct parent call
        self.breed = breed
In methods if you are calling a variable in f string 
name(without self) refers to 
- A local variable or a parameter
- It's only avaialble inside the method where it is defined
self.name referes to 
- A instance variable - it belongs to the object
- You can access it from any method in the class, as long as it's set using self.name =...
'''
class Employee:
    def __init__(self, name, salary):
        print("Employee constructor called")
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary) #calling parent constructer instead of creating
        self.department=department

    def display_info(self):
        super().display_info()
        print(f"Department : {self.department}")

    def __str__(self):
        return f"{self.name} getting {self.salary} salary in {self.department} department"

m1 = Manager("Suriya",25000,'Finance')
print(m1)