import view
main_dct = {}
name_lst = []
lessons_lst = []


def start():
    while True:
        print(main_dct)
        ch = view.choice()
        if ch == 1:
            name = view.get_student()
            if name not in name_lst:
                name_lst.append(name)
                main_dct[name] = {}
                for lesson in lessons_lst:
                    main_dct[name][lesson] = []
        
        if ch == 2: 
            print(main_dct)

        if ch == 3:
            lesson = view.get_journal()
            if lesson not in lessons_lst:
                lessons_lst.append(lesson)
                for name in name_lst:
                    main_dct[name][lesson] = []


        if ch == 4:
            name, lesson, mark = view.attestat()
            main_dct[name][lesson].append(mark)

        if ch == 5:
            name = view.one_student()
            print(main_dct[name])

        if ch == 6:
            print("Сеанс окончен, до свидания!")
            break