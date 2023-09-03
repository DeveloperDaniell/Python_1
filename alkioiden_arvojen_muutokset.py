# Kirjoita ratkaisu tähän
lista = [1, 2, 3, 4, 5]
indeksi = 0
while True:
    indeksi = int(input("Anna indeksi: "))
    if indeksi < 0:
        break
    arvo = int(input("Anna arvo: "))
    lista[indeksi] = arvo
    print(lista)
