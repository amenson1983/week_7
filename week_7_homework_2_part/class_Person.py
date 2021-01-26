import logging

logging.basicConfig(filename='person.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class Person_1:
    def __init__(self,name,adress,phone):
        self.phone = phone
        self.adress = adress
        self.name = name
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        #if 100000000<value<1000000000:
            self.__phone = value
            logging.info("Set phone for Person: " + str(value))
        #else: logging.critical('ERROR!! There must be 9 digits in phone number!')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        logging.info("Set name for Person: " + str(value))

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, value):
        self.__adress = value
        logging.info("Set adress for Person: " + str(value))

    def __str__(self):
        return f" Person`s name: {self.name} \n Person`s adress: {self.adress} \n Person`s phone: {self.phone}"
    def __repr__(self):
        return f"{self.name},{self.adress},{self.phone}"