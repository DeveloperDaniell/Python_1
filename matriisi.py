def summa():
    with open("matriisi.txt") as tiedosto:
        summa = 0
        for rivi in tiedosto:
            for luku in rivi.split(","):
                summa += int(luku)

        return summa
    
def maksimi():
    with open("matriisi.txt") as tiedosto:
        suurin = 0
        for rivi in tiedosto:
            for luku in rivi.split(","):
                if int(luku) > suurin:
                    suurin = int(luku)

        return suurin
    
def rivisummat():
    with open("matriisi.txt") as tiedosto:
        summat = []
        for rivi in tiedosto:
            summat.append(sum(int(luku) for luku in rivi.split(",")))
        return summat


if __name__ == "__main__":
    print(summa())
    print(maksimi())
    print(rivisummat())