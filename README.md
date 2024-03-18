# MontyBot project
The project of a console bot assistant **MontyBot** for keeping a phone book and store some notes

### Instalation ###
To install bot just type in console:

``pip install -i https://test.pypi.org/simple/ MontyBot``


### Using ###
For start using bot, after instal, just type in console:
``MontyBot`` or ``montybot``

Bot can handle with next commands:

``add [username] [phone]`` - adding contact to the phonebook or adding new phone to existing contact

``add-email [username] [email]`` - adding e-mail of contact

``add-birthday [username] [birthday]`` - adding birthday of contact in DD.MM.YYYY format

``add-address [username]`` - adding address of contact

``add-note [title] [note]`` - adding [note] with [title]

``add-tags [title] [tags]`` - adding [tags] to note with [title]

``edit [username] [old phone] [new phone]`` - changing contact in the phonebook

``edit-email [username] [new email]`` - changing e-mail of contact

``edit-birthday [username] [birthday]`` - changing birthday of contact in DD.MM.YYYY format

``edit-note [title] [note]`` - changing [note] with [title]

``rename [username] [new phone]`` - rename contact in the phonebook

``show-email [username]`` - show email of contact

``show-birthday [username]`` - show birthday of the contact

``find-contact [username]`` - show all information of contact

``find-phone [phone]`` - show all contacts with [phone]

``find-email [email]`` - show all contacts with [email]

``find-address [address]`` - show all contacts with [address]

``find-note [title]`` - show note with [title]

``find-tags [tags]`` - show all notes with [tags]

``remove [username]`` - remove contact from phonebook

``remove-phone [username] [phone]`` - remove phone from contact

``remove-note [title]`` - remove note with [title]

``birthdays`` - show all contacts with birthdays on next week

``birthdays [days]`` - show all contacts with birthdays during next [days] days

``all`` - show all contacts in phonebook

``all-notes`` - show all notes

``close, exit, quit, bye`` - close application

``hello, hi`` - just a greeting

``help, ?`` - show help

### Uninstalation ###
To uninstall bot just type in console:

``pip uninstall MontyBot``