tickets = int(input("Введите необходимое вам количество билетов: "))
visitor = tickets

cost = 0
visitor = 1
while visitor <= tickets:
    age_of_visitor = int(input(f'Укажите для какого возраста приобретается билет № {visitor} ? '))
    if age_of_visitor < 18:
        print('Билет будет бесплатный')
    elif 25 > age_of_visitor >= 18:
        cost += 990
        print('Стоимость билета будет 990 руб.')
    else:
        cost += 1390
        print('Стоимость билета будет 1390 руб.')
    visitor += 1

if tickets > 3:
    sale = cost - (cost * 0.1)
    print(f'Итого к оплате {sale} руб., с применением 10%-ой скидки за покупку более 3 билетов')
else:
    print(f'Итого к оплате {cost} руб.')
visitor += 1
