from week_7_classwork.CCar import CCar
from week_7_classwork.CPlane import CPlane
from week_7_classwork.CShip import CShip



if __name__ == '__main__':
    car1 = CCar(10000,150,2000)
    ship1 = CShip(500000,70,2019,'Odessa',1050)
    plane1 = CPlane(1000000,960,2020,200,10000)

    vehicles = [car1,ship1,plane1]
    for vehicle in vehicles:
        print(vehicle)