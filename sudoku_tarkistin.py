def sudoku_oikein(sudoku: list):
    for rivi_nro in range(9):
        if not rivi_oikein(sudoku, rivi_nro):
            return False
    for sarake in range(9):
        if not sarake_oikein(sudoku, sarake):
            return False
    for rivi_nro in [0, 3, 6]:
        for sarake_nro in [0, 3, 6]:
            if not nelio_oikein(sudoku, rivi_nro, sarake_nro):
                return False
    return True

def rivi_oikein(sudoku: list, rivi_nro: int):
    rivi = sudoku[rivi_nro]
    luvut = []
    for ruutu in rivi:
        if ruutu in luvut and ruutu != 0:
            return False
        luvut.append(ruutu)
    return True

def sarake_oikein(sudoku: list, sarake: int):
    luvut = []
    for rivi in sudoku:
        luku = rivi[sarake]
        if luku in luvut and luku != 0:
            return False
        luvut.append(luku)
    return True

def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    luvut = []
    for rivi in sudoku[rivi_nro:rivi_nro+3]:
        for luku in rivi[sarake_nro:sarake_nro+3]:
            if luku in luvut and luku != 0:
                return False
            luvut.append(luku)
    return True

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
