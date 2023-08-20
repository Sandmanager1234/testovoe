from samples import *
from classes.phonebook import Phonebook

IDS_DICT = {
    1: ('фамилию', 'LastName'),
    2: ('имя', 'FirstName'),
    3: ('отчество', 'MidName'),
    4: ('организацию', 'Organization'),
    5: ('рабочий номер телефона', 'WorkPhoneNumber'),
    6: ('личный номер телефона', 'SelfPhoneNumber')
}

def param_match_case(message: str, edit=False):
    selector = ''
    while selector != '7':
        print(message)
        selector = input(menu_inp)
        match selector:
            case '1' | '2' | '3' | '4' | '5' | '6':
                param = IDS_DICT[int(selector)][1]
            case '7':
                break
            case _:
                print(incorret_inp)
                continue
        if edit == False:
            value = input(f'Введите {IDS_DICT[int(selector)][0]}: ')
        else:
            if selector in '123':
                value = names_input_validator(f'Введите {IDS_DICT[int(selector)][0]}: ')
            elif selector in '56':
                value = phone_numbers_input_validator(f'Введите {IDS_DICT[int(selector)][0]}: ')
            else:
                value = input(f'Введите {IDS_DICT[int(selector)][0]}: ')
        return param, value


def id_validator(pb: Phonebook) -> int:
    valid = False
    while valid == False:
        id = input(f'Введите ID элемента. ID от 0 до {len(pb.records)-1}: ')
        if id.isdigit() == True:
            if int(id) > 0 and int(id) < len(pb.records):
                valid = True
    return int(id)

def print_main_menu() -> None:
    print(main_menu)


def print_search_results(results: set) -> None:
    print(f'Найдено {len(results)} записей:\n')
    for id, record in results:
        print(f'[{id}] {record.get_info()}')


def read_pb(pb: Phonebook) -> None:
    page = 1
    max_page = pb.page_count
    inp = ''
    while inp != 'b':
        print("\nТЕЛЕФОННЫЙ СПРАВОЧНИК:\n")
        pb.print_page(page)
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
    error_msg = ''
    while valid == False:
        print(error_msg)
        name = input(message)
        valid = (name.istitle() and name.isalpha())
        error_msg = error_msg_text
    return name
        

def phone_numbers_input_validator(message: str, work = False) -> str:
    valid = False
    error_msg = ''
    while valid == False:
        print(error_msg)
        number = input(message)
        if work == True:
            valid = (number[:2] == '+7' and number[2:].isdigit() and len(number) == 12) or (number == '')
        else:
            valid = number[:2] == '+7' and number[2:].isdigit() and len(number) == 12
        error_msg = error_msg_number
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
    selector = ''
    while selector != '4':
        print(find_menu)
        selector = input(menu_inp)
        match selector:
            case '1':
                find_by_id(pb)
            case '2':
                find_by_one(pb)
            case '3':
                find_by_multiple(pb)
            case '4':
                print('\n')
            case _:
                print(incorret_inp)


def find_by_id(pb: Phonebook):
    id = id_validator(pb)
    print(f'[{id}] {pb.records[id].get_info()}')
    print('Нажмите Enter, чтобы вернутся назад.')
    input()


def find_by_one(pb: Phonebook):
    while True:
        param, value = param_match_case(find_one)
        results = pb.find_records(param, value)
        print_search_results(results)
        ans = input('Продолжить поиск? (y/n): ')
        if ans == 'y':
            pass
        else:
            break


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
    selector = ''
    while selector != '8':
        for i, menu_variant in enumerate(menu_choice):
            print(f'[{i+1}] {menu_variant} {checker(i+1)}')
        print('[7] Продолжить')
        print('[8] Назад')
        selector = input(menu_inp)
        if selector in '123456':
            add_del(int(selector))
        elif selector == '7':
            if len(choices) != 0:
                for id in choices:
                    params.append(IDS_DICT[id][1])
                    values.append(input(f'Введите {IDS_DICT[id][0]}: '))
                results = pb.find_records_by_multiple(params, values)
                print_search_results(results)
                ans = input('Продолжить поиск? (y/n): ')
                if ans == 'y':
                    pass
                elif ans == 'n':
                    break
                else:
                    print(incorret_inp)
            else:
                print('Вы не выбрали параметры поиска')
        elif selector == '8':
            print('\n')
            break
        else:
            print(incorret_inp)
            continue


def edit_record(pb: Phonebook):
    id = id_validator(pb)
    while True:
        param, value = param_match_case(f'\n[{id}] {pb.records[id].get_info()}{edit_one}', edit=True)
        print(param, value)
        pb.edit_record(id, param, value)
        ans = input('Продолжить изменения? (y/n): ')
        if ans == 'y':
            pass
        else:
            break
