#using with @property to define it in cleaner way
# if you use @proiperty, then the method name must match the attribute name that you want to use like a property
class stud:
    def __init__(self,name):
        self.__name = name
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value:
            self.__name=value
        else:
            raise ValueError("Name cannot be empty")
        
s=stud("Sharath")
print(s.name)
s.name ="Amit"
print(s.name)