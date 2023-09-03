from random import choice

def sanat(n: int, alku: str):
    kaikki = []
    valitut = []
    with open("sanat.txt", "r") as file:
        for row in file:
            
            if row.startswith(alku):
                kaikki.append(row.strip())

    if  len(kaikki) < n:
        a = int("t")

    while len(valitut) < n:
        sana = choice(kaikki)
        if sana not in valitut:
            valitut.append(sana)
        
        

    return valitut

        




if __name__ == "__main__":
    lista = sanat(3, "ca")
    for sana in lista:
        print(sana)    