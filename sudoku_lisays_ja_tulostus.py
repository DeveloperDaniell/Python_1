def tulosta(sudoku: list):
    r = 0
    for rivi in sudoku:
        s = 0
        for merkki in rivi:
            s += 1
            if merkki == 0:
                merkki = "_"
            m = f"{merkki} "
            if s%3 == 0 and s < 8:
                m += " "
            print(m, end="")
 
        print()
        r += 1
        if r%3 == 0 and r < 8:
            print()
 
def lisays(sudoku: list, rivi: int, sarake: int, luku: int):
    sudoku[rivi][sarake] = luku
# tee ratkaisu tänne
 


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    tulosta(sudoku)



    