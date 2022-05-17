from car import Car
from repository import Repository
from customer import Customer
from contract import Contract
import datetime

# Instantiere objekter af vores klasse Car
car1 = Car('Volkswagen', 'Golf', 'Grøn', True, 28000, 24000, 18.1, ['Skifte gearkassen i 2018', 'Dækskifte til vintersæson'],1)
car2 = Car('Toyota', 'Prius', 'Blå', False, 50000, 40000, 15.8, [],2)
car3 = Car('Ford', 'Mustang', 'Rød', False, 44500, 30000, 16.5, ['Klargøring til sommersalg'],3)
car4 = Car('Tesla', '3', 'Rød', True, 70000, 40000, 16.5, ['Nyt batteri'],4)

# instantiate objekt af repository
Repo = Repository()
Repo.AddCar(car1)
Repo.AddCar(car2)
Repo.AddCar(car3)
Repo.AddCar(car4)

tempCustomer = Customer(1, 'Hans', 'Hansen', 'kornvænget', '123456')
Repo.AddCustomer(tempCustomer)
tempContract = Contract(111, tempCustomer,car1, datetime.datetime.now().month, 12) 
Repo.AddContract(tempContract)

print("*****Car List *******")
for car in Repo.GetCarList():
    print(car)
print("*****Customer List *******")
for customer in Repo.GetCustomerList():
    print(customer)    
print("*****Contract List *******")
for contract in Repo.GetContractList():
    print(contract)
