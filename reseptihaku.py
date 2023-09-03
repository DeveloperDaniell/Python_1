def lajittelu_aineet(tiedosto: str):
    reseptit = {}
    with open(tiedosto) as lista:
        nimi = ""
        raaka_aineet = []
        aika = 0
        for rivi in lista:
            rivi = rivi.strip()
            if not rivi:  # New recipe starts
                if nimi:  # Save the previous recipe if it exists
                    reseptit[nimi.lower()] = {'alkuperaiset': raaka_aineet, 'nimi': nimi, 'aika': aika}
                nimi = ""  # Reset recipe name and ingredients
                raaka_aineet = []
                aika = 0
            elif not nimi:  # Assuming the recipe name is the first non-empty line
                nimi = rivi
            elif not aika:  # Assuming the recipe time is the second non-empty line
                aika = int(rivi)
            else:  # it's an ingredient
                raaka_aineet.append(rivi)

        if nimi:  # Save the last recipe if it exists
            reseptit[nimi.lower()] = {'alkuperaiset': raaka_aineet, 'nimi': nimi, 'aika': aika}
    return reseptit

def hae_nimi(tiedosto: str, sana: str):
    reseptit = lajittelu_aineet(tiedosto)
    words = []
    for avain in reseptit:
        if sana.lower() in avain:
            words.append(reseptit[avain]['nimi'])
    return words

def hae_aika(tiedosto: str, aika: int):
    reseptit = lajittelu_aineet(tiedosto)
    words = []
    for avain in reseptit:
        if reseptit[avain]['aika'] <= aika:
            words.append(f"{reseptit[avain]['nimi']}, valmistusaika {reseptit[avain]['aika']} min")
    return words

def hae_raakaaine(tiedosto: str, aine: str):
    reseptit = lajittelu_aineet(tiedosto)
    words = []
    for avain in reseptit:
        if aine.lower() in [raaka_aine.lower() for raaka_aine in reseptit[avain]['alkuperaiset']]:
            words.append(f"{reseptit[avain]['nimi']}, valmistusaika {reseptit[avain]['aika']} min")
    return words


if __name__ == "__main__":
    loydetyt = hae_raakaaine("reseptit1.txt", "maito")

    for resepti in loydetyt:
        print(resepti)

