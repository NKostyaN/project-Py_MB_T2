from modules.note import Note


class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str, tags:list[str]):     # it was changed # type: ignore
        self.notes.append(Note(title, text, tags))

    def edit_note(self, title: str, new_text: str):
        for i in self.notes:
            if i.title == title:
                i.text = new_text

    def remove_note(self, title: str):
        for i in self.notes:
            if i.title == title:
                self.notes.remove(i)

    def find_by_title(self, title: str) -> Note:
        for note in self.notes:
            if title in note.title:
                return note

    def to_json(self) -> dict:
        res = {}
        for item in self.notes:
            res.update({item.title: item.text})
        return res
