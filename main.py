from helpers.monty_utils import highlight, show_help
from helpers.monty_data_handler import load_from_json, save_to_json
import modules.monty_assistant as bot
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
                           "change", "rename", "remove", "remove-phone", "add-birthday",
                           "show-birthday", "change-birthday", "birthdays", "find-contact",
                           "find-phone", "find-email", "find-note", "all", "help"])
    
    book = load_from_json("phonebook.json")
    notes = load_from_json("notes.json")
    dirty = False

    print("\nWelcome to the assistant bot!")
    while True:
        user_input = prompt("\nEnter a command:> ", completer = words)
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit", "bye"]:
            if dirty:
                save_to_json(book.to_json(), "phonebook.json")
                save_to_json(notes.to_json(), "notes.json")
            print("Good bye!")
            break

        elif command in ["hello", "hi"]:
            print(f"Hello, my name is {highlight("Monty")}. How can I help you?")

        elif command == "add":
            dirty = True
            print(bot.add_contact(args, book))

        elif command == "change":
            dirty = True
            print(bot.change_contact(args, book))

        elif command == "rename":
            dirty = True
            print(bot.rename_contact(args, book))

        elif command == "remove":
            dirty = True
            print(bot.remove_contact(args, book))

        elif command == "remove-phone":
            dirty = True
            print(bot.remove_phone(args, book))

        elif command == "add-birthday":
            print(bot.add_birthday(args, book))

        elif command == "change-birthday":
            dirty = True
            print(bot.change_birthday(args, book))

        elif command == "show-birthday":
            dirty = True
            print(bot.show_birthday(args, book))

            dirty = True
        elif command == "birthdays":
            bot.birthdays(args, book)

        elif command == "find-contact":
            print(bot.find_contact(args, book))

        elif command == "find-phone":
            print(bot.find_phone(args, book))

        elif command == "find-email":
            print(bot.find_email(args, book))
        
        elif command == "find-note":
            print(bot.find_note(args, notes))

        elif command == "all":
            print(bot.show_all(book))

        elif command == "add-note":
            dirty = True
            print(bot.add_note(args, notes))

        elif command == "edit-note":
            dirty = True
            print(bot.change_note(args, notes))

        elif command == "delete-note":
            dirty = True
            print(bot.delete_note(args, notes))

        elif command == "show-notes":
            dirty = True
            print(bot.show_all_notes(notes))

        elif command in ["help", "?"]:
            print(show_help())

        elif command == "add-email":
            dirty = True
            print(bot.add_email(args, book))

        elif command == "change-email":
            dirty = True
            print(bot.change_email(args, book))

        elif command == "show-email":
            print(bot.show_email(args, book))

        else:
            print(
                f"Invalid command. Use {highlight("help")} or {
                    highlight("?")} to see all available commands."
            )


if __name__ == "__main__":
    main()
