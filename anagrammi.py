# Tee ratkaisu tänne
def anagrammi(sana1, sana2):
    return sorted(sana1) == sorted(sana2)

if __name__ == "__main__":
    print(anagrammi("a", "a"))