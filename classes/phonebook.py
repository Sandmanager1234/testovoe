import math
from classes.record import Record


RECORDS_ON_PAGE = 5 # Количество записей на странице
FILENAME = 'phonebook.txt' # Имя файла справочника


class Phonebook:
    def __init__(self) -> None:
        """
        Объявление класса.

        Читается файл, указанный в FILENAME. Каждая новая строка считается отдельной записью

        Формат записи в файле:

        Фамилия|Имя|Отчество|Название организации|<рабочий телефон>|<личный телефон>

        Все записи объявляются классом `Record` и сохраняются в после `records`.
        `page_count` расчитывается по формуле: <общее количество записей>/<количество записей на странице> с округлением вверх.
        """
        with open(FILENAME, 'r', encoding='utf8') as file:
            rows = file.read().split('\n')
        self.records = list(map(lambda x: Record(x.split('|')) if x != '' else None, rows))
        try:
            self.records.remove(None)
        except:
            pass
        self.page_count = math.ceil(len(self.records)/RECORDS_ON_PAGE)

    def add_record(self, record_data: list[str]) -> None:
        """
        Добавляет запись в конец списка.
        
        Параметр `record_data` - список с характеристиками записи.

        Пример:

        ['Фамилия', 'Имя', 'Отчество', 'Название организации', '+79998887766', '+76665554433']

        После добавления, запись также записывается в файл.
        """
        self.records.append(Record(record_data))
        with open(FILENAME, 'a', encoding='utf8') as file:
            file.write(f'{self.records[-1].get_row()}\n')
    
    def print_page(self, page: int) -> None:
        """
        Выводит в консоль содержимое страницы справочника.

        Параметр `page` - номер страницы, которую необходимо отобразить

        Если указана несуществующая страница, выведится без данных.
        """

        for i, rec in enumerate(self.records[(page-1)*RECORDS_ON_PAGE:page*RECORDS_ON_PAGE]):
            print(f"[{i+(page-1)*RECORDS_ON_PAGE}] {rec.get_info()}")
        print(f'Страница {page}/{self.page_count}')

    def find_records(self, param: str, value: str) -> set:
        """
        Линейный поиск по справочнику по одной из характеристики.

        Параметры:

        `param` - ключ характеристики записи
            Существующие ключи:
                'LastName', 'FirstName', 'MidName', 'Organization', 'WorkPhoneNumber', 'SelfPhoneNumber'
        
        `value` - значение характеристики

        Пример:

        `param` = 'FirstName'\n
        `value` = 'Егор'

        Результатом поиска будет множество содержащее в себе кортежи с id записи и самой записи, где в имени указано значение 'Егор'.

        Пример выходных данных:

        {(3, <Record obj>), (6, <Record obj>), (7, <Record obj>)}
        """
        results = set()
        for i, record in enumerate(self.records):
            if record.d[param] == value:
                results.add((i, record))
        return results
    
    def find_records_by_multiple(self, params: list[str], values: list[str]) -> set:
        """
        Поиск записей по нескольким характеристикам.

        Параметры:

        `params` - список с ключами характеристик.

        `value` - список с значениями характеристик.

        см. `find_records`
        """
        results = self.find_records(params.pop(0), values.pop(0))
        for i, param in enumerate(params):
            results &= self.find_records(param, values[i])
        return results

    def edit_record(self, id: int, param: str, value: str) -> None:
        """
        Изменение характеристики записи.

        Параметры:

        `id` - номер записи в списке

        `param` - ключ характеристики

        `value` - значение характеристики

        После изменения просиходит сохранение всего справочника в файл.
        """
        self.records[id].d[param] = value
        self.__save_pb()

    def __save_pb(self) -> None:
        """
        Сохраняет весь список записей в файл.
        """
        data = '\n'.join(map(lambda x: x.get_row() if x is not None else '', self.records))
        with open(FILENAME, 'w', encoding='utf8') as file:
            file.write(f'{data}\n')


if __name__ == '__main__':
    a  = Phonebook()
    a.read_pb(2)