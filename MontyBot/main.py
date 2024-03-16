try:
    from MontyBot.helpers.monty_utils import highlight, show_help
except ImportError:
    from helpers.monty_utils import highlight, show_help
try:
    from MontyBot.helpers.monty_data_handler import load_from_json, save_to_json
except ImportError:
    from helpers.monty_data_handler import load_from_json, save_to_json
try:
    from MontyBot.modules import monty_assistant as bot
except ImportError:
    
    from modules import monty_assistant as bot
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def parse_input(user_input) -> str:
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
    except:
        cmd = ""
        args = ""
    return cmd, *args


def main():
    words = WordCompleter(["hello", "hi", "close", "exit", "quit", "bye", "add",
                           "add-birthday", "add-address", "add-email", "add-note",
                           "edit", "edit-birthday", "edit-email", "edit-note",
                           "find-contact", "find-phone", "find-email", "find-address", "find-note",
                           "rename", "remove", "remove-phone", "remove-note",
                           "birthdays", "show-birthday", "show-email",
                           "all", "all-notes", "help", "?"])
    
    book = load_from_json("MontyBot_phonebook.json", "phonebook")
    notes = load_from_json("MontyBot_notes.json", "notebook")
    dirty = False

    print("\nWelcome to the assistant bot!")
    while True:
        user_input = prompt("\nEnter a command:> ", completer = words, complete_while_typing = True)
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit", "bye"]:
            if dirty:
                save_to_json(book.to_json(), "MontyBot_phonebook.json")
                save_to_json(notes.to_json(), "MontyBot_notes.json")
            print("Good bye!")
            break

        elif command in ["hello", "hi"]:
            print(f"Hello, my name is {highlight("Monty")}. How can I help you?")

        elif command == "add":
            dirty = True
            print(bot.add_contact(args, book))

        elif command == "add-birthday":
            dirty = True
            print(bot.add_birthday(args, book))

        elif command == "add-address":
            dirty = True
            print(bot.add_address(args, book))

        elif command == "add-email":
            dirty = True
            print(bot.add_email(args, book))

        elif command == "edit":
            dirty = True
            print(bot.edit_contact(args, book))
            
        elif command == "edit-birthday":
            dirty = True
            print(bot.edit_birthday(args, book))
            
        elif command == "edit-email":
            dirty = True
            print(bot.edit_email(args, book))

        elif command == "rename":
            dirty = True
            print(bot.rename_contact(args, book))

        elif command == "remove-phone":
            dirty = True
            print(bot.remove_phone(args, book))

        elif command == "remove":
            dirty = True
            print(bot.remove_contact(args, book))

        elif command == "birthdays":
            bot.birthdays(args, book)

        elif command == "show-birthday":
            print(bot.show_birthday(args, book))

        elif command == "show-email":
            print(bot.show_email(args, book))

        elif command == "find-contact":
            print(bot.find_contact(args, book))

        elif command == "find-phone":
            print(bot.find_phone(args, book))

        elif command == "find-email":
            print(bot.find_email(args, book))
        
        elif command == "find-address":
            print(bot.find_address(args, book))

        elif command == "all":
            print(bot.show_all_contacts(book))

        elif command == "add-note":
            dirty = True
            print(bot.add_note(args, notes))

        elif command == "edit-note":
            dirty = True
            print(bot.edit_note(args, notes))

        elif command == "remove-note":
            dirty = True
            print(bot.remove_note(args, notes))

        elif command == "find-note":
            print(bot.find_note(args, notes))

        elif command == "all-notes":
            dirty = True
            print(bot.show_all_notes(notes))

        elif command in ["help", "?"]:
            print(show_help())
        
        else:
            print(
                f"Invalid command. Use {highlight("help")} or {
                    highlight("?")} to see all available commands."
            )


if __name__ == "__main__":
    main()
