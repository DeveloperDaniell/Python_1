def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    luvut = []
    for rivi in sudoku[rivi_nro:rivi_nro+3]:
        for luku in rivi[sarake_nro:sarake_nro+3]:
            if luku > 0 and luku in luvut:
                return False
            luvut.append(luku)
    return True

if __name__ == "__main__":
    sudoku = [
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

    print(nelio_oikein(sudoku, 0, 0))
    print(nelio_oikein(sudoku, 1, 2))
