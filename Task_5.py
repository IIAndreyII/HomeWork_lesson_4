# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0

indexes_1 = {"0":"\u2070","1":"\u00B9","2":"\u00B2","3":"\u00B3",
"4":"\u2074","5": "\u2075","6":"\u2076","7":"\u2077","8": 
"\u2078","9":"\u2079","-":"\u207B"}

indexes = {"\u2070":"0","\u00B9":"1","\u00B2":"2","\u00B3":"3",
"\u2074":"4","\u2075":"5","\u2076":"6",
"\u2077":"7","\u2078":"8","\u2079":"9"}

with open('data.txt', 'r',encoding='utf-8') as f:
    data = (f.readline())
    
with open('file.txt', 'r',encoding='utf-8') as f:
    file = (f.readline())

print(data)    
print(file)

data_list = data.split(' ')
file_list = file.split(' ')

def new_list(list_1):           # Разбиваем выражение на одночлены вида ['+20x⁵', '-16x³'].
    list_2 = []                 # И создаём список одночленов выражения.
    a = list_1[0]
    list_2.append(a)

    for i in range(1,len(list_1)):
        if i%2!=0:
            c = ';'
            list_2.append(c)
        else:
            c = list_1[i-1]+list_1[i]
            list_2.append(c)

    res = (''.join(list_2))
    list_2 = res.split(';')
    del list_2[-1]
    return list_2

data_list_1 = new_list(data_list)
file_list_1 = new_list(file_list)

def new_list_1(list_3):
    res_list = []
    for i in range(0,len(list_3)):     # Составляем список вида [ ['+42', '¹¹'], ['+93', '¹⁰']] из чисел и степеней.
        res = (''.join(list_3[i]))     
        res_2 = res.split('x')
        res_list.append(res_2)

    for i in range(0,len(res_list)):

        if len(res_list[i])>1 and len(res_list[i][-1])>1:   # Переводим вид степеней из '¹²' в '12'
            c = res_list[i][-1]
            cl = ''
            
            for b in range(0,len(c)):
                
                g = indexes[c[b]]
                cl += g
                res_list[i][-1] = (cl)

        if len(res_list[i])==1:
            res_list[i][-1] = res_list[i][-1]

        if len(res_list[i])>1 and len(res_list[i][-1])==1:
            res_list[i][-1] = (indexes[res_list[i][-1]])

    n_list = []
    for i in range(0,len(res_list)):  # Приводим список к виду ['+47', '9', '+95', '8', '+32', '7']
        n_list += res_list[i]

    for i in range(1,len(n_list),2):  # Приводим список к виду ['+47', 9, '+95', 8, '+32', 7]
        n_list[i] = int(n_list[i])
    
    if len(n_list) % 2 != 0:
        n_list.append(0)
    return n_list

data_list_1 = new_list_1(data_list_1)
file_list_1 = new_list_1(file_list_1)


def st(k):       # Переводим степень из вида '12' в '¹²'
    s = ''                      
    for i in range(0,len(k)):   
        j = k[i]                
        s = s + indexes_1[j]
    return s

count_list = data_list_1[1::2] + file_list_1[1::2]   # Сколько одночленов с степенями и сортируем степени
count_list_1 = list(set(count_list))
count_list = count_list_1[::-1]
res = []

for i in count_list:
    if i in data_list_1 and i not in file_list_1:    # Производим сложение многочленов
        a = data_list_1.index(i)
        b = data_list_1[a-1]
        b = int(b)
        res.append(b)
    if i not in data_list_1 and i in file_list_1:
        a = file_list_1.index(i)
        b = file_list_1[a-1]
        b = int(b)
        res.append(b)
    if i in data_list_1 and i in file_list_1:
        a = data_list_1.index(i)
        a1 = file_list_1.index(i)
        b = int(data_list_1[a-1]) + int(file_list_1[a1-1])
        res.append(b)

# Приводим к красивому виду.

for i in range(0,len(res)):
    count_list[i] = str(count_list[i])

result = []
for i in range(0,len(res)):
    if res[i] >= 0 and i != 0:
        b = f'+ {res[i]}x{st(count_list[i])} '
        result.append(b)
    elif res[i] < 0 and i != 0:
        b = f'- {res[i]*(-1)}x{st(count_list[i])} '
        result.append(b)
    else:
        b = f'{res[i]}x{st(count_list[i])} '
        result.append(b)

if count_list[-1] == '0':
    del result[-1]
    c = res[-1]
    
    if c>=0:
        c = f'+ {c}'
    else:
        c = f'- {c*-1}'
    result.append(c)

result.append(' = 0')
result_1 = (''.join(result))
print(result_1)

with open('result.txt', 'w',encoding='utf-8') as f:
    f=f.write(f'{result_1}')
