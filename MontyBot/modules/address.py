import re
try:
    from MontyBot.helpers.monty_utils import cyan
except ImportError:
    from helpers.monty_utils import cyan
   
class Address:
    def __init__(self, address:str):
        self.address = address
        

    def to_json(self) -> str:
        if self.address == None or self.address == "":
            return "None"
        return str(self.address)


    def __str__(self):
        parts = re.split(r',\s*|\s+', self.address) # split parameters by comma or gap
        """we need to divide address by four parts"""
        if len(parts) == 4:
            country, city, street, apartment = parts
            return f"Country: {cyan(country)}, City: {cyan(city)}, Street: {cyan(street)}, Apartment: {cyan(apartment)}"
        else:
            return f"{cyan(self.address)}"
            