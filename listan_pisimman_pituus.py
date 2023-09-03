def pisimman_pituus(lista):
    uusi = [len(i) for i in lista]
    return max(uusi)

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = pisimman_pituus(lista)
    print(tulos)
