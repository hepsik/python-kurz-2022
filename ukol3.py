import json


with open('body.json', encoding='utf-8') as muj_soubor:
    body = json.load(muj_soubor)

print(body)

for key, value in body.items():
    if value >= 60:
        vysledek = "pass"
    else:
        vysledek = "fail"


prospech = {}

for key in body:

    prospech[key] = vysledek

print(prospech)

with open('prospech.json', mode = 'w', encoding='utf-8') as souborr:
    json.dump(prospech,souborr)

    







