def rivi_oikein(sudoku: list, rivi_nro: int):
    rivi = sudoku[rivi_nro]
    for ruutu in rivi:
        if rivi.count(ruutu) > 1 and ruutu != 0:
            return False
    return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 2, 0, 0, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 4, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 6, 6],
        [3, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 2, 0, 2, 0, 1]
    ]

    print(rivi_oikein(sudoku, 0))
