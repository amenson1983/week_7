from week_7_homework_2_part.class_Employee import Employee


class ShiftChief(Employee):
    def __init__(self,name,id,annual_salary,annual_reward_rate,annual_reward):
        Employee.__init__(self,name,id)
        self.annual_reward_rate = annual_reward_rate
        self.annual_salary = annual_salary
        self.annual_reward = annual_reward

    @property
    def annual_salary(self):
        return self.__annual_salary

    @annual_salary.setter
    def annual_salary(self, value):
        self.__annual_salary = float(value)

    @property
    def annual_reward(self):
        return self.__annual_reward

    @annual_reward.setter
    def annual_reward(self,value):
        self.__annual_reward = value

    def __str__(self):
        return f" Employee name: {self.name} \n Employee ID: {self.id} \n Annual salary: {self.annual_salary} \n Annual reward rate: {self.annual_reward_rate}\n Annual reward amount: {self.annual_reward}"
    def __repr__(self):
        return f"{self.name},{self.id},{self.annual_salary},{self.annual_reward_rate},{self.annual_reward}"