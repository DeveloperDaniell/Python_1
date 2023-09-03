def lue_hedelmat():
    with open("hedelmat.csv") as tiedosto:
        uusi = {}
        for rivi in tiedosto:
            osat = rivi.split(";")
            tuote = osat[0]
            hinta = osat[1]
            uusi[tuote] = float(hinta)
        return uusi

if __name__ == "__main__":
    print(lue_hedelmat())