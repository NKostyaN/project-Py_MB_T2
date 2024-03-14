import json
from helpers.monty_utils import info
from modules.address_book import AddressBook
from modules.record import Record
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
        notes = NoteBook()  #потрібно внести!!!
        try:
            with open(filename, "r", encoding="utf-8 ") as f:
                data = json.load(f)
                if data != "":
                    for key in data.keys():
                        rec = Record(key)
                        if str(data.get(key).get("title")) != "None":
                            rec.add_title(data.get(key).get("title"))
                        if str(data.get(key).get("text")) != "None":
                            rec.add_text(data.get(key).get("text"))
                        notes.add_record(rec)
                else:
                    Log.empty(filename)
        except FileNotFoundError:
            Log.not_found(filename)
        return notes



def save_to_json(data: dict, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


class Log:
    def empty(filename):
        return print(f"{info("[INFO]: {filename} file found, but it's empty for now.")}")

    def not_found(filename):
        return print(f"{
            info(
                "[INFO]: {filename} file not found, but don't worry, I'll create a new one for you."
            )}"
        )
