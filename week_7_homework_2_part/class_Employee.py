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

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = int(value)

    def __str__(self):
        return f" Employee name: {self.name} \n Employee ID: {self.id}"
    def __repr__(self):
        return f"{self.name},{self.id}"