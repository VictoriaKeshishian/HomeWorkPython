
def get_operation():
    operation = int(input('Выберите действие: \n 1 - Добавление нового пользовтеля \n 2 - Вывести таблицу \n 3 - Вывести имя и фамилию \n 4 - Сортировка по именам \n 5 - Сортировка по id \n 6 - Выход \n'))
    return operation

def add_user():
    id = int(input('Введите id: '))
    name = input('Введите имя: ')
    lastname = input('Введите фамилию: ')
    number = int(input('Введите номер: '))
    comments = input('Комментарий: ')
    line = f"{id},{name},{lastname},{number},{comments},\n"
    with open ("user.txt","a") as file:
        file.write(line)
    print('Выполнено')

def print_table():
    with open ("user.txt","r") as file:
        for line in file.readlines():
            print(line, end = " ")

def print_name():
    with open ("user.txt","r") as file:
        for line in file.readlines():
            a = line.split(',')
            print(f'Имя: {a[1]}, Фамилия: {a[2]}')

