from helpers.monty_utils import check_phone


class Phone:
    def __init__(self, phone: str):
        phone = check_phone(phone)
        self.phone = phone

    def set_phone(self, phone: str):
        self.value = phone

    def __str__(self):
        return str(self.phone)
