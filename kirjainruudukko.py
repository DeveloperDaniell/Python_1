luku = int(input("Kerrokset: "))
inc_i = 1
i = 0
while i >= 0:
    row = ""
    inc_j = 1
    j = 0
    while j >= 0:
        delta = i if i < j else j
        row += chr(ord("A") - 1 + luku - delta) + ""
        if j == luku - 1:
            inc_j = -1
        j += inc_j
    print(row)
    if i == luku - 1:
        inc_i = -1
    i += inc_i