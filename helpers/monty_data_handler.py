import json
from helpers.monty_utils import info
from modules.address_book import AddressBook
from modules.record import Record
from modules.note import Note
from modules.notebook import NoteBook


def load_from_json(filename) -> AddressBook:
    if filename == "phonebook.json":
        phonebook = AddressBook()
        try:
            with open(filename, "r", encoding="utf-8 ") as f:
                data = json.load(f)
                if data != "":
                    for key in data.keys():
                        rec = Record(key)
                        for phone in data.get(key).get("phones"):
                            rec.add_phone(phone)
                        if str(data.get(key).get("birthday")) != "None":
                            rec.add_birthday(data.get(key).get("birthday"))
                        if str(data.get(key).get("email")) != "None":
                            rec.add_email(data.get(key).get("email"))
                        phonebook.add_record(rec)
                else:
                    Log.empty(filename)
        except FileNotFoundError:
            Log.not_found(filename)
        return phonebook
    else:
        notes = NoteBook()  
        try:
            with open(filename, "r", encoding="utf-8 ") as f:
                data = json.load(f)
                if data != "":
                   for key, value in data.items():
                       notes.add_note(key, value)
                else:
                    Log.empty(filename)
        except FileNotFoundError:
            Log.not_found(filename)
        return notes


def save_to_json(data: dict, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


class Log:
    @classmethod
    def empty(cls, filename):
        file_name = str(filename)
        str_info = "[INFO]: " + file_name + " file found, but it's empty for now."
        return print(f"{info(str_info)}")
    
    @classmethod
    def not_found(cls, filename):
        file_name = str(filename)
        str_info = "[INFO]: " + file_name + " file not found, but don't worry, I'll create a new one for you."
        return print(f"{info(str_info)}")
