import logging

logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class Employee:
    def __init__(self,name,id):
        self.id = id
        self.name = name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        logging.info("Set name for Employee: " + str(value))

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = int(value)
        logging.info("Set id for Employee: " + str(value))

    def __str__(self):
        return f" Employee name: {self.name} \n Employee ID: {self.id}"
    def __repr__(self):
        return f"{self.name},{self.id}"