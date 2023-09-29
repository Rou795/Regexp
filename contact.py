import re

# Реализуем класс для записи контактов
class Contact:

# конструктор класса.
    def __int__(self, lastname='', surname='', organization='',
                position='', phone='', email=''):
        self.lastname = lastname
        self.surname = surname
        self.organization = organization
        self.position = position
        self.phone = phone
        self.email = email

# перегрузка метода '=='. Для целей проверки тождественности контактов.
# логика такова - проверям атрибуты попарно сначала на пустоту данных, потом
# на их равенстов. Если не равны, то возвращаем False, иначе сохраняем в check True
# если проверили все атрибуты и хотя бы один совпал (при том, что другие не могут сравниваться)
# то это один и тот же контакт

    def __eq__(self, other):
        check = False
        if (self.lastname != '') and (other.lastname != ''):
            check = True
            if self.lastname != other.lastname:
                return False
        if (self.firstname != '') and (other.firstname != ''):
            check = True
            if self.firstname != other.firstname:
                return False
        if (self.surname != '') and (other.surname != ''):
            check = True
            if self.surname != other.surname:
                return False
        if (self.organization != '') and (other.organization != ''):
            check = True
            if self.organization != other.organization:
                return False
        if (self.position != '') and (other.position != ''):
            check = True
            if self.position != other.position:
                return False
        if (self.phone != '') and (other.phone != ''):
            check = True
            if self.phone != other.phone:
                return False
        if (self.email != '') and (other.email != ''):
            check =True
            if self.email != other.email:
                return False
        return check

# перегрузка метода str для более удобного вывода

    def __str__(self):
        contact_text = (f'Фамилия: {self.get_lastname()}\nИмя: {self.get_firstname()}\n'
                        f'Отчество: {self.get_surname()}\nОрганизация: {self.get_organization()}\n'
                        f'Должность: {self.get_position()}\nТелефон: {self.get_phone()}\n'
                        f'E-mail: {self.get_email()}')
        return contact_text

# сеттеры для установки значений атрибутов

    def set_lastname(self, lastname: str):
        self.lastname = lastname.strip()

    def set_firstname(self, firstname: str):
        self.firstname = firstname.strip()

    def set_surname(self, surname: str):
        self.surname = surname.strip()

    def set_organization(self, organization: str):
        self.organization = organization.strip()

    def set_position(self, position: str):
        self.position = position.strip()

    def set_phone(self, phone: str):
        self.phone = phone.strip()

    def set_email(self, email: str):
        self.email = email.strip()

# геттеры для получения значений атрибутов

    def get_lastname(self):
        return self.lastname

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def get_organization(self):
        return self.organization

    def get_position(self):
        return self.position

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

# метод перевода атрибутов контакта в форму списка.
# Используется в дальнейшем слиянии контактов

    def contact_in_list(self):
        contact_list = [self.get_lastname(),
                        self.get_firstname(),
                        self.get_surname(),
                        self.get_organization(),
                        self.get_position(),
                        self.get_phone(),
                        self.get_email()]
        return contact_list

# заполнение атрибутов контакта из списка

    def set_from_line(self, line: list):
        row = ' '.join(line)
        try:
            self.set_lastname(re.search(r'[а-я]+', row, re.I).group().strip())
        except AttributeError:
            self.set_lastname('')
        row = row.replace(self.get_lastname(), '').strip()
        try:
            self.set_firstname(re.search(r'[а-я]+', row, re.I).group().strip())
        except AttributeError :
            self.set_firstname('')
        row = row.replace(self.get_firstname(), '').strip()
        try:
            self.set_surname(re.search(r'[а-я]+', row, re.I).group().strip())
        except AttributeError:
            self.set_surname('')
        row = row.replace(self.get_surname(), '').strip()
        self.set_organization(line[3].strip())
        row = row.replace(self.get_organization(), '').strip()
        try:
            self.set_position(re.search(r'[а-я ,:ceapokmx;–-]{5,500}', row, re.I).group().strip())
        except AttributeError:
            self.set_position('')
        row = row.replace(self.get_position(), '').strip()
        try:
            self.set_email(re.search(r'\S+[@]{1}\S+', row, re.I).group().strip())
        except AttributeError:
            self.set_email('')
        row = row.replace(self.get_email().strip(), '')
        pattern_cmp = re.compile(r"(\+7|8){1,2}[ ]*\(*([0-9]{3})\)*[ -]*([0-9]{3})[ -]*([0-9]{2})"
                                 r"[ -]*([0-9]{2}) *\(*([доб.]*)[. -]*([0-9]*)\)*")
        result = pattern_cmp.sub(r"+7(\2)\3-\4-\5 \6\7", row)
        self.set_phone(result.strip(' '))

# метод объединеия контактов

    def merge(self, other):
        if type(other) != Contact:
            return False
        contact_fields_1 = self.contact_in_list()
        contact_fields_2 = other.contact_in_list()
        merge_contact = []
        for contact_1, contact_2 in zip(contact_fields_1, contact_fields_2):
            if contact_1 == '':
                merge_contact.append(contact_2)
            else:
                merge_contact.append(contact_1)
        self.set_from_line(merge_contact)
