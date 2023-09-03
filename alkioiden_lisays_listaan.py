# Kirjoita ratkaisu tähän
luvut = []
maara = int(input("Kuinka monta lukua: "))
i = 1
while i <= maara:
    luvut.append(int(input(f"Anna luku {i}: ")))
    i += 1

print(luvut)