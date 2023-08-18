from samples import *
from classes.phonebook import Phonebook


def print_main_menu() -> None:
    print(main_menu)

 
def read_pb(pb: Phonebook) -> None:
    page = 1
    max_page = pb.max_page
    inp = ''
    while inp != 'b':
        print("\nТЕЛЕФОННЫЙ СПРАВОЧНИК:\n")
        pb.read_pb(page)
        print(page_commands)
        inp = input("Введите команду: ")
        match inp:
            case 'n':
                if page <= max_page-1:
                    page += 1
                else:
                    print('\nВы на последней странице.\n')
            case 'p':
                if page > 1:
                    page -= 1
                else:
                    print('\nВы на первой странице.\n')
            case 'b':
                print('\n')
            case _:
                print('\nНеверный ввод.\n')


def names_input_validator(message: str) -> str:
    valid = False
    while valid == False:
        name = input(message)
        valid = (name.istitle() and name.isalpha())
    return name
        

def phone_numbers_input_validator(message: str, work = False) -> str:
    valid = False
    while valid == False:
        number = input(message)
        if work == True:
            valid = (number[:2] == '+7' and number[2:].isdigit() and len(number) == 12) or (number == '')
        else:
            valid = number[:2] == '+7' and number[2:].isdigit() and len(number) == 12
    return number


def add_record_to_pb(pb: Phonebook):
    l_name = names_input_validator('Введите фамилию: ')
    f_name = names_input_validator('Введите имя: ')
    m_name = names_input_validator('Введите отчество: ')
    org = input('Введите название организации: ')
    work_phone = phone_numbers_input_validator('Введите рабочий номер телефона: ', True)
    self_phone = phone_numbers_input_validator('Введите личный номер телефона: ')
    pb.add_record([l_name, f_name, m_name, org, work_phone, self_phone])
    print('\nЗАПИСЬ УСПЕШНО ДОБАВЛЕНА!\n')


def find_record(pb: Phonebook):
    selector = 0
    while selector != 4:
        print(find_menu)
        selector = int(input(menu_inp))
        match selector:
            case 1:
                find_by_id(pb)
            case 2:
                find_by_one(pb)
            case 3:
                pass
            case 4:
                print('\n')
            case _:
                print(incorret_inp)


def find_by_id(pb: Phonebook):
    valid = False
    while valid == False:
        id = int(input(f'Введите ID элемента. ID от 0 до {len(pb.records)-1}: '))
        if id > 0 and id < len(pb.records):
            valid = True
    print(f'[{id}] {pb.records[id].data_record()}')
    print('Нажмите Enter, чтобы вернутся назад.')
    input()


def find_by_one(pb: Phonebook):
    selector = 0
    while selector == 7:
        print(find_one)
        selector = int(input(menu_inp))
        match selector:
            case 1:
                param = 'LastName'
            case 2:
                param = 'FirstName'
            case 3:
                param = 'MidName'
            case 4:
                param = 'Organization'
            case 5:
                param = 'WorkPhoneNumber'
            case 6:
                param = 'SelfPhoneNumber'
            case 7:
                break
            case _:
                print(incorret_inp)
                continue
        value = input('Введите значение поиска: ')
        results = pb.find_records(param, value)
        print(f'Найдено {len(results)} результатов:\n')
        for id, record in results:
            print(f'[{id}] {record.data_record()}')
        ans = input('Продолжить поиск? (y/n): ')
        if ans == 'y':
            pass
        elif ans == 'n':
            break
        else:
            print(incorret_inp)


def find_by_multiple(pb: Phonebook):
    choices = []
    checker = lambda x: '(+)' if x in choices else ''
    add_del = lambda x: choices.append(x) if x not in choices else choices.remove(x)
    values = []
    params = []
    menu_choice = [
        'Поиск по фамилии',
        'Поиск по имени',
        'Поиск по отчеству',
        'Поиск по организации',
        'Поиск по рабочему номеру телефона',
        'Поиск по личному номеру телефона',
    ]
    ids_dict = {
        1: ('фамилию', 'LastName'),
        2: ('имя', 'FirstName'),
        3: ('отчество', 'MidName'),
        4: ('организацию', 'Organization'),
        5: ('рабочий номер телефона', 'WorkPhoneNumber'),
        6: ('личный номер телефона', 'SelfPhoneNumber')
    }
    selector = 0
    while selector != 8:
        for i, menu_variant in enumerate(menu_choice):
            print(f'[{i+1}] {menu_variant} {checker(i+1)}')
        print('[7] Продолжить')
        print('[8] Назад')
        selector = int(input(menu_inp))
        if selector in range(1, 7):
            add_del(selector)
        elif selector == 7:
            if len(choices) != 0:
                for id in choices:
                    params.append(ids_dict[id][1])
                    values.append(input(f'Введите {ids_dict[id][0]}: '))
                pb.find_records_by_multiple(params, values) 
            else:
                print('Вы не выбрали параметры поиска')
        elif selector == 8:
            print('пошли нахуй')
            break
        else:
            print(incorret_inp)
            continue
