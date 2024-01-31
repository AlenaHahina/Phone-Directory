
def work_with_phonebook():
    choice = input('Выберите действие:\n1 - Показать список контактов\n2 - Найти контакт\n3 - Добавить новый контакт\n4 - Изменить контакт\n5 - Удалить контакт\n:')
    if choice == '1':
        guide = lesa()
        print(* guide, sep='\n')
        continuation()
    elif choice == '2':
        find_name()
    elif choice == '3':
        add_name()
    elif choice == '4':
        edit()
    elif choice == '5':
        delite()
    else:
        print('Введена неверная команда. Попробуйте ещё раз.')
        work_with_phonebook()

def find_name():
    list_1 = lesa()
    name = input('Введите фамилию: ')
    finde = list(filter(lambda x: name in x[0], list_1))
    if len(finde) !=0:
        for i in finde:
            print(i)
            continuation()
    else:
        surname = input('Фамилия отсутствует в списке контактов. Хотите добавить?\n1 - да\n2 - нет\n: ')
        if surname == '1':
            add_name()
        if surname == '2':
            continuation()
        else:
            print('Введена неверная команда.')
            continuation()


def continuation():
    con = input('Хотите продолжить?\n1 - да\n2 - нет\n: ')
    if con == "1":
        work_with_phonebook()
    elif con == "2":
        print('До свидания!')
        exit()
    else:
        print('Введена неверная команда.')
        continuation()


def delite():
    list_1 = lesa()
    name = input('Введите фамилию: ')
    len_list_1 = len(list_1)
    rem = []
    for i in list_1:
        if name in i[0]:
            rem.append(i)
    if len(rem) !=0:
        print(*rem, sep='\n')
    if len(rem) == 1:
        list_1.remove(rem[0])
        save(list_1)
        continuation()
    elif len(rem) >1:
        num = input('Введите номер телефона: ')
        for j in rem:
            if num == j[2]:
                list_1.remove(j)
                save(list_1)
                continuation()
        if len_list_1 == len(list_1):
            print('Такого номера нет.')
            continuation()  
    else:
        print('Такого контакта нет.')
        continuation() 

    
def edit():
    list_1 = lesa()
    surname = input('Напишите фамилию контакта,который будет изменен\n: ')
    finde = list(filter(lambda x: surname in x[0], list_1))
    if len(finde) !=0:
        for i in finde:
            print(i)
    else:
        print('Фамилия отсутствует в списке контактов.')
        continuation()
    if len(finde) ==1:
        for i in finde:
            new = input('Хотите изменить фамилию - 1, имя -2, номер телефона - 3?\n: ')
            if new == '1':
                    list_1[list_1.index(i)][0] = input('Введите новую фамилию: ')
            elif new == '2':
                    list_1[list_1.index(i)][1] = input('Введите новое имя: ')
            elif new == '3':
                    list_1[list_1.index(i)][2] = input('Введите новый номер телефона: ')        
            else:
                print('Введена неверная команда.')
                edit()
    nam = 0
    if len(finde) >1:
        num = input('Введите номер телефона: ')
        for j in finde:           
            if num == j[1]:
                new = input('Хотите изменить фамилию - 1, имя -2, номер телефона - 3? ')
                if new == '1':
                    list_1[list_1.index(j)][0] = input('Введите новую фамилию: ')
                elif new == '2':
                    list_1[list_1.index(j)][1] = input('Введите новое имя: ')
                elif new == '3':
                    list_1[list_1.index(j)][2] = input('Введите новый номер: ')    
                else:
                    print('Введена неверная команда.')
                    edit()
            else:
                nam += 1
        if len(finde) == nam:
            print('Такого номера телефона нет.')
    save(list_1)
    continuation()


def add_name():
    list_1 = lesa()
    saves = input('Хотите создать новый контакт? Да - 1, нет - 2: ')
    list_2 = []
    if saves == '1':
        name = input('Введите новую фамилию: ')
        list_2.append(name)
        nume = input('Введите новое имя: ')
        list_2.append(nume)
        nume1 = input('Введите новый номер телефона: ')
        list_2.append(nume1)
        if len(list(filter(lambda x: list_2 == x, list_1))) > 1: print('Такой контакт и номер уже есть.')
        else:
            list_1.append(list_2)
            save(list_1)
            print('Контакт добавлен.')
            continuation() 
    elif saves == "2":
        continuation() 
    else:
        print('Введена неверная команда.')
        continuation() 
   


def save(list_1):
    with open('phonebook.txt', 'w', encoding='utf-8') as Phone:
        for i in list_1:
            Phone.write(f'{i[0]},{i[1]},{i[2]}\n')


def lesa():
    guide = []
    with open('phonebook.txt', 'r+', encoding='utf-8') as Phone:
        for i in Phone.readlines():
            guide.append(i.strip().split(','))
    return guide

work_with_phonebook()