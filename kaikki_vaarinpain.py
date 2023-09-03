def kaikki_vaarinpain(lista):
    uusi_lista = []
    i = len(lista) - 1
    while i >= 0:
        uusi_lista.append(lista[i][::-1])
        i -= 1
    return uusi_lista

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    tulos = kaikki_vaarinpain(lista)
    print(tulos)
