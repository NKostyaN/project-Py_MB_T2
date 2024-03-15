class Name:
    def __init__(self, name: str):
        name = name.capitalize()
        self.name = name

    def __str__(self):
        return str(self.name)
