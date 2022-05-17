class Contract:
    def __init__(self, id, customer, car, date, duration):
        self.Id = id
        self.Customer=customer
        self.Car = car
        self.StartDate= date
        self.Duration = duration

    def __str__(self):
        return f'{self.Id} -  \n Customer info: {self.Customer} \n Car info: {self.Car} \n Start Date: {self.Duration} Delivery: {self.Duration+self.StartDate}'    