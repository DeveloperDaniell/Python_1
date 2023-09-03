from datetime import datetime, timedelta

# Kysytään käyttäjältä syötteet
tiedostonimi = input("Tiedosto: ")
aloituspäivä = input("Aloituspäivä (pp.kk.vvvv): ")
päivien_lkm = int(input("Montako päivää: "))

# Muutetaan aloituspäivä datetime-olioksi
aloituspäivä = datetime.strptime(aloituspäivä, "%d.%m.%Y")

# Luodaan listat päiville ja ruutuajoille
päivät = [aloituspäivä + timedelta(days=i) for i in range(päivien_lkm)]
ruutuajat = []

# Kysytään käyttäjältä ruutuajat
for päivä in päivät:
    ajat_str = input(f"Ruutuaika {päivä.strftime('%d.%m.%Y')}: ")
    ajat = list(map(int, ajat_str.split()))
    ruutuajat.append(ajat)

# Lasketaan yhteensä käytetyt minuutit ja keskimääräiset minuutit
yht_min = sum(sum(ajat) for ajat in ruutuajat)
keskim_min = yht_min / len(ruutuajat)

# Tallennetaan tiedot tiedostoon
with open(tiedostonimi, "w") as f:
    f.write(f"Ajanjakso: {päivät[0].strftime('%d.%m.%Y')}-{päivät[-1].strftime('%d.%m.%Y')}\n")
    f.write(f"Yht. minuutteja: {yht_min}\n")
    f.write(f"Keskim. minuutteja: {keskim_min}\n")
    for päivä, ajat in zip(päivät, ruutuajat):
        f.write(f"{päivä.strftime('%d.%m.%Y')}: {ajat[0]}/{ajat[1]}/{ajat[2]}\n")
