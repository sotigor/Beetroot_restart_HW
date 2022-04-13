# Task 1.   Написать программу fio.py, которая создает файл 'fio.txt'
# и записывает туда ваши фамилию, имя, отчество,
# а с нового абзаца - год, месяц и день рождения.

with open('fio.txt', 'w') as fio:
    fio.write('Kosenko Ihor Oleksandrovich \n'
              '1983.09.04')

with open('fio.txt', 'r') as fio:
    print(fio.read())
