from random import randint

def luo_salasana(length: int):
    salasana = ""
    for i in range(length):
        kirjain = chr(randint(97,122))
        salasana += kirjain

    return salasana

if __name__ == "__main__":
    for i in range(10):
        print(luo_salasana(8))
