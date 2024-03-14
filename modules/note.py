class Note():
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __str__(self):
        return f"Title: {str(self.title)}\nText: {str(self.text)}"