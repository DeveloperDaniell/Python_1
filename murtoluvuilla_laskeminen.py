from fractions import Fraction

def jaa_palasiksi(maara: int):
    lista = []
    osa = Fraction(1, maara)
    for i in range(1, maara + 1):
        lista.append(osa)

    return lista


    

if __name__ == "__main__":
    for p in jaa_palasiksi(3):
        print(p)

    print()

    print(jaa_palasiksi(5))

# print (Fraction(11, 35))
# returns Fraction(11, 35)