class CVehicle():
    def __init__(self,price,speed,year):
        self.year = year
        self.speed = speed
        self.price = price
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if 1900<value<2022:
            self.__year = value
        else: self.__year = None

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0<value<10000:
            self.__speed = value
        else: self.__speed = None

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
          self.__price = value


    def __str__(self):
        return f"{self.year}, {self.price}, {self.speed}"
    def __repr__(self):
        return f"{self.year}, {self.price}, {self.speed}"