from datetime import datetime

def onko_validi(hetu: str) -> bool:
    if len(hetu) != 11:
        return False
    
    # Tarkistetaan syntymäpäivä
    paiva = int(hetu[:2])
    kuukausi = int(hetu[2:4])
    vuosi = int(hetu[4:6])
    vuosisata = hetu[6]

    # Määritetään vuosisata
    if vuosisata == '+':
        vuosi += 1800
    elif vuosisata == '-':
        vuosi += 1900
    elif vuosisata == 'A':
        vuosi += 2000
    else:
        return False

    # Tarkistetaan, että päivämäärä on validi
    try:
        datetime(vuosi, kuukausi, paiva)
    except ValueError:
        return False
    
    # Tarkistetaan tarkistusmerkki
    tarkiste_str = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    luku = int(hetu[:6] + hetu[7:10])
    tarkiste_calculated = tarkiste_str[luku % 31]

    return tarkiste_calculated == hetu[-1]

if __name__ == "__main__":
    print(onko_validi("230827-906F"))  # True
    print(onko_validi("120488+246L"))  # True
    print(onko_validi("310823A9877"))  # False, tarkistusmerkki on virheellinen
