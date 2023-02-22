teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

def prumer(a):
    avg = sum(a)/len(a)
    return avg

prumery = [prumer(dny) for dny in teploty]
print(prumery)

ranni_teploty = [dny[0] for dny in teploty]
nocni_teploty = [dny[3] for dny in teploty]

print(f"{ranni_teploty} \n{nocni_teploty}")

poledni =  [dny[1] for dny in teploty]
nocni = [dny[3] for dny in teploty]

vyber = [poledni, nocni]

po = [hodnota[0] for hodnota in vyber]
ut = [hodnota[1] for hodnota in vyber]
st = [hodnota[2] for hodnota in vyber]
ct = [hodnota[3] for hodnota in vyber]
pa = [hodnota[4] for hodnota in vyber]
so = [hodnota[5] for hodnota in vyber]
ne = [hodnota[6] for hodnota in vyber]

poledni_nocni = [po, ut, st, ct, pa, so, ne]
print(poledni_nocni)