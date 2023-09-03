if True:
    # Tätä lohkoa ei suoriteta
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # Kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"

nimet = {}

# Lue opiskelijatiedot
with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(";")
        if osat[0] == "opnro":
            continue
        # Liitä nimiosat yhteen yhdeksi merkkijonoksi
        nimet[osat[0]] = ' '.join(osat[1:])

arvosanat = {}

# Lue tehtävätiedot
with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.strip().split(";")
        if osat[0] == "opnro":
            continue
        # Muuta pisteet kokonaisluvuiksi
        arvosanat[osat[0]] = [int(piste) for piste in osat[1:]]

# Tulosta opiskelijoiden nimet ja tehtäväpisteiden summat
for opnro, nimi in nimet.items():
    if opnro in arvosanat:
        numerot = sum(arvosanat[opnro])
        print(f"{nimi} {numerot}")
