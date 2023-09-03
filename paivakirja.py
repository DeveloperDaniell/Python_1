doc = "paivakirja.txt"

while True:
    print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
    choice = int(input("Valinta: "))
    if choice == 1:
        text = input("Anna merkintä: ")
        with open(doc, "a") as file:
            file.write(text + "\n")
            print("Päiväkirja tallennettu")

    elif choice == 2:
        print("Merkinnät: ")
        with open(doc) as file:
            print(file.read())

    elif choice == 0:
        break

print("Heippa! ")