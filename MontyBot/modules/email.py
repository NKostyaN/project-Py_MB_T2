try:
    from MontyBot.helpers.monty_utils import check_email
except ImportError:
    from helpers.monty_utils import check_email


class Email():
    def __init__(self, email="None"):
        if check_email(email):
            email = check_email(email)
            self.email = email
        else:
            raise ValueError("Use e-mail format please\n")

    def __str__(self):
        return str(self.email)
