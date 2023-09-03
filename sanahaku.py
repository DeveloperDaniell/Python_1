import re

def hae_sanat(hakusana: str):
    sanat = []
    with open("sanat.txt", 'r') as tiedosto:
        for rivi in tiedosto:
            sana = rivi.strip()
            if hakusana.startswith('*'):
                if sana.endswith(hakusana.replace('*', '')):
                    sanat.append(sana)
            elif hakusana.endswith('*'):
                if sana.startswith(hakusana.replace('*', '')):
                    sanat.append(sana)
            elif '.' in hakusana:
                pattern = hakusana.replace('.', '.')
                if re.fullmatch(pattern, sana):
                    sanat.append(sana)
            else:
                if sana == hakusana:
                    sanat.append(sana)
    return sanat
