import math
from classes.record import Record


RECORDS_ON_PAGE = 5 # Количество записей на странице
FILENAME = 'phonebook.txt' # Имя файла справочника


class Phonebook:
    def __init__(self):
        with open(FILENAME, 'r', encoding='utf8') as file:
            rows = file.read().split('\n')
        self.records = list(map(lambda x: Record(x.split('|')) if x != '' else None, rows))
        try:
            self.records.remove(None)
        except:
            pass
        self.max_page = math.ceil(len(self.records)/RECORDS_ON_PAGE)

    def add_record(self, record_data: list[str]) -> None:
        self.records.append(Record(record_data))
        with open(FILENAME, 'a', encoding='utf8') as file:
            file.write(f'{self.records[-1].record_to_row()}\n')
    
    def read_pb(self, page: int) -> None:
        for i, rec in enumerate(self.records[(page-1)*RECORDS_ON_PAGE:page*RECORDS_ON_PAGE]):
            print(f"[{i+(page-1)*RECORDS_ON_PAGE}] {rec.data_record()}")
        print(f'Страница {page}/{self.max_page}')

    def find_records(self, param: str, value: str) -> set:
        results = set()
        for i, record in enumerate(self.records):
            if record.d[param] == value:
                results.add((i, record))
        return results
    
    def find_records_by_multiple(self, params: list[str], values: list[str]) -> set:
        results = self.find_records(params.pop(0), values.pop(0))
        for i, param in enumerate(params):
            results &= self.find_records(param, values[i])
        return results

    def edit_record(self, id: int, param: str, value: str) -> None:
        self.records[id].d[param] = value
        self.__save_pb()

    def __save_pb(self) -> None:
        data = '\n'.join(map(lambda x: x.record_to_row() if x is not None else '', self.records))
        with open(FILENAME, 'w', encoding='utf8') as file:
            file.write(f'{data}\n')


if __name__ == '__main__':
    a  = Phonebook()
    a.read_pb(2)