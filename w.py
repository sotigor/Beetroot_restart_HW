# Task 3. Задана программа w.py, которая читает файл weather.log и
# рассчитывает среднюю температуру:
#     f = open('weather.log', 'r', encoding='utf-8')
#     t = f.readlines()
#     f.close()
#     s = 0
#     for i in t:
#         temp_txt = i.split()[2]
#         temp_int = int(temp_txt.replace('°C,',''))
#         s = s + temp_int
#     print(s / len(t))
# Модифицировать ее так, чтобы она считала только температуры сентября (или августа, например).
# При желании - можно выводить сколько было записей за месяц и т.д. - подумайте,
# как можно было бы расширить возможности.

import datetime

def date_converter(date_table):
    date_converted = datetime.datetime(int(date_table.split('-')[0]),
                                       int(date_table.split('-')[1]),
                                       int(date_table.split('-')[2]))
    return date_converted

# Calculate the average temperature and quantity of entries during defined period

first_date = input('Enter the first (origin) date\n'
                   'You should enter your date in format: year-month-day\n'
                   'Like this: 0000-00-00\n\n')
second_date = input('Enter the second date must be later than the first one\n'
                   'You should enter your date in format: year-month-day\n'
                   'Like this: 0000-00-00\n\n')
f = open('weather.log', 'r', encoding='utf-8')
t = f.readlines()
f.close()
s = 0
count = 0
for i in t:
    # print(i)
    if date_converter(first_date)<=date_converter(i.split()[0]) <= date_converter(second_date):
        temp_txt = i.split()[2]
        temp_int = int(temp_txt.replace('°C,', ''))
        s = s + temp_int
        count += 1
if count == 0:
    print(f'Found entries from {first_date} to {second_date}: {count}\n\n')
else:
    print(f'Found entries from {first_date} to {second_date}: {count}\n\n'
          f'The average temperature from {first_date} to {second_date} is: {s / count:.2f} ')



