from math import sqrt

def hypotenuusa(kateetti1: float, kateetti2: float):
    koko = kateetti1**2 + kateetti2**2
    return sqrt(koko)
    







if __name__ == "__main__":
    print(hypotenuusa(3,4)) # 5.0
    print(hypotenuusa(5,12)) # 13.0
    print(hypotenuusa(1,1)) # 1.4142135623730951