from random import choice, shuffle
from string import ascii_lowercase, digits

def luo_hyva_salasana(pituus: int, numerot: bool, merkit: bool):
    sallitut_merkit = ascii_lowercase
    salasana = [choice(ascii_lowercase)]  # Varmistetaan, että salasanassa on ainakin yksi kirjain

    if numerot:
        sallitut_merkit += digits
        salasana.append(choice(digits))

    if merkit:
        sallitut_merkit += "!?=+-()#"
        salasana.append(choice("!?=+-()#"))

    while len(salasana) < pituus:
        salasana.append(choice(sallitut_merkit))

    shuffle(salasana)
    return ''.join(salasana)

if __name__ == "__main__":
    for _ in range(10):
        print(luo_hyva_salasana(12, True, True))
