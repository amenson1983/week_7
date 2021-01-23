from week_7_classwork.vehicle_class import CVehicle


class CShip(CVehicle):
    def __init__(self, price, speed, year, port, passangers):
        CVehicle.__init__(self, price, speed, year)
        self.port = port
        self.passangers = passangers

    def __str__(self):
        return f"{CVehicle.__str__(self)}, {self.port}, {self.passangers}"