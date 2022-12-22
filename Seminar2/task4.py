# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

import random

n = int(input('Введите число: '))
list_num = [random.randint(-n,n) for i in range(n)]
print(list_num)

path = 'file.txt'
data = open(path, 'r')
multi = 1
for i in data:
    multi *= list_num[int(i)]
data.close()
print(multi)

