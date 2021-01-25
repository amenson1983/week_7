from week_7_classwork.vehicle_class import CVehicle


class CCar:
    def __init__(self,price,speed,year):
        CVehicle.__init__(self,price,speed,year)


    def __str__(self):
        return f"{CVehicle.__str__(self)}"
    def __repr__(self):
        return f"{CVehicle.__repr__(self)}"


class CShip:
    def __init__(self, price, speed, year, port, passangers):
        CVehicle.__init__(self, price, speed, year)
        self.port = port
        self.passangers = passangers

    def __str__(self):
        return f"{CVehicle.__str__(self)}, {self.port}, {self.passangers}"
    def __repr__(self):
        return f"{CVehicle.__str__(self)}, {self.port}, {self.passangers}"


class CPlane:
    def __init__(self, price, speed, year,passangers, height):
        CVehicle.__init__(self, price, speed, year)
        self.height = height
        self.passangers = passangers



    def __str__(self):
        return f"{CVehicle.__str__(self)}, {self.height}, {self.passangers}"
    def __repr__(self):
        return f"{CVehicle.__str__(self)}, {self.height}, {self.passangers}"

# 1. +вывести на екран механизм с наибольшей ценой
# 2. +получить механизм с наименьшей ценой
# 3. получить механизм с ценой меньше 16000
# после 2000 года
# 4. получить масив механизмов год
# выпуска с 2000 по 2010
# 5. получить масив механизмов не
# старше 5 лет с средней ценой(+- 20%)
# и скоростью в диапазоне от 100 до 200

class Vehicles:
    def __init__(self, vehicles_):
        self.vehicles_ = vehicles_

    def print_maxprice_vehicle(self):
        max_ = self.vehicles_[0]
        for i in self.vehicles_:
            if i.price > max_.price:
                max_ = i
        for i in self.vehicles_:
            if i.price == max_.price:
                print(i)



    def get_minprice_vehicle(self):
        min_ = self.vehicles_[0]
        for i in self.vehicles_:
            if i.price < min_.price:
                min_ = i.price
        return min_.price

    def get_price_less_after_vehicle(self, less_price=16000, after_year=2000):
        for i in self.vehicles_:
            if i.price < less_price and i.year >= after_year:
                return i

    def get_vehicles_in_range(self, start_year=2000, end_year=2010):
        pass

    def get_vehicles_less_with_aver_price_and_speed_in_range(self,age_year=5,start_speed=100, end_speed=200):
        pass


class Test_Vehicle:
    def test_get_minprice_vehicle(self):
        vehicles = Vehicles(
            [CCar(10000, 150, 1995),
             CShip(500000, 70, 2008, 'Odessa', 1050),
             CPlane(1000000, 960, 2020, 200, 10000),
             CCar(15000, 220, 2001),
             CShip(600000, 80, 2019, 'Chernomorsk', 1200),
             CPlane(800000, 780, 2015, 150, 10000),
             ]
        )
        min_price_exp = 10000
        min_price_act = vehicles.get_minprice_vehicle()
        if min_price_exp == min_price_act:
            print("Correct")
        else:
            print("Error")

    def test_price_less_after_vehicle(self):
        vehicles = Vehicles(
            [CCar(10000, 150, 1995),
             CShip(500000, 70, 2008, 'Odessa', 1050),
             CPlane(1000000, 960, 2020, 200, 10000),
             CCar(15000, 220, 2001),
             CShip(600000, 80, 2019, 'Chernomorsk', 1200),
             CPlane(800000, 780, 2015, 150, 10000),
             ]
        )
        year_exp = 2001
        price_exp = 15000
        veh_ = vehicles.get_price_less_after_vehicle()
        if price_exp == veh_.price and year_exp == veh_.year:
            print("Correct")
        else:
            print("Error")


if __name__ == '__main__':

    car1 = CCar(10000, 150, 1995)
    ship1 = CShip(500000, 70, 2008, 'Odessa', 1050)
    plane1 = CPlane(1000000, 960, 2020, 200, 10000)
    car2 = CCar(15000, 220, 2001)
    ship2 = CShip(600000, 80, 2019, 'Chernomorsk', 1200)
    plane2 = CPlane(800000, 780, 2015, 150, 10000)

    vehicles = [car1,ship1,plane1,car2,ship2,plane2]
    vehicles_ = Vehicles(vehicles)

    min_ = vehicles_.get_minprice_vehicle()
    print(min_)
    Test_Vehicle().test_get_minprice_vehicle()

    vehicles_.print_maxprice_vehicle()
    vehs_ = vehicles_.get_price_less_after_vehicle()
    Test_Vehicle().test_price_less_after_vehicle()
    print(vehs_)

