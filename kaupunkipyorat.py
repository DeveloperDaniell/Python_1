# if True:
#     # Tätä lohkoa ei suoriteta
#     info = input("File: ")
# else:
#     # Kovakoodatut syötteet
#     info = "stations1.csv"


def hae_asematiedot(tiedosto: str):
    stations = {}
    with open(tiedosto) as file:
        for row in file:
            part = row.split(";")
            if part[0] == "Longitude":
                continue
            Longitude = part[0]
            Latitude = part[1]
            place = part[3]
            stations[place] = float(Longitude), float(Latitude)
        return stations
    
import math

def etaisyys(asemat: dict, asema1: str, asema2: str):
    longitude1, latitude1 = asemat[asema1]
    longitude2, latitude2 = asemat[asema2]

    x_kilometreina = (longitude1 - longitude2) * 55.26
    y_kilometreina = (latitude1 - latitude2) * 111.2
    etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)

    return etaisyys

def suurin_etaisyys(asemat: dict):
    largest_distance = 0
    largest_pair = ()
    for asema1 in asemat:
        for asema2 in asemat:
            if asema1 != asema2:
                current_distance = etaisyys(asemat, asema1, asema2)
                if current_distance > largest_distance:
                    largest_distance = current_distance
                    largest_pair = (asema1, asema2, largest_distance)
    return largest_pair




    
if __name__ == "__main__":
    asemat = hae_asematiedot('stations1.csv')
    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)