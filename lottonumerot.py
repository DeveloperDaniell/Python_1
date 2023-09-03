from random import randint

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    rivi = []
    while len(rivi) < maara:
        uusi = randint(alaraja, ylaraja)
        if uusi not in rivi:
            rivi.append(uusi)

    rivi.sort()
    return rivi
if __name__ == "__main__":
    print(lottonumerot(3,2,22))


