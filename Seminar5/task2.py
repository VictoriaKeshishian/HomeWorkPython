# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. 
# Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 

# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, 
#         тобы гарантированно победить, соответственно внедрить этот алгоритм боту )

from random import randint as ri

total_sweet = 221
take_sweet = 0
player1_sweet = 0
player2_sweet = 0
bot_sweet = 0


def start_game():
    global choice
    print('На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход')
    print('')
    if choice == 'да': who_is_first_with_bot()
    else: who_is_first()

print('Вы хотите играть с ботом? (введите да или нет): ')   
choice = input()

def who_is_first():
    random_number = ri(1,2)
    if random_number == 1: player1_turn()
    else: player2_turn()

def who_is_first_with_bot():
    random_number = ri(1,2)
    if random_number == 1: player1_turn()
    else: bot_turn()

def player1_turn():
    global choice
    global total_sweet
    global take_sweet
    global player1_sweet
    print(f'Ход первого игрока, количество конфет на столе {total_sweet}')
    print('')
    take_sweet = int(input('Сколько конфет возьмете? '))
    print('')
    while take_sweet > total_sweet or take_sweet > 28 or take_sweet < 0:
        take_sweet = int(input('Недопустимое количество конфет, попробуйте еще раз: '))
        print('')
    total_sweet -= take_sweet
    take_sweet += take_sweet
    if total_sweet > 0:
        if choice == 'да': bot_turn()
        elif choice == 'нет': player2_turn()
    else: print('Победил первый игрок!!!')

def player2_turn():
    global total_sweet
    global take_sweet
    global player2_sweet
    print(f'Ход второго игрока, количество конфет на столе {total_sweet}')
    print('')
    take_sweet = int(input('Сколько конфет возьмете? '))
    print('')
    while take_sweet > total_sweet or take_sweet > 28 or take_sweet < 0:
        take_sweet = int(input('Недопустимое количество конфет, попробуйте еще раз: '))
        print('')
    total_sweet -= take_sweet
    take_sweet += take_sweet
    if total_sweet > 0: player1_turn()
    else: print('Победил второй игрок!!!')


def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(0,28)
    total_sweet -= take_sweet
    take_sweet += take_sweet
    print(f'{take_sweet} взял бот, осталось {total_sweet} конфет')
    print('')
    if total_sweet > 0: player1_turn()
    else: print('Победил Бот!!!')
    
