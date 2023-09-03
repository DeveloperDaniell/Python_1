def samat(sana, a, b):
    if a < len(sana) and b < len(sana):
        if sana[a] == sana[b]:
            return True
        else:
            return False
    else:
        return False

# Testataan funktiota
if __name__ == "__main__":
    print(samat("koodari", 1, 10))
