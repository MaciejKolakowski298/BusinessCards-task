from faker import Faker

class BaseContact:
    def __init__(self, name, phone, e_mail):
        self.name = name
        self.phone = phone
        self.e_mail = e_mail

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name}")
   

    def __str__(self):
        return f"{self.name}, {self.phone} , {self.e_mail}"

    @property
    def label_length(self):
        return len(self.name)


class BusinessContact(BaseContact):
    def __init__(self, name, phone, e_mail, position, company, business_phone):
        super().__init__(name, phone, e_mail)
        self.position=position
        self.company=company
        self.business_phone=business_phone
    
    def contact(self):
        print(f"Wybieram numer służbowy {self.business_phone} i dzwonię do {self.name}")

def create_contacts(rodzaj, ilość):
    wizytowki=[]
    fake=Faker('pl_PL')

    if rodzaj=='BaseContact':
        for i in range (ilość):
            wizytowka=BaseContact(fake.name(),fake.phone_number(), fake.email())
            wizytowki.append(wizytowka)
    elif rodzaj=='BusinessContact':
        for i in range (ilość):
            bwizytowka=BusinessContact(fake.name(), fake.phone_number(), fake.email(), fake.job(), fake.company(), fake.phone_number())
            wizytowki.append(bwizytowka)
    return wizytowki

wizytowki=create_contacts('BaseContact', 3)
wizytowki+=create_contacts('BusinessContact', 3)

for i in wizytowki:
    i.contact()
    print('ilość znaków', i.label_length)