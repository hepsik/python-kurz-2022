class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    def __str__(self) -> str:
        return f"Auto {self.typ_vozidla}, registracni znacka {self.registracni_znacka}, najeto {self.najete_km}"
    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            return "Potvrzuji zapůjčení"
        else: 
            return "Vozidlo není k dispozici"
    def info(self):
        return f"{self.typ_vozidla}, {self.registracni_znacka}, {self.najete_km}"
    
pezot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
oktavka = Auto("1P3 4747", "Skoda Octavia", 41253)
print(pezot)

print(pezot.info())

auto_uzivatel = input("Jake auto si chcete pujcit?")

if auto_uzivatel == "Peugeot":
    print(pezot.info())
    print(pezot.pujc_auto())
elif auto_uzivatel == "Skoda":
    print(oktavka.info())
    print(oktavka.pujc_auto())
else: 
    print("Takove auto nemame")



