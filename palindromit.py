def palindromi(sana):
    sana2 = sana[::-1]
    if sana == sana2:
        return True
    else:
        return False

def paaohjelma():
    while True:
        syote = input("Anna palindromi: ")
        if palindromi(syote):
            print(f"{syote} on palindromi!")
            break
        else:
            print("ei ollut palindromi")

paaohjelma()
