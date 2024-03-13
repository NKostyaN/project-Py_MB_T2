from datetime import datetime

class Note():
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.creation_date = datetime.now()

    def __str__(self):
        return f"\
        Title: {str(self.title)}\n\
        Text: {str(self.text)}\n\
        Creation date: {str(self.creation_date)}"
    