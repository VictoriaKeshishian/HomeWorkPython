#2.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            if not (x or y or z) == (not x and not y and not z):
                print(f'X:{x}; Y:{y}; X:{z}')
