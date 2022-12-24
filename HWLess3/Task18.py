# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# Ввод: 10
# Ввод: 7 
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random
n = int(input('Введите длину массива? '))
massive = []
for i in range(0, n):
    random_numbers = random.randint(1, n)
    massive.append(random_numbers)
print(f'{massive}')

x = int(input('введите число для сравнения: '))
min = max = abs(x - massive[0])
count = False
z = k = massive[0]
for i in range(0,len(massive)):
    if massive[i] == x:
        count = True
        print(f'Число {x} в заданном массиве бизко к самому себе!')
        break
    else:
        for j in range(1, len(massive)):          
            if massive[j] > x and (massive[j] - x) < max:
                max = massive[j] - x
                z = massive[j]
            elif massive[j] < x and (x - massive[j]) < min:
                min = x - massive[j]
                k = massive[j]

if count == False:
    if max < min:
        print(f'Ближайшее число к {x} является {z}.')
    elif max == min:
        print(f'Число {k} и число {z} одинаково близки к {x}!')
    else:
        print(f'Ближайшее число к  {x} является число {k}.')
