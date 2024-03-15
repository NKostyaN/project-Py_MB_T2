from modules.note import Note
import json


class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str):
        self.notes.append(Note(title, text))

    def edit_note(self, title: str, new_text: str):
        for note in self.notes:
            if note.title == title:
                note.text = new_text

    def remove_note(self, title: str):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)

    def find_by_title(self, title: str) -> Note:
        for note in self.notes:
            if title in note.title:
                return note
    @classmethod       
    def save_notes_to_json(self, filename: str):
        with open(filename, "w") as f:
            json.dump(self.notes, f)

    def load_notes_from_json(self, filename: str):
        with open(filename, "r") as f:
            self.notes = json.load(f)    