# Найти сумму чисел списка стоящих на нечетной позиции

from random import randint as ri
list = [ri(0,20) for i in range(5)]
print(list)

total = 0
for i,num in enumerate(list):
    if i%2 != 0:
        total += num

print(total)