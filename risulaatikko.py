# kopioi edellisestä tehtävästä funktion viiva koodi tänne
# tee ratkaisu tänne
def viiva(koko, merkki):
    if merkki == "":
        print("*" * koko)
    else:
        print(koko * merkki[0])
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    koko = 0
    while koko < korkeus:
        koko += 1
        viiva(10, "#")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
