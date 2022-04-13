# Task 5 (**) Задан файл с зарплатами администрации Белого дома на 2017 год
# формат:
#     NAME;STATUS;SALARY;PAY BASIS;POSITION TITLE
#     имя ; статус ; заработок ; тип контракта ; занимаемая должность
# Статус может быть - Employee служащий, либо Detailee - "временно назначенного на другую должность"
# (за которым сохраняется оклад на прежнем месте).
# С помощью скриптов на питоне определить:
# 1. Кто зарабатывает меньше всего.
# 2. Кто зарабатывает больше всего.
# 3. Средний заработок всех сотрудников.
# 4. Какие 10 сотрудников зарабатывают больше всех.
# 5. Сколько людей временно назначены на другую должность?
# 6. Сколько платят людям из пункта 5?
# 7. Сколько людей в должности "STAFF ASSISTANT"
# 8. Среднюю зарплату всех "STAFF ASSISTANT"
# 9. Есть ли люди, которым не платят зарплату вообще?

salary = []
name = []
status = []
position = []

whouse = open('white_house_2017_salaries_com.csv','r')
whouse.readline()
wh_data = whouse.readlines()
whouse.close()

for line in wh_data:
    salary.append(float(line.split(';')[2].replace('$','').replace(',','')))
    name.append(line.split(';')[0])
    status.append(line.split(';')[1])
    position.append(line.split(';')[4])

# 1,2 Кто зарабатывает меньше и больше всего.
minsalary = []
min_salary = max(salary)
maxsalary = []
max_salary = min(salary)
for item in salary:
# Finding min salary.
    if 0 < item < min_salary:
        min_salary = item
# Finding max salary.
    if item > max_salary:
        max_salary = item
# Finding how many people have the same max and min salary level and who exactly
for index,item in enumerate(salary):
    if item == min_salary:
        minsalary.append(index)
    if item == max_salary:
        maxsalary.append(index)

print(f"\nTwo people {name[minsalary[0]]} and {name[minsalary[1]]} get the minimum salary which is: ${min_salary}\n")
print(f"Only one person {name[maxsalary[0]]} get the maximum salary which is: ${max_salary}\n")

# 3. Средний заработок всех сотрудников.
av_salary = sum(salary)/len(salary)
print(f"The average salary for all co-workers is: {'$' + str(av_salary)}\n\n")

# 4. Какие 10 сотрудников зарабатывают больше всех.
sorted_salary = sorted(zip(salary,name), key = lambda x: x[0], reverse = True)
sorted_salary = sorted_salary[0:10]
print("These are 10 the most paid emloyees:")
for item in sorted_salary:
    print(f"{item[1]} earns: {'$'+str(item[0])}")

# 5. Сколько людей временно назначены на другую должность?

print(f"\n\nThe quantity of people who temporaryly assigned to the position: {status.count('Detailee')}")

# 6. Сколько платят людям временно назначеным на другую должность?

salary_detailee = [salary[index] for index,item in enumerate(status) if item == 'Detailee']

print(f"\nPeople who temporaryly assigned to the position have the following budget: ${sum(salary_detailee)}")

# 7. Сколько людей в должности "STAFF ASSISTANT"

q_position = position.count('STAFF ASSISTANT\n')
print(f"\n\nThe quantity of people who in STAFF ASSISTANT position: {q_position}")

# 8. Среднюю зарплату всех "STAFF ASSISTANT"

salary_position = [salary[index] for index,item in enumerate(position) if item == 'STAFF ASSISTANT\n']
av_salary_position = sum(salary_position)/len(salary_position)

print(f"\nThe average salary for people in STAFF ASSISTANT position is: ${av_salary_position:.2f}")

# 9. Есть ли люди, которым не платят зарплату вообще?

nopaid_people = [name[index] for index, item in enumerate(salary) if item == 0]
print("\n\nPeople who work for free (doesn't get salary for their job) are:")
for item in nopaid_people:
    print(item)


