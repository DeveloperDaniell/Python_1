def suorita(ohjelma):
    muuttujat = {chr(i + 65): 0 for i in range(26)}  # alustetaan muuttujat A-Z
    kohta = {ohjelma[i].split(':')[0]: i for i in range(len(ohjelma)) if ohjelma[i].endswith(':')}  # tallennetaan hyppykohtien rivinumerot
    tulokset = []

    i = 0
    while i < len(ohjelma):
        rivi = ohjelma[i].split()
        if rivi[0] == 'PRINT':
            tulokset.append(int(muuttujat[rivi[1]] if rivi[1] in muuttujat else rivi[1]))
        elif rivi[0] == 'MOV':
            muuttujat[rivi[1]] = int(muuttujat[rivi[2]] if rivi[2] in muuttujat else rivi[2])
        elif rivi[0] == 'ADD':
            muuttujat[rivi[1]] += int(muuttujat[rivi[2]] if rivi[2] in muuttujat else rivi[2])
        elif rivi[0] == 'SUB':
            muuttujat[rivi[1]] -= int(muuttujat[rivi[2]] if rivi[2] in muuttujat else rivi[2])
        elif rivi[0] == 'MUL':
            muuttujat[rivi[1]] *= int(muuttujat[rivi[2]] if rivi[2] in muuttujat else rivi[2])
        elif rivi[0] == 'JUMP':
            i = kohta[rivi[1]]
            continue
        elif rivi[0] == 'IF':
            ehto = ''.join(rivi[1:4])
            if eval(ehto.replace('==', '==').replace('!=', '!=').replace('<', '<').replace('<=', '<=').replace('>', '>').replace('>=', '>=')):
                i = kohta[rivi[5]]
                continue
        elif rivi[0] == 'END':
            break
        i += 1

    return tulokset
