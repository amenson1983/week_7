class Uom:
  gramm = 1000
  kg = 1

class Shop:
  def __init__(self,shopping_list):
    self.shopping_list = shopping_list

  def print_list(self):
    for i in self.shopping_list:
      print('__________________________')
      print(i)

