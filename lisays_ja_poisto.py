# Kirjoita ratkaisu tähän
list = []
i = 1
while True:
    print("Lista on nyt", list)
    valinta = input("(l)isää, (p)oista vai e(x)it: ")
    if valinta == "l":
        list.append(i)
        i += 1
    elif valinta == "p":
        list.pop()
        i -= 1
    else:
        break
print("Moi!")