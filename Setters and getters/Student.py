#Now with getters ans setters
class Student(object):
    def __init__(self,name):
        self.__name=name #private variable(with double underscore)

    def get_name(self): #Getter
        return self.__name
    def set_name(self, new_name): #setter
        if new_name !="":
            self.__name=new_name
        else:
            print("Invalid name! Cannot be empty!")

s = Student("Sharath")
print(s.get_name()) # Acess using getter
s.set_name("Rahul") #modifying using setter
print(s.get_name())
s.set_name("")