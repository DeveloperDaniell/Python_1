import string

def vaihda_koko(merkkijono: str):
    new = ""
    for i in merkkijono:
        if i.islower():
            new += i.upper()
        else:
            new += i.lower()
    return new

def puolita(merkkijono: str):
    jako = len(merkkijono) // 2

    return merkkijono[:jako], merkkijono[jako:]


def poista_erikoismerkit(merkkijono: str):
    new = ""
    for i in merkkijono:
        if i in string.ascii_letters or i in "äöå 1234567890":
            new += i
        
    return new

if __name__ == "__main__":
    import merkkiapuri

    mjono = "Moi kaikki!"

    print(merkkiapuri.vaihda_koko(mjono))

    p1, p2 = merkkiapuri.puolita(mjono)

    print(p1)
    print(p2)

    m2 = merkkiapuri.poista_erikoismerkit("Tämä on testi, katsotaan miten käy!!!11!")
    print(m2)