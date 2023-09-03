# tee ratkaisu tänne
def joulukuusi(koko):
    print("joulukuusi!")
    for i in range(1, koko + 1):
        print(" " * (koko - i) + "*" * (2 * i - 1))
    print(" " * (koko - 1) + "*")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(5)