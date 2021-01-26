from week_7_homework_2_part.class_Customer import Customer, CustomersWorkout
from week_7_homework_2_part.class_Person import Person_1

if __name__ == '__main__':

    list = CustomersWorkout([
        Customer('Turchyn Andrii', 'Zhitomir, Zamkova, 1, fl.4', 989922947, 995, True),
        Customer('Turchyn Sergey', 'Warszaw', 4499322966, 996, False),
        Customer('Turchyn Alexandr', 'Zhitomir, Zamkova, 1, fl.4', 984446669, 997, True),
        Customer('Turchyna Natali', 'Zhitomir, Zamkova, 1, fl.4', 987418476, 998, False),
        Customer('Turchyna Daxi', 'Zhitomir, Zamkova, 1, fl.4', 989922947, 999, False)
    ])
    x = list.get_min_id()
    print('Minimal ID number belongs to: \n', x)
    print('***************************************')
    print('Refused to receive mail: ')
    list.print_refuses()
    print('***************************************')
    print('Agree to receive mail:')
    list.print_agrees()