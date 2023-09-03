def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if x not in range(3) or y not in range(3):
        return False
    if lauta[y][x] != "":
        return False
    lauta[y][x] = nappula
    return True

if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)
