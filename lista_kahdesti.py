lista = []
while True:
    luku = int(input("Anna luku: "))
    lista.append(luku)
    if luku == 0:
        break
    print("Lista:", lista)
    print("Järjestettynä:", sorted(lista))
print("Moi!")