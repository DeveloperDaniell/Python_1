# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(koko, merkki):
    if merkki == "":
        print("*" * koko)
    else:
        print(koko * merkki[0])

def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 1
    while i <= koko:
        viiva( i , "#")
        i += 1


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
