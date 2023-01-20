# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Структура данных:
# Фамилия, имя, отчество, номер телефона.
# .
# Пример данных:
# Ivanov, Ivan, Ivanovich, +79111234567
# Petrov, Petr, Petrovich, +79119876543
# .
# Функции справочника:
# - Показать все записи
# - Найти запись по вхождению частей имени
# - Найти запись по телефону
# - Добавить новый контакт
# - Удалить контакт
# - Изменить номер телефона у контакта
# .
# Пример работы программы:
# .
# При запуске программы пользователю выдается меню:

# Введите номер действия:
# 1 - Показать все записи
# 2 - Найти запись по вхождению частей имени
# 3 - Найти запись по телефону
# 4 - Добавить новый контакт
# 5 - Удалить контакт
# 6 - Изменить номер телефона у контакта
# 7 - Выход


phone_nums = " PhoneBook.txt "

def show_all(file_name):
    show = open(file_name, 'r', encoding='utf8')
    print(show.read())


def readfile(file_name):
    result = []
    with open(file_name, 'r+', encoding='utf8') as data:
        for line in data:
            result.append(line.split(','))
    return result


def phone_searh(userlist):
    phonenumber = ' ' + input('Введите номер телефона: ') + "\n"
    for i in userlist:
        if i[3] == phonenumber:
            print(i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3])


def namesearch(dictArray):
    name = ' ' + input("Введите имя пользователя: ")
    for i in dictArray:
        if i[1] == name:
            print(i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3])


def addContact(file_name):
    new_contact = input('Введите ФИО и номер телефона через запятую(", "):  ')
    with open(file_name, 'a', encoding='utf8') as data:
        data.writelines(new_contact + '\n')


def deleteContact(file_name):
    contact_to_delete = input(
        'Введите фамилию контакта: (удаление контакта возможно по его фамилии)')
    s = ""
    with open(file_name, "r", encoding="utf8") as data:
        for line in data:
            if contact_to_delete in line:
                continue
            s += line

    with open(file_name, "w", encoding="utf8") as data:
        data.write(s)


def defaut():
    print('Данный справочник не содержит данных символов! Проверьте ввод!')


print("Приветствуем в нашем справочнике ! \n Выберите интересующую Вас ктаегорию: \n1 - Показать все записи \n2 - Найти запись по номеру телефона \n3 - Найти запись по имени \n4 - Добавить новый контакт \n5 - Удалить контакт \n6 - Выход \n ")
userAnswer = input('Введите цифру: ')

match userAnswer:
    case "1":
        show_all(phone_nums)

    case "2":
        phone_searh(readfile(phone_nums))

    case "3":
        namesearch(readfile(phone_nums))

    case "4":
        addContact(phone_nums)

    case "5":
        deleteContact(phone_nums)

    case "6":
        exit(0)

    case _:
        defaut()
