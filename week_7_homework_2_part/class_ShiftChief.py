from week_7_homework_2_part.class_Employee import Employee
import logging

logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class ShiftChief(Employee):
    def __init__(self,name,id,annual_salary,annual_reward):
        Employee.__init__(self,name,id)
        self.annual_salary = annual_salary
        self.annual_reward = annual_reward

    @property
    def annual_salary(self):
        return self.__annual_salary

    @annual_salary.setter
    def annual_salary(self, value):
        self.__annual_salary = float(value)
        logging.info("Set annual salary for ShiftChief: " + str(value))

    @property
    def annual_reward(self):
        return self.__annual_reward

    @annual_reward.setter
    def annual_reward(self,value):
        self.__annual_reward = value
        logging.info("Set annual reward for ShiftChief: " + str(value))

    def __str__(self):
        return f" Employee name: {self.name} \n Employee ID: {self.id} \n Annual salary: {self.annual_salary} \n Annual reward amount: {self.annual_reward}"
    def __repr__(self):
        return f"{self.name},{self.id},{self.annual_salary},{self.annual_reward}"