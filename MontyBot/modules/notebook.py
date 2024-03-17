from modules.note import Note


class NoteBook:
    def __init__(self):
        self.notes: list[Note] = []

    def add_note(self, note: Note):
        self.notes.append(note)

    def edit_note(self, title: str, new_text: str):
        for n in self.notes:
            if n.title == title:
                n.text = new_text

    def remove_note(self, title: str):
        self.notes = [n for n in self.notes if n.title != title]

    def find_by_title(self, title: str) -> Note:
        for n in self.notes:
            if n.title == title:
                return n

    def search_notes_by_tag(self, tag: str) -> list[Note]:
        return [n for n in self.notes if tag in n.tags]

    def sort_notes_by_tag(self, tag: str) -> list[Note]:
        return sorted(self.notes, key=lambda n: tag in n.tags)

    def to_json(self) -> dict:
        res = {}
        for n in self.notes:
            res[n.title] = {
                "text": n.text, "tags": n.tags
            }
        return res
