from faker import Faker

fake = Faker()

class BusinessCard:
    def __init__(self,name,surname,company,position,email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email

data = BusinessCard(name=fake.name(),surname=fake.last_name(),company=fake.company(),position=fake.job(),email=fake.email())
print(str(data.name)+' | '+str(data.surname)+' | '+str(data.company)+' | '+str(data.position)+' | '+str(data.email))