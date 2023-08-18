KEYS = ('LastName', 'FirstName', 'MidName', 'Organization', 'WorkPhoneNumber', 'SelfPhoneNumber')

class Record:
    def __init__(self, s: list[str]):
        # self.l_name, self.f_name, self.m_name, self.org, self.work_phone, self.self_phone = s
        self.d = dict(zip(KEYS, s))

    def data_record(self) -> str:
        data = f"""{self.d['LastName']} {self.d['FirstName']} {self.d['MidName']}
Организация: {self.d['Organization']}
Рабочий телефон: {self.d['WorkPhoneNumber']}  Личный телефон: {self.d['SelfPhoneNumber']}
"""
        return data

    def record_to_row(self) -> str:
        row = f"{self.d['LastName']}|{self.d['FirstName']}|{self.d['MidName']}|{self.d['Organization']}|{self.d['WorkPhoneNumber']}|{self.d['SelfPhoneNumber']}"
        return row