from week_7_homework_2_part.class_Customer import Customer, CustomersWorkout
from week_7_homework_2_part.class_Person import Person_1

if __name__ == '__main__':

    person1 = Customer('Turchyn Andrii','Zhitomir, Zamkova, 1, fl.4',989922947,995,True)
    person2 = Customer('Turchyn Sergey', 'Warszaw', 4499322966, 996, False)
    person3 = Customer('Turchyn Alexandr', 'Zhitomir, Zamkova, 1, fl.4', 984446669, 997, True)
    person4 = Customer('Turchyna Natali', 'Zhitomir, Zamkova, 1, fl.4', 987418476, 998, False)
    person5 = Customer('Turchyna Daxi', 'Zhitomir, Zamkova, 1, fl.4', 989922947, 999, False)
    list = CustomersWorkout([
        Customer('Turchyn Andrii', 'Zhitomir, Zamkova, 1, fl.4', 989922947, 995, True),
        Customer('Turchyn Sergey', 'Warszaw', 4499322966, 996, False),
        Customer('Turchyn Alexandr', 'Zhitomir, Zamkova, 1, fl.4', 984446669, 997, True),
        Customer('Turchyna Natali', 'Zhitomir, Zamkova, 1, fl.4', 987418476, 998, False),
        Customer('Turchyna Daxi', 'Zhitomir, Zamkova, 1, fl.4', 989922947, 999, False)
    ])
    x = list.get_min_id()
    #list.print_refuses()
    #list.print_agrees()
    print(x)