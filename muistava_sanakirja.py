def lisaa_sana(sanakirja):
    suomeksi = input("Anna sana suomeksi: ")
    englanniksi = input("Anna sana englanniksi: ")
    sanakirja[suomeksi] = englanniksi
    print("Sanapari lisätty")

def hae_sana(sanakirja):
    sana = input("Anna sana: ")
    for suomeksi, englanniksi in sanakirja.items():
        if sana == suomeksi or sana == englanniksi:
            print(f"{suomeksi} - {englanniksi}")

def tallenna_sanakirja(sanakirja):
    with open("sanakirja.txt", 'w') as tiedosto:
        for suomeksi, englanniksi in sanakirja.items():
            tiedosto.write(f"{suomeksi}:{englanniksi}\n")

def lataa_sanakirja():
    sanakirja = {}
    try:
        with open("sanakirja.txt", 'r') as tiedosto:
            for rivi in tiedosto:
                suomeksi, englanniksi = rivi.strip().split(":")
                sanakirja[suomeksi] = englanniksi
    except FileNotFoundError:
        pass  # Tiedostoa ei ole, jatketaan tyhjällä sanakirjalla
    return sanakirja

def main():
    sanakirja = lataa_sanakirja()
    while True:
        print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
        valinta = input("Valinta: ")
        if valinta == '1':
            lisaa_sana(sanakirja)
            tallenna_sanakirja(sanakirja)
        elif valinta == '2':
            hae_sana(sanakirja)
        elif valinta == '3':
            print("Moi!")
            break
        else:
            print("Tuntematon valinta, yritä uudelleen.")

main()
