def uniikit(lista):
    uniikit_luvut = sorted(set(lista))
    return uniikit_luvut

if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista))  # [1, 2, 3]
