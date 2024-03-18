try:
    from MontyBot.helpers.monty_utils import yellow, cyan, warning, info, get_birthdays_per_week, check_phone, check_email
except ImportError:
    from helpers.monty_utils import yellow, cyan, warning, info, get_birthdays_per_week, check_phone, check_email
try:
    from .address_book import AddressBook
except ImportError:
    from address_book import AddressBook
try:
    from .record import Record
except ImportError:
    from record import Record
try:
    from .notebook import NoteBook
except ImportError:
    from notebook import NoteBook


def input_error(func) -> str:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_string = f"{warning(f"Error in {func.__name__}:")} {e}\n"
            if str(func.__name__) == "add_contact":
                error_string += f"Please use {yellow("add")} {cyan("[username] [phone]")}.\n"
            elif str(func.__name__) == "add_email":
                error_string += f"Please use {yellow("add-email")} {cyan("[username] [email]")}.\n"
            elif str(func.__name__) == "add_birthday":
                error_string += f"Please use {yellow("add-birthday")} {cyan("[username] [birthday]")}.\n"
            elif str(func.__name__) == "add_address":
                error_string += f"Please use {yellow("add-address")} {cyan("[username]")}.\n"
            elif str(func.__name__) == "add_note":
                error_string += f"Please use {yellow("add-note")} {cyan("[title] [note]")}.\n"
            elif str(func.__name__) == "add_tags":
                error_string += f"Please use {yellow("add-tag")} {cyan("[title] [tags]")}.\n"
            elif str(func.__name__) == "edit_contact":
                error_string += f"Please use {yellow("edit")} {cyan("[username] [old phone] [new phone]")}.\n"
            elif str(func.__name__) == "edit_email":
                error_string += f"Please use {yellow("edit-email")} {cyan("[username] [new email]")}.\n"
            elif str(func.__name__) == "edit_birthday":
                error_string += f"Please use {yellow("edit-birthday")} {cyan("[username] [birthday]")}.\n"
            elif str(func.__name__) == "edit_note":
                error_string += f"Please use {yellow("edit-note")} {cyan("[title] [note]")}.\n"
            elif str(func.__name__) == "rename_contact":
                error_string += f"Please use {yellow("rename")} {cyan("[username] [new phone]")}.\n"
            elif str(func.__name__) == "show_email":
                error_string += f"Please use {yellow("show-email")} {cyan("[username]")}.\n"
            elif str(func.__name__) == "show_birthday":
                error_string += f"Please use {yellow("show-birthday")} {cyan("[username]")}.\n"
            elif str(func.__name__) == "find_contact":
                error_string += f"Please use {yellow("find-contact")} {cyan("[username]")}.\n"
            elif str(func.__name__) == "find_phone":
                error_string += f"Please use {yellow("find-phone")} {cyan("[phone]")}.\n"
            elif str(func.__name__) == "find_email":
                error_string += f"Please use {yellow("find-email")} {cyan("[email]")}.\n"
            elif str(func.__name__) == "find_address":
                error_string += f"Please use {yellow("find-address")} {cyan("[address]")}.\n"
            elif str(func.__name__) == "find_note":
                error_string += f"Please use {yellow("find-note")} {cyan("[title]")}.\n"
            elif str(func.__name__) == "find_tags":
                error_string += f"Please use {yellow("find-tags")} {cyan("[tags]")}.\n"
            elif str(func.__name__) == "remove_contact":
                error_string += f"Please use {yellow("remove")} {cyan("[username]")}.\n"
            elif str(func.__name__) == "remove_phone":
                error_string += f"Please use {yellow("remove-phone")} {cyan("[username] [phone]")}.\n"
            elif str(func.__name__) == "remove_note":
                error_string += f"Please use {yellow("remove-note")} {cyan("[title]")}.\n"

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
            return f"Contact {yellow(name)} already have {cyan(phone)} phone.\n"
        else:
            rec.add_phone(phone)
            return f"Contact {yellow(name)} updated with {cyan(phone)} phone.\n"
    else:
        rec = Record(name)
        rec.add_phone(phone)
        book.add_record(rec)
        return f"Contact {yellow(name)} added.\n"


@input_error
def edit_contact(args, book: AddressBook) -> str:
    name, phone_old, phone_new = args
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        rec.edit_phone(phone_old, phone_new)
        return f"Contact {yellow(name)} updated.\n"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


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
            if str(rec.email) != "None":
                new_rec.add_email(str(rec.email))
            if str(rec.address) != "None":
                new_rec.add_address(str(rec.address))
            book.add_record(new_rec)
            book.delete(name)
            return f"Contact {yellow(name)} now have new name {yellow(new_rec.name)}.\n"
        else:
            return f"Contact name {yellow(name)} equal new name {yellow(new_name)}.\n"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


@input_error
def remove_contact(args, book: AddressBook) -> str:
    name = args[0]
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        book.delete(name)
        return f"Contact {yellow(name)} was removed from phonebook.\n"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


@input_error
def find_contact(args, book: AddressBook) -> str:
    name = args[0]
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        return rec
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


@input_error
def find_phone(args, book: AddressBook) -> str:
    phone = args[0]
    phone = check_phone(phone)
    found = []
    for key, rec in book.items():
        for item in rec.phones:
            if phone == str(item):
                found.append(rec)
    if found:
        res = ""
        for item in found:
            res += f"{str(item)}"
        return res
    else:
        return f"Phone {phone} not found.\n"
    

@input_error
def find_email(args, book: AddressBook) -> str:       # find email
    email = args[0]
    email = check_email(email)
    found = []
    for key, rec in book.items():
        if email == rec.email:
            found.append(rec)
    if found:
        res = ""
        for item in found:
            res += f"{str(item)}"
        return res
    else:
        return f"Email {cyan(email)} not found.\n"


@input_error
def remove_phone(args, book: AddressBook) -> str:
    name, phone = args
    name = name.capitalize()
    rec = book.find(name)
    found = False
    if rec:
        for item in rec.phones:
            if phone == str(item):
                rec.remove_phone(phone)
                found = True
                return f"{cyan(phone)} phone removed from {yellow(name)}.\n"
        if found:
            return f"Contact {yellow(name)} does not have {cyan(phone)} phone.\n"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


@input_error
def add_birthday(args, book: AddressBook) -> str:
    name, bday = args
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        rec.add_birthday(bday)
        if str(rec.birthday) != "None":
            return f"Birthday added, contact {yellow(name)} updated.\n"
        else:
            return ""
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


@input_error
def add_address(args, book: AddressBook) -> str:   # adding address to AddressBook
    name = args[0]
    name = name.capitalize()
    address = " ".join(args[1:])
    if not address:
        return "Please provide a valid address.\n"
    rec = book.find(name)
    if rec:
        rec.add_address(address)
        return f"Address added to contact {yellow(name)}.\n"


@input_error
def edit_birthday(args, book: AddressBook) -> str:
    name, bday = args
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        rec.add_birthday(bday)
        if str(rec.birthday) != "None":
            return f"Birthday changed, contact {yellow(name)} updated.\n"
        else:
            return ""
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


@input_error
def add_email(args, book: AddressBook) -> str:            # add new email
    name, email = args
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        rec.add_email(email)
        if str(rec.email) != "None":
            return f"Email added, contact {yellow(name)} updated.\n"
        else:
            return ""
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


@input_error
def edit_email(args, book: AddressBook) -> str:          # change user's email
    name, email_new = args
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        rec.edit_email(email_new)
        return f"Email changed, contact {yellow(name)} updated.\n"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


@input_error
def show_birthday(args, book: AddressBook) -> str:      # show email of user
    name = args[0]
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        return f"{yellow(f"{name}'s")} birthday is: {cyan(str(book.get(name).birthday))}.\n"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


@input_error
def show_email(args, book: AddressBook) -> str:          # show email of user
    name = args[0]
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        return f"{yellow(f"{name}'s")} email is: {cyan(str(book.get(name).email))}.\n"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling.\n"


@input_error
def birthdays(args, book: AddressBook) -> str:
    days = int(args[0]) if args else 7
    days = 7 if days < 1 else days
    phonebook = []
    for name in book.keys():
        if str(book.get(name).birthday) != "None":
            phonebook.append({name: str(book.get(name).birthday)})
    return get_birthdays_per_week(phonebook, days)


@input_error
def find_address(args, book: AddressBook) -> str:  # finding contacts with some address
    address = args
    found = []
    for key, rec in book.items():
        for item in address:
            if item in str(rec.address):
                if not (rec in found):
                    found.append(rec)
    if found:
        res = ""
        for item in found:
            res += f"{str(item)}"
        return res
    else:
        return f"Address {cyan(address)} not found.\n"


@input_error
def add_note(args, notes: NoteBook) -> str:
    """
    Generates a new note in the given NoteBook object 
    if the note title does not already exist.
    """
    title = args[0]
    title = title.capitalize()
    text = " ".join(args[1:])
    note = notes.find_by_title(title)
    if note:
        return f"Note {yellow(title)} already exist. Use {cyan("edit-note")} instead.\n"
    else:
        notes.add_note(title, text, "")
        note = notes.find_by_title(title)
        tags_input = str(input("Any tags?:->"))
        if tags_input != "":
            note.tags = tags_input
        else:
            note.tags = ""
        return f"Note {yellow(title)} has been added.\n"
    
@input_error
def add_tags(args, notes: NoteBook) -> str:
    """Adding tags to the note"""
    title = args[0]
    title = title.capitalize()
    tags = " ".join(args[1:])
    note = notes.find_by_title(title)
    if note:
        note.tags = tags
        return f"Tags added to note with title {yellow(title)}.\n"
    else:
        return f"Note with title {yellow(title)} not found.\n"


@input_error
def edit_note(args, notes: NoteBook) -> str:
    """Edit a note in the notebook."""
    title = args[0]
    title = title.capitalize()
    new_text = " ".join(args[1:])
    note = notes.find_by_title(title)
    if note:
        notes.edit_note(title, new_text)
        tags_input = str(input("Any tags?:->"))
        if tags_input != "":
            note.tags = tags_input
        else:
            note.tags = ""
        return f"Note {yellow(title)} has been edited.\n"
    else:
        return f"Note with title {yellow(title)} not found.\n"


@input_error
def remove_note(args, notes: NoteBook) -> str:
    """Remove a note from the given NoteBook by title."""
    title = args[0]
    title = title.capitalize()
    if notes.find_by_title(title):
        notes.remove_note(title)
        return f"Note {yellow(title)} has been deleted.\n"
    else:
        return f"Note with title {yellow(title)} not found.\n"


@input_error
def find_note(args, notes: NoteBook) -> str:
    """A function to find a note by title in a given NoteBook."""
    title = args[0]
    title = title.capitalize()
    note = notes.find_by_title(title)
    if note:
        return str(note)
    else:
        return f"Note with title {yellow(title)} not found.\n"


@input_error
def find_tags(args, notes: NoteBook) -> str:
    """A function to find a note by tag in a given NoteBook."""
    found = []
    for item in notes.notes:
        for arg in args:
            if arg in item.tags:
                found.append(item)
    if found:
        res = ""
        for item in found:
            res += str(item)
        return res
    else:
        return f"Note with tags {yellow(args)} not found.\n"


@input_error
def show_all_contacts(book: AddressBook) -> str:
    phonebook = ""
    for name in book.keys():
        rec = book.get(name)
        user = f"\n{info("--- ")}{yellow(name)} {info("-"*(40-len(name)))}"
        phones = f"\nphones: {cyan(rec.phones_list())}"
        bday = f"\nbirthday: {cyan(rec.birthday)}" if str(
            rec.birthday) != "None" else ""
        user_email = f"\nemail: {cyan(rec.email)}" if str(
            rec.email) != "None" else ""
        adr = f"\naddress: {rec.address}" if str(rec.address) != "None" else ""
        phonebook += f"{user}{phones}{bday}{user_email}{adr}\n"
    if phonebook == "":
        return "Phonebook is empty.\n"
    else:
        return phonebook


@input_error
def show_all_notes(notes: NoteBook) -> str:
    """
    A function that takes a NoteBook object as input 
    and generates a string containing all notes with formatting.
    """
    res = ""
    for note in notes.notes:
        res += str(note)
    return res
