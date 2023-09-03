ryhmat = {}

while True:    
    valinta = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
    
    if valinta == 2:
        nimi = input("nimi: ")
        numero = input("numero: ")
        if nimi not in ryhmat:
            ryhmat[nimi] = []
        ryhmat[nimi].append(numero)
        print("ok!")
        
    elif valinta == 1:
        haku = input("nimi: ")
        if haku in ryhmat:
            for numero in ryhmat[haku]:
                print(numero)
        else:
            print("ei numeroa")

    elif valinta == 3:
        print("lopetetaan...")
        break
