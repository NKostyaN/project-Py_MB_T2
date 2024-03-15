import re
   
class Address:
    def __init__(self, address:str):
        self.address = address
        

    def to_json(self) -> str:
        if self.address == None or self.address == "":
            return "None"
        return self.address


    def __str__(self):
        # parts = self.address.split(", ")
        parts = re.split(r',\s*|\s+', self.address)
        if len(parts) == 4:
            country, city, street, apartment = parts
            return f"ADDRESS-> Country:{country}, City:{city}, Street:{street}, Apartment:{apartment}"
        else:
            return f"Address: {self.address}"
            