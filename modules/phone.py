from helpers.monty_utils import strip_phone_number


class Phone():
    def __init__(self, phone: str):
        phone = strip_phone_number(phone)
        self.phone = phone

    def set_phone(self, phone: str):
        self.value = phone

    def __str__(self):
        return str(self.phone)
