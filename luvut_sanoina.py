def lukukirja():
    # Apusanakirja
    ykkoset = {0:"nolla", 1:"yksi", 2:"kaksi", 3:"kolme", 4:"neljä", 5:"viisi", 6:"kuusi", 7:"seitsemän", 8:"kahdeksan", 9:"yhdeksän"}
 
    luvut = {}
 
    # 0 - 9
    for i in range(10):
        luvut[i] = ykkoset[i]
 
    # 10 on erikoistapaus
    luvut[10] = "kymmenen"
 
    # 11 - 19
    for i in range(1, 10):
        luvut[i + 10] = ykkoset[i] + "toista"
 
    # 20 - 99
    for i in range(2, 10):
        luvut[i * 10] = ykkoset[i] + "kymmentä"
        for j in range(1, 10):
            luvut[i * 10 + j] = ykkoset[i] + "kymmentä" + ykkoset[j]
 
    return luvut

if __name__ == "__main__":
    luvut = lukukirja()
    print(luvut[2])      # "kaksi"
    print(luvut[11])     # "yksitoista"
    print(luvut[45])     # "neljäkymmentäviisi"
    print(luvut[99])     # "yhdensänkymmentäyhdeksän"
    print(luvut[0])      # "nolla"
