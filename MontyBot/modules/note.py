try:
    from MontyBot.helpers.monty_utils import yellow, info
except ImportError:
    from helpers.monty_utils import yellow, info


class Note:
    def __init__(self, title="None", text="None", tags=""):
        self.title = title
        self.text = text
        self.tags = tags

    def __str__(self):
        res = ""
        res += f"\n{info("-")} {yellow(self.title)} {info("-")}\n{self.text}\n"
        res += f"{info("[tags:] "+self.tags)}\n" if self.tags != "" else ""
        return res
