import string

def jaa_merkkeihin(merkkijono: str):
    osat = ([], [], [])
    for merkki in merkkijono:
        if merkki in string.ascii_letters:
            osat[0].append(merkki)
        elif merkki in string.punctuation:
            osat[1].append(merkki)
        else:
            osat[2].append(merkki)

    # Muuntaa listat merkkijonoiksi ja palauttaa ne tupleena
    return ("".join(osat[0]), "".join(osat[1]), "".join(osat[2]))

if __name__ == "__main__":
    osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
    print(osat[0])  # Tulostaa kirjaimet yhtenäisenä merkkijonona
    print(osat[1])  # Tulostaa erikoismerkit yhtenäisenä merkkijonona
    print(osat[2])  # Tulostaa muut merkit yhtenäisenä merkkijonona
 