from week_7_homework_2_part.class_Customer import Customer
from week_7_homework_2_part.class_Shop_and_UOM import Shop
from week_7_homework_2_part.class_products import Products
import logging

logging.basicConfig(filename='shop.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

if __name__ == '__main__':
    product = Shop([
        Products('Apple',10,10,1),
        Products('Banana',10,10,1),
        Products('Orange',10,10,1)
    ])
    person1 = Customer('Turchyn Andrii', 'Zhitomir, Zamkova, 1, fl.4', 989922947, 995, True)
    y = product.attach_products_to_customer(person1)
