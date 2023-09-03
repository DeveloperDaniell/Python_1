def lue(luku: int, luku1: int, luku2: int):
    while True:
        try:
            syote = input("syötä luku: ")
            luku = int(syote)
            if luku >= luku1 and luku <= luku2:
                return luku
        except ValueError:
                pass
        
        print(f"Syötteen on oltava kokonaisluku väliltä {luku1}...{luku2}")
    
    #print(f"syötit luvun: {luku}")
            




if __name__ == "__main__":
    luku = lue("syötä luku: ", 5, 10)
    print("syötit luvun:", luku) 

