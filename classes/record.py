KEYS = ('LastName', 'FirstName', 'MidName', 'Organization', 'WorkPhoneNumber', 'SelfPhoneNumber')

class Record:
    def __init__(self, params: list[str]) -> None:
        """
        Объявление класса.

        Параметры:

        `params` - список характеристик записи расставленные в следующем порядке:

        Фамилия, Имя, Отчество, Название организации, рабочий телефон, личный телефон
        """
        # self.l_name, self.f_name, self.m_name, self.org, self.work_phone, self.self_phone = s
        self.d = dict(zip(KEYS, params))

    def get_info(self) -> str:
        """
        Возвращает строку с информацией о записи.

        Пример выходной строки:

        Фамилия Имя Отчество\n
        Организация: Название организации\n
        Рабочий телефон: +71112223344 Личный телефон: +79998887766
        """
        data = f"""{self.d['LastName']} {self.d['FirstName']} {self.d['MidName']}
Организация: {self.d['Organization']}
Рабочий телефон: {self.d['WorkPhoneNumber']}  Личный телефон: {self.d['SelfPhoneNumber']}
"""
        return data

    def get_row(self) -> str:
        """
        Возвращает строку для записи в текстовый файл в следующем формате:

        Фамилия|Имя|Отчество|Название организации|<рабочий телефон>|<личный телефон>

        Пример:
        
        Иванов|Иван|Иванович|ИП ИИИ|+79998887766|+71112223344
        """
        row = f"{self.d['LastName']}|{self.d['FirstName']}|{self.d['MidName']}|{self.d['Organization']}|{self.d['WorkPhoneNumber']}|{self.d['SelfPhoneNumber']}"
        return row