try:
    from MontyBot.helpers.monty_utils import check_email
except ImportError:
    from helpers.monty_utils import check_email


class Email:  # class email for addressbook
    def __init__(self, email="None"):
        if check_email(email):
            email = check_email(email)  # e-mail format validation
            self.email = email
        else:
            raise ValueError("Use e-mail format please\n")

    def __str__(self):
        return str(self.email)
