from helpers.monty_utils import check_date


class Birthday():
    def __init__(self, birthday="None"):
        birthday = check_date(birthday)
        self.birthday = birthday

    def __str__(self):
        return str(self.birthday)
