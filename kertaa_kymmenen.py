def kertaa_kymmenen(alku: int, loppu: int):
    uusi = {}
    i = alku
    while i <= loppu:
        uusi[i] = i * 10
        i += 1
    return uusi



if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)