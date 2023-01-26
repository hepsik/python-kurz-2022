

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadej kod soucastky")
pocet = int(input("Zadej počet kusů"))


if kod in sklad:
    if pocet > sklad[kod]:
        print(f"Lze prodat pouze {sklad[kod]} ks.")
        sklad.pop(kod)
    else:
        print(f"Dostatečná počet ks na skladě.")
        sklad[kod] = sklad[kod] - pocet
         
else:
    print(f"Neni skladem, smula")

print(sklad)
