# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# first = int(input())
# sec =  int(input())
# third = int(input())

# sum1 = ((first + 1) // 2)
# print(f"В первом классе потребуется {sum1} парт")

# sum2 = ((sec +1) // 2)
# print(f"Во втором классе потребуется {sum2} парт")

# sum3 = ((third + 1)// 2)
# print(f"В третьем классе потребуется {sum3} парт")

# print (f"во всех трех классах потребуется {sum1 + sum2 + sum3} парт")


# Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
# это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# n = int(input())
# m = int(input())
# if n - m == 0:
#   c = 0
# else:
#   c = n + m - 1
# print(c)


# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2016
# Output: YES


# year = int(input("Введите год: "))

# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print(" Yes")
# else:
#     print("No")


# with open('file.txt', 'w') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()
# path = 'file.txt'
# data = open(path, 'r'




# По данному целому неотрицательному n вычислите значение n!.
#  N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while


# Input:       5

# Output:    120








# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.



# n = int(input("Введите число: "))
# def fibonache(n):
#     # 0 1 1 2 3 5 8 

#     if n == 0:
#         return 1
#     if n == 1:
#         return 2 
#     number0 = 0
#     number1 = 1
#     count = 2
#     while n >= number1:
#         if n == number1:
#             return count
#         temp = number1
#         number1 += number0
#         number0 = temp
#         count += 1
#     return -1
# print(fibonache(n))



# Задача №13
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений
# за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура
# ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2


# import random

# n = 100
# m = []
# for num in range(0,n):
#     random_number = round(random.uniform(-50,50),0)
#     m.append(random_number)

# print(n)
# print(m)

# 1 вариант  решения

# from random import randint
# n = int(input())
# l = [randint(-50, 50) for i in range(1, n)]
# count = 0
# maxcount = 0
# m = []
# for el in l:
#     if el >= 0:
#         count += 1
#         m.append(count)
#     else:
#         if count > maxcount:
#             maxcount = count
#         count = 0

# print(l)
# print(maxcount)


# 2 вариант решения


import random
# n = 35
# m = []
# count = 0 
# max = 0
# for i in range(0, n):
#     random_num = round(random.randint(-50, 50))
#     m.append(random_num)
#     if m[i] < 0 : count = 0 
#     if m[i] > 0 : 
#         count +=1
#         if max < count : max = count
   
# print(n)
# print(m)

# print(count)
# print(max)

# 3  вариант решения

# def sinoptik(N):
#     days=[]
#     for _ in range(N):
#         days.append(round(random.uniform(-10,50),0))  
#     print(days)
#     maxPeriod = maxPeriodResult = 0
#     i = 0
#     while i<N-1:
#         if days[i]>0:
#             while days[i]>0 and i<N-1:
#                 maxPeriod+=1
#                 i+=1
#             if maxPeriodResult<maxPeriod: maxPeriodResult=maxPeriod
#         maxPeriod=0
#         i+=1
#     return maxPeriodResult

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

# def arbuzLine(N):
#     arbuzes=[]
#     for _ in range(N):
#         arbuzes.append(random.randint(5000,30000))
#     arbuzes.sort()
#     print(arbuzes)
    
#     min=max=arbuzes[0]
#     for item in arbuzes:
#         if min>item: min = item
#         elif max < item: max = item
    
#     return min, max

#     def arbuzLine(N):
#     arbuzes=[]
#     for _ in range(N):
#         arbuzes.append(random.randint(5000,30000))
#     arbuzes.sort()
#     print(arbuzes)
    
#     min=max=arbuzes[0]
#     for item in arbuzes:
#         if min>item: min = item
#         elif max < item: max = item
    
#     return min, max

# 17
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# 19
# Дана последовательность из N целых чисел и число K.
#  Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 2
# Output:  [4, 5, 1, 2, 3]


# K = 2
# m = [1, 2, 3, 4, 5]
# result = []
# for i in range(0, K):
#     m.insert(0, m[-1])
#     m.pop(-1)
#     print(m)


# # вариант № 2
# n = int(input('Введите длину списка >>> '))
# l = []
# for num in range(0,n):
    
#     random_number = round(random.randint(-10,10))
#     l.append(random_number)
# print(l)

# k = int(input('Введите на сколько индексов сдвигать >>> '))
# for i in range(k):
#     p = l.pop(-1)
#     l.insert(0, p)

# print(l)


# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
#  {" VIII ":" S007 "}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# inpDict = {
#     "I": "S001",
#     "II": "S002",
#     "III": "S001",
#     "IV": "S005",
#     "V": " S005 ",
#     "VI": " S009 ",
#     "VII": " S007 ",
# }



# 23
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером) 

# Input: [0, -1, 5, 2, 3]
# Output: 2 

# пояснение
# (-1 < 5, 2 < 3)


# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# text = "a a a b c a a d c d d"
# dict = {}
# for t in text.split():
#     if t in dict:
#         count = dict.get(t)
#         dict[t] = count= count + 1
#     else:
#         dict[t] = 1
# print(dict)


# 2 способ решения

# string = 'a a a b c a a d c d d'
# res = ''
# data = {}
# array = string.split()
# print(array)
# for item in array:
#     if item in data:
#         data[item] += 1
#         res += item + '_' + str(data[item]) + ' '
#     else:
#         data[item] = 0
#         res += item + ' '
# print(res)


# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13



# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
#  Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. 
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#        max_number = n
# print(max_number)

n = int(input('введи число N:'))
if n!=0:
    max_number = n
    while n != 0:
        if max_number < n:
            max_number = n
        n = int(input('введи следуещее число N:'))
    print('максимальное число {}'.format(max_number))
else:
    print('чисел нет')

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)


# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, 
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells.

# Output: 19

# st = "She sells sea shells on the sea shore;\
# The shells that she sells are sea shells I'm sure.\
# So if she sells sea shells on the sea shore,\
# I'm sure that the shells are sea shore shells."
# print(st)
# st = st.lower()
# st = st.replace(',', " ")
# st = st.replace('.', " ")
# st = st.replace(';', " ")
# st = st.replace('\'', " ")
# words = set(st.split())
# print(words)
# print(len(words))
