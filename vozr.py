# Task 2. Написать программу vozr.py, которая читает файл 'fio.txt',
# выделяет в нем имя и год рождения, вычисляет возраст (разность 2022 - год рождения)
# и печатает сообщение "Добрый день <имя>! Ваш возраст <возраст> лет!"

with open('fio.txt', 'r') as fio:
    parsed_line1 = fio.readline().split()[1]
    parsed_line2 = fio.readline().split('.')[0]
    print(f'Добрый день {parsed_line1}! Ваш возраст {2022 - int(parsed_line2)} лет!')
