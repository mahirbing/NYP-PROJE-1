# Models/product.py

from datetime import datetime

class Product:
    def __init__(self, name="Unknown", price=0, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"Product created: {self.name} - Date: {datetime.now()}")

    # name özelliği için getter ve setter
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if 3 <= len(value) <= 8:
            self._name = value
        else:
            raise ValueError("Name must be between 3 and 8 characters.")

    # price özelliği için getter ve setter
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price must be 0 or more.")

    # quantity özelliği için getter ve setter
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value >= 1:
            self._quantity = value
        else:
            raise ValueError("Quantity must be 1 or more.")

    def get_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
