# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 5, 6]
print(list)

if len(list) % 2 !=0:
    ab = [(list[i]*list[len(list) - i - 1]) for i in range(0, int(len(list)//2 + 1))]
else:
    ab = [(list[i]*list[len(list) - i - 1]) for i in range(0, int(len(list)//2))]
print(ab)
