from week_7_homework_2_part.class_Employee import Employee
import logging

logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
class ProductWorkerException(Exception):
    def __init__(self, str_err):
        Exception.__init__(self,str_err)


class ProductionWorker(Employee):
    def __init__(self,name,id,shift_num,hour_rate):
        Employee.__init__(self,name,id)
        self.hour_rate = hour_rate
        self.shift_num = shift_num
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        logging.info("Set name for Production Worker: " + str(value))

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
        logging.info("Set id for Production Worker: " + str(value))

    @property
    def hour_rate(self):
        return self.__hour_rate

    @hour_rate.setter
    def hour_rate(self, value):
        if value > 0:
            self.__hour_rate = float(value)
            logging.info("Set hour rate for Production Worker: " + str(value))
        else:
            self.__hour_rate = None
            str_err = "Hour rate error. Value must be positive and higher than nill"
            print(str_err)
            raise ProductWorkerException(str_err)


    @property
    def shift_num(self):
        return self.__shift_num

    @shift_num.setter
    def shift_num(self, value):
        if value in range(1,3):
            self.__shift_num = value
            logging.info("Set shift for Production Worker: " + str(value))
        else:
            self.__shift_num = None
            str_err = "Shift number error. Value must be 1 or 2"
            print(str_err)
            raise ProductWorkerException(str_err)

    def __str__(self):
        return f" Employee name: {self.name} \n Employee ID: {self.id} \n Shift number: {self.shift_num} \n Rate per hour: {self.hour_rate}"
    def __repr__(self):
        return f"{self.name},{self.id},{self.shift_num},{self.hour_rate}"