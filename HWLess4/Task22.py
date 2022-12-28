# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого набора. 
# m - кол-во элементов второго набора. 
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12


import random
def create_array(x, start, end):
    massive = []
    for i in range(0, x):
        random_numbers = random.randint(start, end)
        massive.append(random_numbers)
    return massive


n = int(input('Введите количество элементов в первом наборе'))
m = int(input('Введите количество элементов во втором наборе'))
array_start = int(input('Введите начало набора: '))
array_end = int(input('Введите конец набора: '))

f_array = create_array(n, array_start, array_end)
print('Первый набор:', f_array)
s_array = create_array(m, array_start, array_end)
print('Второй набор:', s_array)

f_set = set(f_array)
s_set = set(s_array)
final_set = f_set.intersection(s_set)
print(f'Числа встречаются в обоих массивах {sorted(final_set)}')