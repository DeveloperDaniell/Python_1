luvut = []

while True:
    luku = int(input("Syötä seuraava luku: "))
    if luku > 0:
        luvut.append(luku)
    else:
        break

if len(luvut) < 2:
    print("Luvut ovat peräkkäisiä.")
else:
    luvut.sort()
    for i in range(len(luvut) - 1):
        if luvut[i] == luvut[i + 1]:
            print("Luvut eivät ole peräkkäisiä.")
            break
    else:
        print("Luvut ovat peräkkäisiä.")
