from modules.name import Name
from modules.phone import Phone
from modules.email import Email
from modules.birthday import Birthday


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None

    def __str__(self):
        res = f"{self.name}, phones: {'; '.join(p for p in self.phones)}"
        if str(self.birthday) != "None":
            res = res + f", birthday: {self.birthday}"
        if str(self.email) != "None":
            res = res + f", email: {self.email}"
        return res

    def phones_list(self):
        res = f"{', '.join(str(p) for p in self.phones)}"
        return res

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def find_phone(self, phone: str) -> str:
        for item in self.phones:
            if item == phone:
                return item

    def edit_phone(self, old_phone: str, new_phone: str):
        for phone in self.phones:
            if phone == old_phone:
                phone.set_phone(new_phone)
    
    def edit_email(self, email: str):
        self.email = Email(email)

    def remove_phone(self, phone: str):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)

    def add_birthday(self, birthday) -> str:
        self.birthday = Birthday(birthday)
    
    def add_email(self, email) -> str:
        self.email = Email(email)

    def to_json(self) -> dict:
        phones = []
        for item in self.phones:
            phones.append(str(item))
        return {
            "name": str(self.name),
            "phones": phones,
            "birthday": str(self.birthday),
            "email": str(self.email),
        }
