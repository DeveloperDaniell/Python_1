# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(koko, merkki):
    if merkki == "":
        print("*" * koko)
    else:
        print(koko * merkki[0])

def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    korkeus = 1
    while korkeus <= koko:
        viiva(koko, merkki)
        korkeus += 1
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "x")
