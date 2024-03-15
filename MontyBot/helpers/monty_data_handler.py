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


def load_from_json() -> (
    AddressBook
):  # to do -->     def load_from_json(filename: str) -> AddressBook:
    phonebook = AddressBook()
    try:
        # with open(Path.home() / "MontyBot_phonebook.json", "r", encoding="utf-8 ") as f:          # use user path
        with open("MontyBot_phonebook.json", "r", encoding="utf-8 ") as f:
            data = json.load(f)
            if data != "":
                for key in data.keys():
                    rec = Record(key)
                    for phone in data.get(key).get("phones"):
                        rec.add_phone(phone)
                    if str(data.get(key).get("birthday")) != "None":
                        rec.add_birthday(data.get(key).get("birthday"))
                    phonebook.add_record(rec)
            else:
                Log.empty()
    except FileNotFoundError:
        Log.not_found()
    return phonebook


def save_to_json(
    data: dict,
):  # to do -->     def save_to_json(data: dict, filename: str):
    # with open(Path.home() / "MontyBot_phonebook.json", "w", encoding="utf-8") as f:               # use user path
    with open("MontyBot_phonebook.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


class Log:
    def empty():
        return print(info("[INFO]: Phonebook file found, but it's empty for now."))

    def not_found():
        return print(
            info(
                "[INFO]: Phonebook file not found, but don't worry, I'll create a new one for you."
            )
        )
