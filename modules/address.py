class Address:
    def __init__(self, country, city, street, appartment):
        self.country = country
        self.city = city
        self.street = street
        self.appartment = appartment

    def __str__(self):
        address_str = f"Country: {self.country}, City: {self.city}, Street: {self.street}, appartment: {self.appartment}"
        return address_str