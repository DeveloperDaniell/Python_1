def lyhin(nimet: list):
    tulos = ""
 
    for nimi in nimet:
        if tulos == "" or len(nimi) < len(tulos):
            tulos = nimi
 
    return tulos

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]

    tulos = lyhin(lista)
    print(tulos)
