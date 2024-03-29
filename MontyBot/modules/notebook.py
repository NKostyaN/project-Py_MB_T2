try:
    from MontyBot.modules.note import Note
except ImportError:
    from modules.note import Note


class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str, tags: str):
        self.notes.append(Note(title, text, tags))

    def edit_note(self, title: str, new_text: str):
        for i in self.notes:
            if i.title == title:
                i.text = new_text

    def remove_note(self, title: str):
        for i in self.notes:
            if i.title == title:
                self.notes.remove(i)

    def find_by_title(self, title: str) -> Note:  # find note by title
        for note in self.notes:
            if title in note.title:
                return note

    def to_json(self) -> dict:  # convert data for json
        res = {}
        for item in self.notes:
            value = []
            value.append(item.text)
            value.append(item.tags)
            res.update({item.title: value})
        return res
