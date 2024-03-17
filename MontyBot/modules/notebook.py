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
            
    def search_notes_by_tag(self, tag):
        found_notes = []
        for note in self.notes:
            if tag in note.tags:
                found_notes.append(note)
        return found_notes

    def sort_notes_by_tag(self, tag):
        sorted_notes = sorted(self.notes, key=lambda note: tag in note.tags)
        return sorted_notes


    # it was changed
    def to_json(self) -> dict:
        res = {}
        for item in self.notes:
            res[item.title] = {
                "text": item.text,
                "tags": item.tags  # Assuming 'tags' is an attribute of the note item
            }
        return res