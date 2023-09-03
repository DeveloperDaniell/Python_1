def tee_tuple(x: int, y: int, z: int):
    tuple = (x, y, z)
    return min(tuple), max(tuple), sum(tuple)


if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))