def pisin(merkkijonot: list):
    suurin = ""
    for i in merkkijonot:
        if len(i) > len(suurin):
            suurin = i
    return suurin    

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))