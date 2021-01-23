from week_7_classwork.CShip import CShip
from week_7_classwork.vehicle_class import CVehicle


class CPlane(CShip):
    def __init__(self, price, speed, year,passangers, height):
        CVehicle.__init__(self, price, speed, year)
        self.height = height
        self.passangers = passangers

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if 0 < value < 10000:
            self.__height = value
        else:
            self.__height = None

    def __str__(self):
        return f"{CVehicle.__str__(self)}, {self.height}, {self.passangers}"