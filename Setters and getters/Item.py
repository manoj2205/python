#setter without changing functionality (just assign)
class Item:
    def __init__(self,price):
        self.__price=price

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value): #No Validation, just assignment
        self.__price = value

#The above class is same as like 
item = Item(100)
item.price =150 #just assign value
print(item.price)

# Setter with extra functionality (validation)
class Item:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Price must be positive")
        
item = Item(100)
# item.price = -50     # ❌ will raise error