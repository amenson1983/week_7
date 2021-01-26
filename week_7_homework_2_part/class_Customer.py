import logging

from week_7_homework_2_part.class_Person import Person_1

logging.basicConfig(filename='person.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class Customer(Person_1):
    def __init__(self,name,adress,phone,id,inlist):
        Person_1.__init__(self,name,adress,phone)
        self.inlist = inlist
        self.id = id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value > 0:
            self.__id = value
            logging.info("Set ID for Person: " + str(value))
        else: self.__id = None


    @property
    def inlist(self):
        return self.__inlist

    @inlist.setter
    def inlist(self, value):
        if value == True:
            self.__inlist = True
            logging.info("Set Person`s agree for receiving mail: " + str(value))
        elif value == False:
            self.__inlist = False
            logging.info("Set Person`s disagree for receiving mail: " + str(value))

    def __str__(self):
        return f"{Person_1.__str__(self)} \n Agree for mail? {self.inlist} \n Customer`s ID: {self.id}"
    def __repr__(self):
        return f"{Person_1.__str__(self)},{self.inlist},{self.id}"

class CustomersWorkout:
    def __init__(self,customers_list):
        self.customers_list = customers_list

    def get_min_id(self):
        min_ = self.customers_list[0]
        for i in self.customers_list:
            if i.id < min_.id:
                min_ = i.id
        return min_

    def print_refuses(self):
        for customer in self.customers_list:
            if customer.inlist == False:
                print('____________________')
                print(customer)

    def print_agrees(self):
        for customer in self.customers_list:
            if customer.inlist == True:
                print('____________________')
                print(customer)

