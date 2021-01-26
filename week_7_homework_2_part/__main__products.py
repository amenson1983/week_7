from week_7_homework_2_part.class_Customer import Customer
from week_7_homework_2_part.class_Shop_and_UOM import Shop
from week_7_homework_2_part.class_products import Products
import logging

logging.basicConfig(filename='shop.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

if __name__ == '__main__':
    product = Shop([
        Products('Apple',3.2,15,5),
        Products('Banana',4.9,10,3),
        Products('Orange',6,10,4)
    ])
    person1 = Customer('Turchyn Andrii', 'Zhitomir, Zamkova, 1, fl.4', 989922947, 995, True)
    x = product.get_total_cost_with_discount()
    logging.info("Printing list of bought items: " + str(x))

    y = product.attach_products_to_customer(person1)
