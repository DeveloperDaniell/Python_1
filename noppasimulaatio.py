from random import *

def heita(noppa: str):
    if noppa == "A":
        silma = int(choice("333336"))

    elif noppa == "B":
        silma = int(choice("222555"))

    elif noppa == "C":
        silma = int(choice("144444"))

    return silma

def pelaa(noppa1: str, noppa2: str, kertaa: int):
    eka = 0
    toka = 0
    tasa = 0
    for i in range(kertaa):
        heitto1 = heita(noppa1)
        heitto2 = heita(noppa2)
        if heitto1 > heitto2:
            eka += 1
        elif heitto1 < heitto2:
            toka += 1
        else:
            tasa += 1
    return eka, toka, tasa



if __name__ == "__main__":
    print(heita("A"))
    tulos = pelaa("A", "C", 1000)
    print(tulos)
    tulos = pelaa("B", "B", 1000)
    print(tulos)