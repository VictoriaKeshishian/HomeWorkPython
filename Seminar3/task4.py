# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Введите десятичное число:\n '))
number_b = ''
while number > 0:
    number_b = str(number % 2) + number_b
    number = number // 2
print(number_b)