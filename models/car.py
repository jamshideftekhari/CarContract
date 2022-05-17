class Car:
    def __init__(self, brand, model, color, onSale, marketPrice, sellingPrice, kmPerLiter, reperationer, id):
        self.Brand = brand
        self.Model = model
        self.Color = color
        self.OnSale = onSale
        self.MarketPrice = marketPrice
        self.SellingPrice = sellingPrice
        self.KmPerLiter = kmPerLiter
        self.Reperationer = reperationer
        self.CarId = id

    def __str__(self):
        return f'Car ID: {self.CarId}, Brand:  {self.Brand}, Model: {self.Model}, Color: {self.Color}, On Sale: {self.OnSale}, Marker Price: {self.MarketPrice}, Selling Price: {self.SellingPrice}, KM per Liter: {self.KmPerLiter}, Reprationer: {self.Reperationer}'    