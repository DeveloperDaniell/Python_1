def wordlist():
    words = []
    with open("wordlist.txt") as tiedosto:
        for rivi in tiedosto:
            words.append(rivi.strip())
    return words
 
words = wordlist()
lause = input("write text: ")
for sana in lause.split(' '):
    if sana.lower() in words:
        print(sana + " ", end="")
    else:
        print("*" + sana + "* ", end="")
print()