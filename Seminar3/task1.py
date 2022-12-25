# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
list = [random.randint(0,20) for i in range(10)]
print(list)

count = 0
for i in range(len(list)):
    if i % 2 != 0:
        count += list[i]
print(count)

