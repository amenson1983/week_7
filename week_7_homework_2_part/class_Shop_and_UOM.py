import logging
logging.basicConfig(filename='shop.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')




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

  def attach_products_to_customer(self,customer):
    bill = [customer.id,customer.name,customer.phone,customer.adress,self.shopping_list,self.get_total_cost_with_discount()]
    print('Name of Customer:',customer.name,'\n',
          'Phone +380:', customer.phone, '\n',
          'Adress of Customer:', customer.adress, '\n',
          'The Bill:'
          )
    logging.info("Printing customer data on bill...")
    for i in self.shopping_list:
      print('*************************************')
      print(i)
      logging.info("Printing products...")
    print('*************************************')
    print('*************************************')
    print('Total cost with discount: ', self.get_total_cost_with_discount())
    logging.info("Printing total cost with discount..." + str(self.get_total_cost_with_discount()))
    return bill