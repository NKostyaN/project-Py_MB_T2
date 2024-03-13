from note import Note
from datetime import datetime



class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str) -> str:
        self.notes.append(Note(title.capitalize(), text))
        print(f'Note {title} has been added.')

    def change_note_title(self, old_title: str, new_title: str) -> str:
        for note in self.notes:
            if note.title == old_title.capitalize():
                note.title = new_title.capitalize()
                print(f'Title {old_title} has been changed to title {new_title}.')
            else:
                print(f'Title {old_title} wasn\'t found.')

    def edit_note_text(self, title: str, new_text: str) -> str:
        for note in self.notes:
            if note.title == title.capitalize():
                note.text = new_text
                print(f'{title} text has been edited.')
            else:
                print('Note with the specified title not found.')

    def remove_note(self, title: str):
        for note in self.notes:
            if note.title == title.capitalize():
                self.notes.remove(note)
                print('Note has been deleted.')
            else:
                print(f'Title {title} wasn\'t found.')

    def show_notes(self) -> str:
        if self.notes:
            print('\nYour notes:\n')
            for note in self.notes:
                print(f'Title: {note.title}\nText: {note.text}\nCreation date: {note.creation_date}\n')
        else:
            print('\nYou have no notes.')

    def search_by_title(self, title: str) -> str:
        found_notes = []
        for note in self.notes:
            if title.capitalize() in note.title:
                found_notes.append(note)
        if found_notes:
            print('\nFound notes:')
            for note in found_notes:
                print(f'Title: {note.title}\nText: {note.text}\nCreation date: {note.creation_date}\n')
        else:
            print(f'\nTitle {title} wasn\'t found.')

    def search_by_date(self, date: str) -> str:
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            found_notes = [note for note in self.notes if date.date() == note.creation_date.date()]
            if found_notes:
                print('\nFound notes:')
                for note in found_notes:
                    print(f'Title: {note.title}\nText: {note.text}\nCreation date: {note.creation_date}\n')
            else:
                print('\nNotes with the specified date not found.')
        except ValueError:
            print('Incorrect date format.')



def show_menu():
    print("\nChoose an action:")
    print("1. Show notes")
    print("2. Add a note")
    print("3. Edit a note title")
    print("4. Edit a note text")
    print("5. Delete a note")
    print("6. Search by title")
    print("7. Search by date")
    print("8. Exit")

def main():
    note_manager = NoteBook()

    while True:
        show_menu()
        choice = input("\nEnter the action number: ")

        if choice == '1':
            note_manager.show_notes()
        elif choice == '2':
            title = input("\nEnter the note title: ")
            text = input("Enter the note text: ")
            note_manager.add_note(title, text)
        elif choice == '3':
            old_title = input("\nEnter the note title what you want to edit: ")
            new_title = input("Enter the new note title: ")
            note_manager.change_note_title(old_title, new_title)
        elif choice == '4':
            title = input("\nEnter the note title to edit text: ")
            new_text = input("Enter the new text: ")
            note_manager.edit_note_text(title, new_text)
        elif choice == '5':
            title = input("\nEnter the note title to delete: ")
            note_manager.remove_note(title)
        elif choice == '6':
            title_str = input("\nEnter the title to search: ")
            note_manager.search_by_title(title_str)
        elif choice == '7':
            date_str = input("\nEnter the date to search (format: YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                note_manager.search_by_date(date)
            except ValueError:
                print('Incorrect date format.')
        elif choice == '8':
            print('Goodbye!')
            break
        else:
            print('Invalid input. Please try again.')

if __name__ == '__main__':
    main()
