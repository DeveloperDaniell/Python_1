# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(koko, merkki):
    if merkki == "":
        print("*" * koko)
    else:
        print(koko * merkki[0])


def kolmio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 1
    while i <= koko:
        viiva( i , merkki)
        i += 1

def kuvio(koko1, merkki1, koko2, merkki2):
    i = 1
    kolmio(koko1, merkki1)
    while i <= koko2:
        viiva(koko1, merkki2)
        i += 1



# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    #kuvio(5, "x", 2, "o")
    kuvio(5, "X", 3, "*")
