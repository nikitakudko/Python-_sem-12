def input_surname():
    return input('Введите фамилию контакта: ').title()

def input_name():
    return input('Введите имя контакта: ').title()

def input_patronymic():
    return input('Введите отчество контакта: ').title()

def input_pnohe():
    return input('Введите телефон контакта: ')

def input_address():
    return input('Введите адресс(город) контакта: ').title()

def creat_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_pnohe()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone} {address}\n'


def add_contact():
    with open('phonebook.txt', 'a', encoding ='utf-8') as file:
        file.write(creat_contact()) 


def print_contacts():
    with open('phonebook.txt', 'r', encoding ='utf-8') as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n')
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)


def search_contact():
    print(
            'Возможные варианты поиска:\n'
            '1. По фамилии\n'
            '2. По имени\n'
            '3. По отчеству\n'
            '4. По телефону\n'
            '5. По адрессу(город)'
            )
    var = input('выберите вариант поиска: ')
    while var not in ('1','2','3','4','5'):
        print("некорректный ввод")
        var = input('выберите вариант поиска: ')
    i_var = int(var) - 1

    search = input("Введите данный для поиска: ").title()
    with open('phonebook.txt', 'r', encoding ='utf-8') as file:
        contacts_list = file.readlines()
    for str_cont in contacts_list:
        lst_contact = str_cont.split()
        if search in lst_contact[i_var]:
            print(str_cont)


def delete_contact():
    print_contacts()
    numb = int(input('Выберите порядковый номер контакта, который хотите удалить:'))
    with open('phonebook.txt', 'r', encoding ='utf-8') as file:
        lines = file.readlines()
    del lines[numb - 1]

    with open('phonebook.txt', 'w', encoding ='utf-8') as file:
        file.writelines(lines)


# def change_contact():
#     print_contacts()
#     numb = int(input('Выберите порядковый номер контакта, который хотите изменить:'))
#     with open('phonebook.txt', 'r', encoding ='utf-8') as file:
#         contacts_list = file.readlines()
#     print(
#             'Что хотите изменить?:\n'
#             '1. Фамилию\n'
#             '2. Имя\n'
#             '3. Отчество\n'
#             '4. Телефону\n'
#             '5. Адресс(город)'
#             )
#     var = input('выберите вариант для изменения: ')
#     while var not in ('1','2','3','4','5'):
#         print("некорректный ввод")
#         var = input('выберите вариант для изменения: ')
#     i_var = int(var) - 1
#     text = input('Введите данные для замены: ')
#     contact = contacts_list[numb - 1].split()
#     contacts_list = contact.replace(contact[i_var], text)
    
#     with open('phonebook.txt', 'w', encoding ='utf-8') as file:
#         file.writelines(contacts_list)


def change_contact():
    print_contacts()
    numb = int(input('Выберите порядковый номер контакта, который хотите изменить:'))
    with open('phonebook.txt', 'r', encoding ='utf-8') as file:
        lines = file.readlines()
    lines[numb-1] = creat_contact()

    with open('phonebook.txt', 'w', encoding ='utf-8') as file:
        file.writelines(lines)


def interface():

    with open('phonebook.txt', 'a', encoding ='utf-8'):
        pass
    
    var = 0
    while var != '6':
        print(
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Удалить контакт\n'
            '5. Изменить контакт\n'
            '6. Выход'
            )
        print()
        var = input('выберите вариант действия: ')
        while var not in ('1','2','3','4','5','6'):
            print("некорректный ввод")
            var = input('выберите вариант действия: ')
        print()

        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                delete_contact()
            case '5':
                change_contact()
            case '6':
                print("")
        print()

if __name__ == "__main__": 
    interface()