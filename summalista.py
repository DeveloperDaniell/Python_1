def summa(lista1, lista2):
    uusi_lista = []
    for i in range(len(lista1)):
        summa = lista1[i] + lista2[i]
        uusi_lista.append(summa)
    return uusi_lista


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b))  # [8, 10, 12]
