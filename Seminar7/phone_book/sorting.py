def sort_names():
    with open("user.txt","r+") as file:
        lst1 = file.readlines()
        lst2 = []
        for line in lst1:
            temp = line.split(",")
            lst2.append(temp)
        lst2 = sorted(lst2,key = lambda x:x[1])
        file.seek(0)
        for worker in lst2:
            file.write(",".join(worker))
    print("Сортировка выполнена")

def sort_id():
    with open("user.txt","r+") as file:
        lst1 = file.readlines()
        lst2 = []
        for line in lst1:
            temp = line.split(",")
            lst2.append(temp)
        lst2 = sorted(lst2,key = lambda x:x[1])
        file.seek(0)
        for worker in lst2:
            file.write(",".join(worker))
    print("Сортировка выполнена")
