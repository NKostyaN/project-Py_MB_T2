import re
try:
    from MontyBot.helpers.monty_utils import highlight
except ImportError:
    from helpers.monty_utils import highlight
   
class Address:
    def __init__(self, address:str):
        self.address = address
        

    def to_json(self) -> str:
        if self.address == None or self.address == "":
            return "None"
        return str(self.address)


    def __str__(self):
        parts = re.split(r',\s*|\s+', self.address)
        if len(parts) == 4:
            country, city, street, apartment = parts
            return f"Country: {highlight(country)}, City: {highlight(city)}, Street: {highlight(street)}, Apartment: {highlight(apartment)}"
        else:
            return f"{highlight(self.address)}"
            