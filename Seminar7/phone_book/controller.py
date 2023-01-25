# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных.
# Модуль контроллер
# Модуль для импорта(ввода данных)
# Модуль для экспорта(вывод данных)
# Строка содержит id,имя,фамилию,номер телефона, комментрий - символ разделитель на выбор(можно использовать пробел или запятые) + файл с хранением этих строк
# *Добавить сортировку по имени или по id
# *Добавить вывод только имени и фамилии

import view 
import sorting



def start():
    while True:
        get_operation = view.get_operation()
        if get_operation == 1: view.add_user()
        elif get_operation == 2: view.print_table()
        elif get_operation == 3: view.print_name()
        elif get_operation == 4: sorting.sort_names()
        elif get_operation == 5: sorting.sort_id()
        elif get_operation == 6: break
