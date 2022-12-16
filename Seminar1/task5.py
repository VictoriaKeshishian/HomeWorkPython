# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# d = √ (х А – х В)*2 + (у А – у В)*2 формула
print("Input x1: ")
x1 = int(input())
print("Input y1: ")
y1 = int(input())
print("Input x2: ")
x2 = int(input())
print("Input y2: ")
y2 = int(input())

import math
print(f'A1A2 lenght is:  {round(math.sqrt((x1-x2)**2+(y1-y2)**2),3)}')
