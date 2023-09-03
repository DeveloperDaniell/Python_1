import random

def luo_satunnaiset_parit():
    nimet = ["Daniel", "Pauli", "Teemu", "Riku", "Allu", "Otto", "Toni", "Kähkönen"]
    random.shuffle(nimet)
    parit = [(nimet[i], nimet[i+1]) for i in range(0, len(nimet), 2)]
    return parit

parit = luo_satunnaiset_parit()
for pari in parit:
    print(pari[0], "-", pari[1])