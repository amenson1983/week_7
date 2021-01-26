from week_7_homework_2_part.class_Shop_and_UOM import Shop
from week_7_homework_2_part.class_products import Products

if __name__ == '__main__':
    product = Shop([
        Products('Apple',3.2,15,5),
        Products('Banana',4.4,0,3),
        Products('Orange',6,10,4)
    ])
    product.print_list()