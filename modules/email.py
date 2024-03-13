from helpers.monty_utils import check_email


class Email():
    def __init__(self, email="None"):
        email = check_email(email)
        self.email = email

    def __str__(self):
        return str(self.email)
