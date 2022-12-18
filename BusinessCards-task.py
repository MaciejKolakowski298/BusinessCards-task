class BusinessCards:
    def __init__(self, name, last_name, company, job_position, e_mail):
        self.name = name
        self.last_name = last_name
        self.company = company
        self.job_position = job_position
        self.e_mail = e_mail
    def __str__(self):
        return f"{self.name} {self.last_name} , {self.e_mail}"
Card_1 = BusinessCards(name="Dorota", last_name="Wysocki", company="Poore Simmon's", job_position="Cytotechnologist", e_mail="DorotaWysocki@rhyta.com")
Card_2 = BusinessCards(name="Józef", last_name="Rutkowski", company="Aronson Furniture", job_position="Greenskeeper", e_mail="JozefRutkowski@rhyta.com")
Card_3 = BusinessCards(name="Klementyna", last_name="Zając", company="Fellowship Investments", job_position="Braille clerk", e_mail="KlementynaZajac@dayrep.com")
Card_4 = BusinessCards(name="Lew", last_name="Czarnecki", company="Hastings", job_position="Correctional treatment specialist", e_mail="LewCzarnecki@teleworm.us")
Card_5 = BusinessCards(name="Racław", last_name="Zawacki", company="Well's And Wade", job_position="Physical therapist assistant", e_mail="RaclawZawacki@jourrapide.com")

BusinessCards_list=[Card_1 , Card_2 , Card_3 , Card_4 , Card_5]

for i in BusinessCards_list:
    print(i)

by_name = sorted(BusinessCards_list, key=lambda card: card.name)
for i in by_name:
    print(i)  

by_last_name = sorted(BusinessCards_list, key=lambda card: card.last_name)
for i in by_last_name:
    print(i) 

by_e_mail = sorted(BusinessCards_list, key=lambda card: card.e_mail)  
for i in by_e_mail:
    print(i)
   

#for i in BusinessCards_list:
    #print(i.name , i.last_name , i.e_mail)

#print(f"{Card_1.name} {Card_1.last_name} , {Card_1.e_mail}")