from helpers.monty_utils import highlight, warning, get_birthdays_per_week, check_phone
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
                error_string += f"Wrong arguments count, pls use {
                    highlight("add [username] [phone]")}."
            elif str(func.__name__) == "change_contact":
                error_string += f"Wrong arguments count, pls use {
                    highlight("change [username] [phone]")}."
            elif str(func.__name__) == "show_phone":
                error_string += (
                    f"Wrong arguments count, pls use {
                        highlight("phone [username]")}."
                )
            return error_string

    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    name = name.capitalize()
    phone = check_phone(str(phone))
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
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        rec.edit_phone(phone_old, phone_new)
        return "Contact updated."
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def rename_contact(args, book: AddressBook) -> str:
    name, new_name = args
    name = name.capitalize()
    new_name = new_name.capitalize()
    rec = book.find(name)
    if rec:
        if name != new_name:
            new_rec = Record(new_name)
            for phone in rec.phones:
                new_rec.add_phone(str(phone))
            if str(rec.birthday) != "None":
                new_rec.add_birthday(str(rec.birthday))
            book.add_record(new_rec)
            book.delete(name)
            return f"Contact {highlight(name)} now have new name {highlight(new_rec.name)}"
        else:
            return f"Contact name {highlight(name)} equal new name {highlight(new_name)}"
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def remove_contact(args, book: AddressBook) -> str:
    name = args[0]
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        book.delete(name)
        return f"Contact {highlight(name)} was removed from phonebook"
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def find_contact(args, book: AddressBook) -> str:
    name = args[0]
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        return rec
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def find_phone(args, book: AddressBook) -> str:
    phone = args[0]
    phone = check_phone(phone)
    finded = []
    for key, rec in book.items():
        for item in rec.phones:
            if phone == str(item):
                finded.append(rec)
    if finded:
        res = ""
        for item in finded:
            res += f"{str(item)}\n"
        return res
    else:
        return f"Phone {phone} not found"


@input_error
def find_email(args, book: AddressBook) -> str:
    email = args[0]
    # email = check_email(email)          # need to add check email from Serg
    finded = []
    for key, rec in book.items():
        if email == rec.email:
            finded.append(rec)
    if finded:
        res = ""
        for item in finded:
            res += f"{str(item)}\n"
        return res
    else:
        return f"Email {email} not found"
    

@input_error
def find_note(args, book: AddressBook) -> str:
    title = args[0]
    # email = check_email(email)            # need to add check email from Serg
    for key, rec in book.items():           # neet to change to notes.items() from Slava
        if title == rec.title:
            return rec                      # note.__str__()
        else:
            return f"Note {title} not found"
    
    
@input_error
def remove_phone(args, book: AddressBook) -> str:
    name, phone = args
    name = name.capitalize()
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
    name = name.capitalize()
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
def change_birthday(args, book: AddressBook) -> str:
    name, bday = args
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        rec.add_birthday(bday)
        if str(rec.birthday) != "None":
            return f"Birthday changed, contact {highlight(name)} updated."
        else:
            return ""
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def add_email(args, book: AddressBook) -> str:
    name, email = args
    rec = book.find(name)
    if rec:
        rec.add_email(email)
        if str(rec.email) != "None":
            return f"Email added, contact {highlight(name)} updated."
        else:
            return ""
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def change_email(args, book: AddressBook) -> str:
    name, email_new = args
    rec = book.find(name)
    if rec:
        rec.edit_email(email_new)
        return f"Email changed, contact {highlight(name)} updated."
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def show_birthday(args, book: AddressBook) -> str:
    name = args[0]
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        return f"{highlight(f"{name}'s")} birthday is: {highlight(str(book.get(name).birthday))}"
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def show_email(args, book: AddressBook) -> str:
    name = args[0]
    rec = book.find(name)
    if rec:
        return f"{highlight(f"{name}'s")} email is: {highlight(str(book.get(name).email))}"
    else:
        return f"Contact {highlight(name)} does not exist. Check your spelling."


@input_error
def birthdays(args, book: AddressBook) -> str:
    days = int(args[0]) if args else 7
    days = 7 if days < 1 else days
    phonebook = []
    for name in book.keys():
        if str(book.get(name).birthday) != "None":
            phonebook.append({name : str(book.get(name).birthday)})
    return get_birthdays_per_week(phonebook, days)
    

def show_all(book: AddressBook) -> str:
    phonebook = ""
    for name in book.keys():
        rec = book.get(name)
        bday = f"; birthday: {highlight(rec.birthday)}" if str(
            rec.birthday) != "None" else ""
        user_email = f"; email: {highlight(rec.email)}" if str(
            rec.email) != "None" else ""
        phonebook += f"{highlight(name)}, phones: {highlight(rec.phones_list())}{
            bday}{user_email}\n"
    if phonebook == "":
        return "Phonebook is empty."
    else:
        return phonebook


def add_note(args, notes: NoteBook) -> str:
    title = args[0]
    text = " ".join(args[1:])
    if notes.find_by_title(title):
        return f"Note {title} already exist."
    else:
        notes.add_note(title, text)
        return f"Note {title} has been added."


def change_note(args, notes: NoteBook) -> str:
    title = args[0]
    new_text = " ".join(args[1:])
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
        return str(res.text)
    else:
        return f"Note with title {highlight(title)} not found."


def show_all_notes(notes: NoteBook) -> str:
    for note in notes.notes:
        print(f"Title: {highlight(note.title)}\nText: {note.text}\n")
