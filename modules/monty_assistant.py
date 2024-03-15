from helpers.monty_utils import highlight, warning, get_birthdays_per_week, strip_phone_number
from modules.address_book import AddressBook
from modules.record import Record
from modules.notebook import NoteBook


def input_error(func) -> str:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_string = f"{warning(f"Error in {func.__name__}:")} {e}\n"
            if str(func.__name__) == "add_contact":
                error_string += f"Wrong arguments count, pls use {highlight("add [username] [phone]")}."
            elif str(func.__name__) == "change_contact":
                error_string += f"Wrong arguments count, pls use {highlight("change [username] [phone]")}."
            elif str(func.__name__) == "show_phone":
                error_string += (
                    f"Wrong arguments count, pls use {highlight("phone [username]")}."
                )
            return error_string

    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    phone = strip_phone_number(str(phone))
    rec = book.find(name)
    if rec:
        if rec.find_phone(phone) != None:
            return f"Contact {highlight(name)} already have {highlight(phone)} phone"
        else:
            rec.add_phone(phone)
            return f"Contact {highlight(name)} updated with {highlight(phone)} phone"
    else:
        rec = Record(name)
        rec.add_phone(phone)
        book.add_record(rec)
        return "Contact added."


@input_error
def change_contact(args, book: AddressBook) -> str:
    name, phone_old, phone_new = args
    rec = book.find(name)
    if rec:
        rec.edit_phone(phone_old, phone_new)
        return "Contact updated."
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."
    

@input_error
def rename_contact(args, book: AddressBook) -> str:
    name, new_name = args
    print(name, new_name)
    rec = book.find(name)
    if rec:
        new_rec = Record(new_name)
        for phone in rec.phones:
            new_rec.add_phone(str(phone))
        if str(rec.birthday) != "None":
            new_rec.add_birthday(str(rec.birthday))
        book.add_record(new_rec)
        book.delete(name)
        return f"Contact {highlight(name)} now have new name {highlight(new_rec.name)}"
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def remove_contact(args, book: AddressBook) -> str:
    name = args[0]
    rec = book.find(name)
    if rec:
        book.delete(name)
        return f"Contact {highlight(name)} was removed from phonebook"
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def show_phone(args, book: AddressBook) -> str:
    name = args[0]
    rec = book.find(name)
    if rec:
        return f"{highlight(f"{name}'s")} phones is: {highlight(rec.phones_list())}"
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."
    
@input_error
def remove_phone(args, book: AddressBook) -> str:
    name, phone = args
    rec = book.find(name)
    if rec:
        if rec.find_phone(phone) != None:
            rec.remove_phone(phone)
            return f"{highlight(phone)} phone removed from {highlight(name)}"
        else:
            return f"Contact {highlight(name)} does not have {highlight(phone)} phone"
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def add_birthday(args, book: AddressBook) -> str:
    name, bday = args
    rec = book.find(name)
    if rec:
        rec.add_birthday(bday)
        if str(rec.birthday) != "None":
            return f"Birthday added, contact {highlight(name)} updated."
        else:
            return ""
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def show_birthday(args, book: AddressBook) -> str:
    name = args[0]
    rec = book.find(name)
    if rec:
        return f"{highlight(f"{name}'s")} birthday is: {highlight(str(book.get(name).birthday))}"
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def birthdays(book: AddressBook) -> str:
    phonebook = []
    for name in book.keys():
        if str(book.get(name).birthday) != "None":
            phonebook.append({name : str(book.get(name).birthday)})
    return get_birthdays_per_week(phonebook)
    

def show_all(book: AddressBook) -> str:
    phonebook = ""
    for name in book.keys():
        rec = book.get(name)
        bday = f"; birthday: {highlight(rec.birthday)}" if str(rec.birthday) != "None" else ""
        phonebook += f"{highlight(name)}, phones: {highlight(rec.phones_list())}{bday}\n"
    if phonebook == "":
        return "Phonebook is empty."
    else:
        return phonebook
    
def add_note(args, notes: NoteBook) -> str:
    title = args[0]
    text = ""
    for i in args[1: ]:
        text += i
    rec = notes.find_by_title(title)
    if rec:
        return f"Note {title} already exist."
    else:
        notes.add_note(title.capitalize(), text)
        return f"Note {title} has been added."

def change_note(args, notes: NoteBook) -> str:
    title, new_text = args
    if notes.find_by_title(title):
        notes.edit_note(title, new_text)
        return f"Note {highlight(title)} has been edited."
    else:
        return f"Note with title {highlight(title)} not found."

def delete_note(args, notes: NoteBook) -> str:
    title = args[0]
    if notes.find_by_title(title):
        notes.remove_note(title)
        return f"Note {highlight(title)} has been deleted."
    else:
        return f"Note with title {highlight(title)} not found."

def find_note(args, notes: NoteBook) -> str:
    title = args[0]
    res = notes.find_by_title(title)
    if res:
        return f"{title}: {res.text}"
    else:
        return f"Note with title {highlight(title)} not found."