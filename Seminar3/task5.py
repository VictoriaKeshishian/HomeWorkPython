# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите число: \n'))
print('Числовой ряд:')
for i in range(0, number + 1, 1):
    print(i, end = ' ')


def Fibonacci(n):
    if n in [1,2]: return 1
    else: return Fibonacci(n-1) + Fibonacci(n-2)

def findFibonacci(n):
    if n == 1: return 1
    elif n == 2: return -1
    else:
        num1, num2 = 1, -1
        for n in range(2,n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
for e in range(1, number + 1):
    list.append(Fibonacci(e))
    list.insert(0, findFibonacci(e))
print('')
print(f'Последовательность Фибоначчи:\n {list}')

