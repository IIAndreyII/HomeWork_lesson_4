# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

n = input('Введите размер списка: ')

def is_int(k):
    try:
        int(k)
    except:
        print('Введено не корректное число.')
        quit()

is_int(n)
n = int(n)
new_list = []

import random

for i in range(n):
    a = random.randint(0,9)
    new_list.append(a)

print(new_list)

new_list1 = []
for number in new_list:
    count = new_list.count(number)
    if count > 1: continue
    else: new_list1.append(number)

print(new_list1)