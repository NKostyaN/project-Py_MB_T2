class Note():
    def __init__(self, title = "None", text = "None", tag = ""):
        self.title = title
        self.text = text
        self.tags = tag

    def __str__(self):
        return f"Title: {str(self.title)}\nText: {str(self.text)}"