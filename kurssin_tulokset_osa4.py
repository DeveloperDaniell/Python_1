if True:
    opiskelijatiedot = input("opiskelijatiedot: ")
    tehtavatiedot = input("tehtävätiedot: ")
    koetiedot = input("koetiedot: ")
    kurssitiedot = input("kurssin tiedot: ")
else:
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
    koetiedot = "koepisteet1.csv"
    kurssitiedot = "kurssi1.txt"

nimet = {}    

with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(";")
        if osat[0] == "opnro":
            continue
        nimet[osat[0]] = ' '.join(osat[1:])

koepisteet = {}

with open(koetiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(";")
        if osat[0] == "opnro":
            continue
        koepisteet[osat[0]] = sum([int(piste) for piste in osat[1:]])

tehtavat = {}

with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(";")
        if osat[0] == "opnro":
            continue
        tehtavat[osat[0]] = [int(piste) for piste in osat[1:]]

kurssin_nimi = ""
kurssin_op = ""
with open(kurssitiedot) as tiedosto:
    for rivi in tiedosto:
        if "nimi" in rivi:
            kurssin_nimi = rivi.split(": ")[1].strip()
        elif "laajuus opintopisteina" in rivi:
            kurssin_op = rivi.split(": ")[1].strip()

kurssi = f"{kurssin_nimi}, {kurssin_op} opintopistettä"

def laske_arvosana(pisteet):
    if pisteet <= 14:
        return 0
    elif pisteet <= 17:
        return 1
    elif pisteet <= 20:
        return 2
    elif pisteet <= 23:
        return 3
    elif pisteet <= 27:
        return 4
    else:
        return 5

print(kurssi)
print("========================================")
print(f'{"nimi":30}{"teht_lkm":<10}{"teht_pist":<10}{"koe_pist":<10}{"yht_pist":<10}{"arvosana":<10}')
for opnro, nimi in nimet.items():
    teht_lkm = len(tehtavat[opnro])
    teht_pist = (sum(tehtavat[opnro]) / 40) * 10  # 40 pistettä tehtävistä tuo 10 pistettä
    teht_pist = int(teht_pist)  # pyöristetään alaspäin kokonaislukuarvoon
    koe_pist = koepisteet[opnro]
    yht_pist = teht_pist + koe_pist
    arvosana = laske_arvosana(yht_pist)
    print(f'{nimi:30}{teht_lkm:<10}{teht_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana:<10}')
