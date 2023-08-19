import random

records = 50

l_names = ['Шестопалов', 'Шерстнев', 'Базалук', 'Понасенков', 'Сапронов', 'Крюк', 'Александров', 'Дуров']
f_names = ['Павел', 'Егор', 'Эдуард', 'Александр', 'Сергей', 'Андрей', 'Пётр', 'Василий', 'Геннадий', 'Николай']
m_names = ['Николаевич', 'Викторович', 'Сергеевич', 'Александрович', 'Эдуардович', 'Васильевич', 'Геннадиевич', 'Андреевич', 'Егорович']

orgs = ['Яндекс', 'Тинькофф', 'Сбербанк', 'РиоРим', 'ИП', 'Google', 'Вкусно - и точка', 'Бургер Кинг', 'KFC', 'hh.ru', 'Valve corp', '<epam>', 'Kwork', 'Mail.ru Group', 'Vkontakte', 'На шее у мамы']

result = []
for i in range(records):
    l_name = random.choice(l_names)
    f_name = random.choice(f_names)
    m_name = random.choice(m_names)
    org = random.choice(orgs)
    wpn = '+7' + str(random.randint(1000000000, 9999999999))
    spn = '+7' + str(random.randint(1000000000, 9999999999))
    result.append(f'{l_name}|{f_name}|{m_name}|{org}|{wpn}|{spn}')

data = '\n'.join(result)
with open('phonbook.txt', 'w', encoding='utf8') as file:
    file.write(f"{data}\n")