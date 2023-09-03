def pisimmat(lista: list):
    pisin_pituus = max(len(sana) for sana in lista)
    pisimmat_sanat = [sana for sana in lista if len(sana) == pisin_pituus]
    return pisimmat_sanat

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = pisimmat(lista)
    print(tulos)