# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = input('Введите натуральное число: ' )

try:
    int(n)
except:
    print('Введено не корректное число.')
    quit()

c = n
i = 2 # первый простой множитель
list1 = []
n = int(n)

while i <= n:
    if n % i == 0:
        list1.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {c} приведены в списке: {list1}")