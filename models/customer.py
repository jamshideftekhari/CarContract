class Customer:
    def __init__(self, id, fn, ln, adress, phone):
        self.Id = id
        self.FirstName = fn
        self.LastName = ln
        self.Adress = adress
        self.Phone = phone

    def __str__(self):
        return f'{self.Id} - Customer First name: {self.FirstName}, last Name: {self.LastName}, Adress: {self.Adress}, Phone Number: {self.Phone}'    