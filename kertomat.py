def kertomat(n: int):
    tulos = {}
    tulos[1] = 1
    for i in range(2, n + 1):
        tulos[i] = tulos[i-1] * i
    return tulos


if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])  # tulostaa 1
    print(k[3])  # tulostaa 6
    print(k[5])  # tulostaa 120
