from datetime import datetime

paiva = int(input("Päivä: "))
kuukausi = int(input("Kuukausi: "))
vuosi = int(input("Vuosi: "))

syntyma = datetime(vuosi, kuukausi, paiva)
hetki = datetime( 1999, 12, 31)
ika = hetki - syntyma

if ika.days > 0:
    print(f"Olit {ika.days} päivää vanha, kun vuosituhat vaihtui.")
else:
    print("Et ollut syntynyt, kun vuosituhat vaihtui.")
