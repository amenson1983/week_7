
class Products:
    def __init__(self,description,price,discount,quantity):
        self.quantity = quantity
        self.discount = discount
        self.price = price
        self.description = description
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else: self.__price = None

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        if value > 0:
            self.__discount = value/100
        else:
            self.__discount = None

    def __str__(self):
        return f'Product description: {self.description} \nProduct price: {self.price} \nProduct`s discount: {self.discount} \nQuantity: {self.quantity}'
