try:
    from MontyBot.helpers.monty_utils import yellow, cyan, warning, get_birthdays_per_week, check_phone, check_email
except ImportError:
    from helpers.monty_utils import yellow, cyan, warning, get_birthdays_per_week, check_phone, check_email
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
                error_string += f"Wrong arguments count, pls use {yellow("add")} {cyan("[username] [phone]")}."
            elif str(func.__name__) == "edit_contact":
                error_string += f"Wrong arguments count, pls use {yellow("edit")} {cyan("[username] [old phone] [new phone]")}."
            elif str(func.__name__) == "show_phone":
                error_string += (
                    f"Wrong arguments count, pls use {cyan("phone [username]")}."
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
            return f"Contact {yellow(name)} already have {cyan(phone)} phone"
        else:
            rec.add_phone(phone)
            return f"Contact {yellow(name)} updated with {cyan(phone)} phone"
    else:
        rec = Record(name)
        rec.add_phone(phone)
        book.add_record(rec)
        return "Contact added."


@input_error
def edit_contact(args, book: AddressBook) -> str:
    name, phone_old, phone_new = args
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        rec.edit_phone(phone_old, phone_new)
        return "Contact updated."
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."


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
            return f"Contact {yellow(name)} now have new name {cyan(new_rec.name)}"
        else:
            return f"Contact name {yellow(name)} equal new name {cyan(new_name)}"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."


@input_error
def remove_contact(args, book: AddressBook) -> str:
    name = args[0]
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        book.delete(name)
        return f"Contact {yellow(name)} was removed from phonebook"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."


@input_error
def find_contact(args, book: AddressBook) -> str:
    name = args[0]
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        return rec
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."


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
            res += f"{str(item)}"
        return res
    else:
        return f"Phone {phone} not found"


@input_error
def find_email(args, book: AddressBook) -> str:
    email = args[0]
    email = check_email(email)
    finded = []
    for key, rec in book.items():
        if email == rec.email:
            finded.append(rec)
    if finded:
        res = ""
        for item in finded:
            res += f"{str(item)}"
        return res
    else:
        return f"Email {cyan(email)} not found"
    

@input_error
def find_note(args, notes: NoteBook) -> str:
    title = args[0]
    for item in notes:
        if title == item.title:
            return item.title, item.text
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
            return f"{cyan(phone)} phone removed from {yellow(name)}"
        else:
            return f"Contact {yellow(name)} does not have {cyan(phone)} phone"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."


@input_error
def add_birthday(args, book: AddressBook) -> str:
    name, bday = args
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        rec.add_birthday(bday)
        if str(rec.birthday) != "None":
            return f"Birthday added, contact {yellow(name)} updated."
        else:
            return ""
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."
    

@input_error
def add_address(args, book: AddressBook) -> str:
    name = args[0]
    address = " ".join(args[1:]) 
    if not address:
        return "Please provide a valid address."
    rec = book.find(name)
    if rec:
        rec.add_address(address)
        return f"Address added to contact {yellow(name)}."
    
    
@input_error
def edit_birthday(args, book: AddressBook) -> str:
    name, bday = args
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        rec.add_birthday(bday)
        if str(rec.birthday) != "None":
            return f"Birthday changed, contact {yellow(name)} updated."
        else:
            return ""
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."


@input_error
def add_email(args, book: AddressBook) -> str:
    name, email = args
    rec = book.find(name)
    if rec:
        rec.add_email(email)
        if str(rec.email) != "None":
            return f"Email added, contact {yellow(name)} updated."
        else:
            return ""
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."


@input_error
def edit_email(args, book: AddressBook) -> str:
    name, email_new = args
    rec = book.find(name)
    if rec:
        rec.edit_email(email_new)
        return f"Email changed, contact {yellow(name)} updated."
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."


@input_error
def show_birthday(args, book: AddressBook) -> str:
    name = args[0]
    name = name.capitalize()
    rec = book.find(name)
    if rec:
        return f"{cyan(f"{name}'s")} birthday is: {cyan(str(book.get(name).birthday))}"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."


@input_error
def show_email(args, book: AddressBook) -> str:
    name = args[0]
    rec = book.find(name)
    if rec:
        return f"{cyan(f"{name}'s")} email is: {cyan(str(book.get(name).email))}"
    else:
        return f"Contact {yellow(name)} does not exist. Check your spelling."


@input_error
def birthdays(args, book: AddressBook) -> str:
    days = int(args[0]) if args else 7
    days = 7 if days < 1 else days
    phonebook = []
    for name in book.keys():
        if str(book.get(name).birthday) != "None":
            phonebook.append({name : str(book.get(name).birthday)})
    return get_birthdays_per_week(phonebook, days)


@input_error
def find_address(args, book: AddressBook) -> str:
    name = args[0]
    rec = book.find(name)
    if rec:
        if rec.address:
            return f"Address for {yellow(name)}: {cyan(rec.address)}"
        else:
            return f"No address found for {yellow(name)}."
    else:
        return f"Contact {yellow(name)} does not exist."

@input_error
def add_note(args, notes: NoteBook) -> str:
    title = args[0]
    text = " ".join(args[1:])
    if notes.find_by_title(title):
        return f"Note {cyan(title)} already exist."
    else:
        notes.add_note(title, text)
        return f"Note {cyan(title)} has been added."


@input_error
def edit_note(args, notes: NoteBook) -> str:
    title = args[0]
    new_text = " ".join(args[1:])
    if notes.find_by_title(title):
        notes.edit_note(title, new_text)
        return f"Note {cyan(title)} has been edited."
    else:
        return f"Note with title {cyan(title)} not found."


def remove_note(args, notes: NoteBook) -> str:
    title = args[0]
    if notes.find_by_title(title):
        notes.remove_note(title)
        return f"Note {cyan(title)} has been deleted."
    else:
        return f"Note with title {cyan(title)} not found."


@input_error
def find_note(args, notes: NoteBook) -> str:
    title = args[0]
    res = notes.find_by_title(title)
    if res:
        return str(res.text)
    else:
        return f"Note with title {cyan(title)} not found."


@input_error
def show_all_contacts(book: AddressBook) -> str:
    phonebook = ""
    for name in book.keys():
        rec = book.get(name)
        phones = f"\nphones: {cyan(rec.phones_list())}"
        bday = f"\nbirthday: {cyan(rec.birthday)}" if str(rec.birthday) != "None" else ""
        user_email = f"\nemail: {cyan(rec.email)}" if str(rec.email) != "None" else ""
        adr = f"\naddress: {rec.address}" if str(rec.address) != "None" else ""
        phonebook += f"\n{"--- "}{yellow(name)} {"-"*40}{phones}{bday}{user_email}{adr}\n"
    phonebook += f"{"-"*40}\n"
    if phonebook == "":
        return "Phonebook is empty."
    else:
        return phonebook
    

@input_error
def show_all_notes(notes: NoteBook) -> str:
    res = ""
    for note in notes.notes:
        res += f"\n{"--- "}{yellow(note.title)} ---\n{note.text}\n"
    return res
