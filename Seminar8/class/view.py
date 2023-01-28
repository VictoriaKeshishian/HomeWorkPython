def choice():
    ch = int(input("выберите действие:\n 1 - добавить ученика,\n 2 - показать список учеников,\n 3 - добавить предмет,\n 4 - поставить оценку,\n 5 - успеваемость ученика,\n  6 - выход,\n"))
    return ch


def get_student():
    name =  input('Введите имя и фамилию: ')
    return name

def get_journal():
    lesson = input('Введите предмет: ')
    return lesson

def attestat():
    name = input('Введите имя и фамилию: ')
    lesson = input('Введите предмет: ')
    mark = input('Введите оценку: ')
    return name, lesson, mark

def one_student():
    name =  input('Введите имя и фамилию ученика: ')
    return name

