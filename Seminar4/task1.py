#Вычислить число c заданной точностью d
from math import pi

n = int(input("Введите число для заданной точности числа Пи:\n"))
template = '{:.' + str(n) + 'f}'
print(template.format(pi))