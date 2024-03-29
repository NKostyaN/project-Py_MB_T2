from pathlib import Path
import json
try:
    from .monty_utils import info
except ImportError:
    from monty_utils import info
try:    
    from MontyBot.modules.address_book import AddressBook
except ImportError:
    from modules.address_book import AddressBook
try:
    from MontyBot.modules.record import Record
except ImportError:
    from modules.record import Record
try:
    from MontyBot.modules.notebook import NoteBook
except ImportError:
    from modules.notebook import NoteBook



def load_from_json(filename, key="phonebook"):
    if key == "phonebook":                                                           # load addressbook
        phonebook = AddressBook()
        try:
            with open(Path.home() / filename, "r", encoding="utf-8 ") as f:          # use user path
            # with open(filename, "r", encoding="utf-8 ") as f:                      # use local path
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
                        if str(data.get(key).get("address")) != "None":
                            rec.add_address(data.get(key).get("address"))
                        phonebook.add_record(rec)
                else:
                    Log.empty(filename)
        except FileNotFoundError:
            Log.not_found(filename)
        return phonebook
    else:                                                                            # load notes
        notes = NoteBook()  
        try:
            with open(Path.home() / filename, "r", encoding="utf-8 ") as f:          # use user path
            # with open(filename, "r", encoding="utf-8 ") as f:                      # use local path
                data = json.load(f)
                if data != "":
                   for key, value in data.items():
                       notes.add_note(key, value[0], value[1])
                else:
                    Log.empty(filename)
        except FileNotFoundError:
            Log.not_found(filename)
        return notes


def save_to_json(data: dict, filename):                                             # save addressbook or notes
    with open(Path.home() / filename, "w", encoding="utf-8") as f:                  # use user path
    # with open(filename, "w", encoding="utf-8") as f:                              # use local path
        json.dump(data, f, ensure_ascii=False, indent=4)


class Log:                                                                          # messages no file or empty file
    @classmethod
    def empty(cls, filename):
        return print(f"{info("[INFO]: " + str(filename) + " file found, but it's empty for now.")}")
    
    @classmethod
    def not_found(cls, filename):
        return print(f"{info("[INFO]: " + str(filename) + " file not found, but don't worry, I'll create a new one for you.")}")
