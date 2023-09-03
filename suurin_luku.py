def suurin():
    with open("luvut.txt") as tiedosto:
        suurin = 0
        for rivi in tiedosto:
            luku = int(rivi)
            if luku > suurin:
                suurin = luku
        return suurin

if __name__ == "__main__":
    print(suurin())
