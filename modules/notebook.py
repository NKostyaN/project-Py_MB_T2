from modules.note import Note


class NoteBook:
    def __init__(self):
        self.notes = {}

    def add_note(self, title: str, text: str) -> str:
        note_id = len(self.notes) + 1
        self.notes[note_id] = Note(title, text)
        print('New note has been added.')


    def edit_note(self, note_id: int, new_title: str, new_text: str) -> str:
        if note_id in self.notes:
            self.notes[note_id].title = new_title
            self.notes[note_id].text = new_text
            print('Note has been edited .')
        else:
            print('Note with the specified ID not found.')

    def delete_note(self, note_id: int) -> str:
        if note_id in self.notes:
            del self.notes[note_id]
            print('Note has been deleted.')
        else:
            print('Note with the specified ID not found.')
            
    def show_notes(self) -> str:
        if self.notes:
            print('\nYour notes:')
            for note_id, note_obj in self.notes.items():
                print(f'{note_id}. {note_obj.title} - Created at: {note_obj.created_at}')
        else:
            print('\nYou have no notes.')

    def search_by_title(self, title_str):
        found_notes = []
        for note_id, note_obj in self.notes.items():
            if title_str.lower() in note_obj.title.lower():
                found_notes.append((note_id, note_obj))
        if found_notes:
            print('\nFound notes:')
            for note_id, note_obj in found_notes:
                print(f'{note_id}. {note_obj.title} - Created at: {note_obj.created_at}')
        else:
            print('\nNotes with the specified title not found.')

    def search_by_date(self, date):
        found_notes = []
        for note_id, note_obj in self.notes.items():
            if date.date() == note_obj.created_at.date():
                found_notes.append((note_id, note_obj))
        if found_notes:
            print('\nFound notes:')
            for note_id, note_obj in found_notes:
                print(f'{note_id}. {note_obj.title} - Created at: {note_obj.created_at}')
        else:
            print('\nNotes with the specified date not found.')

