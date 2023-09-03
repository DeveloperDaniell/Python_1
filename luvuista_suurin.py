# tee ratkaisu tänne
def luvuista_suurin(a, b, c):
    if a > b and a > c:
        return a
    elif b >= a and b > c:
        return b
    else:
        return c
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    suurin = luvuista_suurin(1, 1, -100)
    print(suurin)