# tee ratkaisu tänne
def eniten_kirjainta(mjono):
    kirjaimet = {}
    for kirjain in mjono:
        if kirjain in kirjaimet:
            kirjaimet[kirjain] += 1
        else:
            kirjaimet[kirjain] = 1
    eniten_esiintyva_kirjain = None
    eniten_esiintymia = 0
    for kirjain, esiintymat in kirjaimet.items():
        if esiintymat > eniten_esiintymia:
            eniten_esiintymia = esiintymat
            eniten_esiintyva_kirjain = kirjain
    return eniten_esiintyva_kirjain

if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))
