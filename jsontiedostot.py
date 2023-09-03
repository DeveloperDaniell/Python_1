import json

def tulosta_henkilot(tiedosto: str):
    with open(tiedosto, "r") as file:
        data = json.load(file)
        for henkilo in data:
            nimi = henkilo['nimi']
            ika = henkilo['ika']
            harrastukset = ', '.join(henkilo['harrastukset'])
            print(f"{nimi} {ika} vuotta ({harrastukset})")

if __name__ == "__main__":
    tulosta_henkilot("tiedosto1.json")
