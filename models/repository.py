class Repository:
    def __init__(self):
        self.RepoCar = []
        self.Customer = []
        self.Contract = [] 

    def AddCar(self, car):
        self.RepoCar.append(car)

    def GetCar(self, index):
        return self.RepoCar[index]

    def GetCarList(self):
        return self.RepoCar        

    def AddCustomer(self, customer):
        self.Customer.append(customer)

    def GetCustomer(self, index):
        return self.Customer[index]

    def GetCustomerList(self):
        return self.Customer

    def AddContract(self, contract):
        self.Contract.append(contract)

    def GetContract(self, index):
        return self.Contract[index]

    def GetContractList(self):
        return self.Contract

