class Note():
    def __init__(self, title="None", text="None", tags=[]):
        self.title = title
        self.text = text
        self.tags = tags

    def __str__(self):
        return f"Title: {str(self.title)}\nText: {str(self.text)}\nTags: {', '.join(self.tags)}"