import logging
class Uom:
  gramm = 1000
  kg = 1

class Shop:
  def __init__(self,shopping_list):
    self.shopping_list = shopping_list

  def print_list(self):
    for i in self.shopping_list:
      print('********************************')
      print(i)
      logging.info("Printing item: " + str(i))

  def get_total_cost_with_discount(self):
    cost = 0
    for product in self.shopping_list:
      cost += ((product.price-(product.price*product.discount))*product.quantity)
      logging.info("Adding product cost to total cost: " + str(product))
    return cost
