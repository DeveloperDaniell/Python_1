def laskuri():
    sanat = set()
    while True:
        sana = input("sana: ")
        if sana in sanat:
            break
        sanat.add(sana)
    print("Annoit", len(sanat), "eri sanaa")

laskuri()
