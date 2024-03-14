class Address:
    def __init__(self, address:str):
        self.address = address
        

    def __str__(self):
        parts = self.address.split(", ")
        if len(parts) == 4:
            country, city, street, apartment = parts
            return f"Country: {country}, City: {city}, Street: {street}, Apartment: {apartment}"
        else:
            return f"Address: {self.address}"