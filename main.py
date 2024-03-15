from helpers.monty_utils import highlight, show_help
from helpers.monty_data_handler import load_from_json, save_to_json
import modules.monty_assistant as bot


def parse_input(user_input) -> str:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("\nWelcome to the assistant bot!")
    book = load_from_json("phonebook.json")
    note = load_from_json("notes.json")
    dirty = False
    
    while True:
        user_input = input("\nEnter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit", "bye"]:
            if dirty:
                save_to_json(book.to_json(), "phonebook.json")
                save_to_json(note.to_json(), "notes.json")
            print("Good bye!")
            break

        elif command in ["hello", "hi"]:
            print("How can I help you?")

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

        elif command == "show-birthday":
            dirty = True
            print(bot.show_birthday(args, book))

            dirty = True
        elif command == "birthdays":
            bot.birthdays(book)

        elif command == "phone":
            print(bot.show_phone(args, book))

        elif command == "all":
            print(bot.show_all(book))

        elif command == "add-note":
            dirty = True
            print(bot.add_note(args, notes))

        elif command == "find-note":
            dirty = True
            print(bot.find_note(args, notes))

        elif command == "edit-note":
            dirty = True
            print(bot.change_note(args, notes))

        elif command == "delete-note":
            dirty = True
            print(bot.delete_note(args, notes))

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
                f"Invalid command. Use {highlight("help")} or {highlight("?")} to see all available commands."
            )


if __name__ == "__main__":
    main()
