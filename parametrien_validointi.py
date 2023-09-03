def uusi_henkilo(nimi: str, ika: int):
    if nimi == "" or " " not in nimi or len(nimi) > 40 or ika < 0 or ika > 150:
        raise ValueError
    
    return nimi, ika
