# Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)


lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(lst)

def multi(ab):
    if len(lst) % 2 !=0:
        ab = [(lst[i]*lst[len(lst) - i - 1]) for i in range(0, int(len(lst)//2 + 1))]
    else:
        ab = [(lst[i]*lst[len(lst) - i - 1]) for i in range(0, int(len(lst)//2))]
    return ab


print(multi(lst))

