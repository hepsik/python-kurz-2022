import math 
#fce overeni cila
def overeni(cislo):
    if len(cislo) == 9:
        return True
    elif len(cislo) == 13 and cislo[0:4]== "+420":
        cislo.replace(" ","")
        return True
    elif len(cislo) == 16 and cislo[4]== " " and cislo[8]== " " and cislo[12]== " ":
        return True
    else:
        return False
#fce cena zpravy  
def cena_zpravy(text):
    cena = 3
    pocet_znaku = int(len(text))
    pocet_ks = pocet_znaku / 180
    zaokrouhlene = math.ceil(pocet_ks)
    cena_sms = zaokrouhlene * cena
    return cena_sms

cislo_uzivatel = input("Zadej telefonní číslo příjemce.")
print(overeni(cislo_uzivatel))

if overeni(cislo_uzivatel) == False:
    print(f"Zadané číslo je ve špatném formátu")
else:
    zprava = input("Zadej text zprávy.")
    vysledna_cena = cena_zpravy(zprava)
    print(f"Cena zprávy bude {vysledna_cena} Kč.")










