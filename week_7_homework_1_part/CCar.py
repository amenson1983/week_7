from week_7_homework_1_part.vehicle_class import CVehicle


class CCar(CVehicle):
    def __init__(self,price,speed,year):
        CVehicle.__init__(self,price,speed,year)

    def __str__(self):
        return f"{CVehicle.__str__(self)}"