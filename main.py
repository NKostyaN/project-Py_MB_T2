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
    words = WordCompleter(["hello", "hi", "close", "exit", "quit", "bye", "add", "change", "rename", "remove", "remove-phone", "add-birthday", "show-birthday", "change-birthday", "birthdays", "find-contact", "all", "help"])
    print("\nWelcome to the assistant bot!")
    book = load_from_json()     # to do -- >  book = load_from_json("phonebook.json")
                                # to do -- >  notes = load_from_json("notebook.json")
    dirty = False
    
    while True:
        user_input = prompt("\nEnter a command:> ", completer = words)
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit", "bye"]:
            if dirty:
                save_to_json(book.to_json())
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
            dirty = True
            print(bot.add_birthday(args, book))

        elif command == "change-birthday":
            dirty = True
            print(bot.change_birthday(args, book))

        elif command == "show-birthday":
            print(bot.show_birthday(args, book))

        elif command == "birthdays":
            bot.birthdays(args, book)

        elif command == "find-contact":
            print(bot.find_contact(args, book))

        elif command == "all":
            print(bot.show_all(book))

        elif command in ["help", "?"]:
            print(show_help())

        else:
            print(
                f"Invalid command. Use {highlight("help")} or {highlight("?")} to see all available commands."
            )


if __name__ == "__main__":
    main()
