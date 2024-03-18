from datetime import datetime, timedelta
import re


def cyan(txt: str) -> str:
    """Return text in cyan color"""
    return f"\033[96m{txt}\x1b[0m"          # cyan

def yellow(txt: str) -> str:
    """Return text if yellow color"""
    return f"\033[93m{txt}\x1b[0m"          # yellow

def warning(txt: str) -> str:
    """Return text in red color"""
    return f"\033[91m{txt}\x1b[0m"          # red

def info(txt: str) -> str:
    """Return text in grey color"""
    return f"\33[90m{txt}\x1b[0m"           # grey

def error(txt: str) -> str:
    """Return text with background in red color"""
    return f"\033[41m{txt}\x1b[0m"          # red background

def check_phone(phone: str) -> str:
    """Return corrected phone number"""
    extract = re.findall(r'\d+', phone)
    phone = ""
    for line in extract:
        phone += line
    return phone

def check_date(date_str: str) -> str:
    """Check is date was entered in correct format"""
    date_format = "%d.%m.%Y"
    date = ""
    try:
        date = datetime.strftime(datetime.strptime(date_str, date_format), date_format)
        return date
    except Exception as e:
        print(f"{warning(f"Error in {check_date.__name__}:")} {e}")
        print(f"Use {cyan("DD.MM.YYYY")} format please\n")

def validate_email(email_str: str) -> str:             # re-pattern for email validation 
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email_str):
        return email_str

def check_email(email_str: str) -> str:                # email-format validation 
    try:
        validated_email = validate_email(email_str)
        return validated_email 
    except Exception as e:
        return None  

def get_birthdays_per_week(users: list, during_days=7) -> str:
    """Check is there is someone to congratulate in next week or in next [during_days] days"""
    today = datetime.today().date()
    weekdays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }
    try:
        for usr in users:
            for key in usr.keys():
                name = key
                bday = datetime.strptime(usr[key], "%d.%m.%Y").date() 
            bday_this_year = bday.replace(year=today.year)

            if bday_this_year < today:                                  
                if bday_this_year.weekday() < 5 or (
                    today.weekday() != 0 and today.weekday() != 6
                ):
                    bday_this_year = bday_this_year.replace(
                        year=bday_this_year.year + 1
                    )

            weekday = bday_this_year.weekday()
            if weekday >= 5:
                bday_this_year += timedelta(days=7 - weekday)

            delta = (bday_this_year - today).days
            if delta < during_days:
                weekdays[bday_this_year.strftime("%A")].append(name)

        bdays = {}
        for k, v in weekdays.items():
            if v != []:
                bdays.update({k: v})
        if bdays != {}:
            for k, v in bdays.items():
                print(f"{cyan(str(k))}: {", ".join(v)}")
        else:
            print("There is no one to congratulate during the week" if during_days == 7 else f"There is no one to congratulate during {during_days} days")

    except TypeError:
        print(error("Something wrong in input data, pls check it"))


def show_help() -> str:
    """Shows list of all available commands"""
    help = (
        f"\n {"-"*10} Available commands {"-"*10}\n"
        f"  {yellow("add")} {cyan("[username] [phone]")} - adding contact to the phonebook or adding new phone to existing contact\n"
        f"  {yellow("add-email")} {cyan("[username] [email]")} - adding e-mail of contact\n"
        f"  {yellow("add-birthday")} {cyan("[username] [birthday]")} - adding birthday of contact in {cyan("DD.MM.YYYY")} format\n"
        f"  {yellow("add-address")} {cyan("[username]")} - adding address of contact\n"
        f"  {yellow("add-note")} {cyan("[title] [note]")} - adding [note] with [title]\n"
        f"  {yellow("add-tags")} {cyan("[title] [tags]")} - adding [tags] to note with [title]\n"
        f"  {yellow("edit")} {cyan("[username] [old phone] [new phone]")} - changing contact in the phonebook\n"
        f"  {yellow("edit-email")} {cyan("[username] [new email]")} - changing e-mail of contact\n"
        f"  {yellow("edit-birthday")} {cyan("[username] [birthday]")} - changing birthday of contact in {cyan("DD.MM.YYYY")} format\n"
        f"  {yellow("edit-note")} {cyan("[title] [note]")} - changing [note] with [title]\n"
        f"  {yellow("rename")} {cyan("[username] [new phone]")} - rename contact in the phonebook\n"
        f"  {yellow("show-email")} {cyan("[username]")} - show email of contact\n"
        f"  {yellow("show-birthday")} {cyan("[username]")} - show birthday of the contact\n"
        f"  {yellow("find-contact")} {cyan("[username]")} - show all information of contact\n"
        f"  {yellow("find-phone")} {cyan("[phone]")} - show all contacts with [phone]\n"
        f"  {yellow("find-email")} {cyan("[email]")} - show all contacts with [email]\n"
        f"  {yellow("find-address")} {cyan("[address]")} - show all contacts with [address]\n"
        f"  {yellow("find-note")} {cyan("[title]")} - show note with [title]\n"
        f"  {yellow("find-tags")} {cyan("[tags]")} - show all notes with [tags]\n"
        f"  {yellow("remove")} {cyan("[username]")} - remove contact from phonebook\n"
        f"  {yellow("remove-phone")} {cyan("[username] [phone]")} - remove phone from contact\n"
        f"  {yellow("remove-note")} {cyan("[title]")} - remove note with [title]\n"
        f"  {yellow("birthdays")} - show all contacts with birthdays on next week\n"
        f"  {yellow("birthdays")} {cyan("[days]")} - show all contacts with birthdays during next [days] days\n"
        f"  {yellow("all")} - show all contacts in phonebook\n"
        f"  {yellow("all-notes")} - show all notes\n"
        f"  {yellow("close")}, {yellow("exit")}, {yellow("quit")}, {yellow("bye")} - close application\n"
        f"  {yellow("hello")}, {yellow("hi")} - just a greeting\n"
        f"  {yellow("help")}, {yellow("?")} - this help\n"
        f"{"-"*40}"
    )
    return help


if __name__ == "__main__":
    pass
