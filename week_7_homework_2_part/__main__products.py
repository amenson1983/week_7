from week_7_homework_2_part.class_Shop_and_UOM import Shop
from week_7_homework_2_part.class_products import Products
import logging

logging.basicConfig(filename='shop.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

if __name__ == '__main__':
    product = Shop([
        Products('Apple',3.2,15,5),
        Products('Banana',4.4,10,3),
        Products('Orange',6,10,4)
    ])
    x = product.get_total_cost_with_discount()
    logging.info("Printing list of bought items: " + str(x))
    product.print_list()
    print('********************************')
    print('Total cost:',float(x))