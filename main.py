import re
import menu
from classes.phonebook import Phonebook


def main():
    pb = Phonebook()
    selector = 0
    while selector != '5':
        menu.print_main_menu()
        selector = input(menu.menu_inp)
        match selector:
            case '1':
                menu.read_pb(pb)
            case '2':
                menu.add_record_to_pb(pb)
            case '3':
                menu.edit_record(pb)
                pass
            case '4':
                menu.find_record(pb)
            case '5':
                print('bb')
                exit()
            case _:
                print(menu.incorret_inp)


if __name__ == '__main__':
    main()