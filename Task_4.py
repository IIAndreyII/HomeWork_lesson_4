# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

indexes = {"0":"\u2070","1":"\u00B9","2":"\u00B2","3":"\u00B3",
"4":"\u2074","5": "\u2075","6":"\u2076","7":"\u2077","8": 
"\u2078","9":"\u2079","-":"\u207B"}

# z = int(input('Введите максимальную степень многочлена: '))
import random

z = 12
d = str(z)


def st(k):
    s = ''
    for i in range(0,len(k)):
        j = k[i]
        
        s = s + indexes[j]
    return s

polynomial = []
for i in range(0,(z)*2):
    a = random.randint(0,100)
    if i%2==0 and a!=0:
        if a!=0:
            polynomial.append(f'{a}x{st(d)} ')
            d = int(d)
            d -= 1
            d = str(d)

            
    elif i%2!=0 and a!=0:
        k = random.randint(0,1)
        if k == 1:
            polynomial.append('+ ')
        elif k == 0:
            polynomial.append('- ')


s = random.randint(0,101)
polynomial.append(f'{s} = 0')

result = (''.join(polynomial))

print(result)


with open('data.txt', 'w',encoding='utf-8') as f:
    f=f.write(f'{result}')



