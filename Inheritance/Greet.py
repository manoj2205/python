'''
Method overloading - Defining multiple methods with the same name but different parameters in the same class.
Python does not support traditional method overloading directly. You cannot define multiple methods with the same name — the last one will overwrite the previous ones.
To simulate overloading in python - follow below example
Use default parameters or *args and **kwargs
'''
class Greet:
    def hello(self,name=None):
        if name:
            print(f'Hello{name}')
        else:
            print("Hello")
g = Greet()
g.hello()
g.hello("Manoj")