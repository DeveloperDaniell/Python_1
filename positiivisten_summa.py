def positiivisten_summa(lista):
    return sum([luku for luku in lista if luku > 0])


if __name__ == "__main__":
    lista = [1, -2, 3, -4, 5]
    vastaus = positiivisten_summa(lista)
    print("vastaus:", vastaus)
