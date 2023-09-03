def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi] = []

def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
    kurssi, arvosana = suoritus
    if nimi in opiskelijat:
        if not opiskelijat[nimi]:  # jos ei suorituksia
            opiskelijat[nimi] = [(kurssi, arvosana)]
        else:
            for i, (k, a) in enumerate(opiskelijat[nimi]):
                if k == kurssi:  # jos kurssi jo olemassa, päivitetään arvosana
                    if a < arvosana:  # otetaan parempi suoritus
                        opiskelijat[nimi][i] = (kurssi, arvosana)
                    break
            else:  # jos kurssi ei ollut olemassa
                opiskelijat[nimi].append((kurssi, arvosana))

def tulosta(opiskelijat: dict, nimi: str):
    if nimi in opiskelijat:
        print(f"{nimi}:")
        suoritukset = opiskelijat[nimi]
        if suoritukset:
            arvosanat = []
            for kurssi, arvosana in suoritukset:
                if arvosana > 0:  # vain arvosanat yli 0 otetaan huomioon
                    arvosanat.append(arvosana)
            if arvosanat:  # vain jos on suorituksia yli 0
                print(" suorituksia", len(arvosanat), "kurssilta:")
                for kurssi, arvosana in suoritukset:
                    if arvosana > 0:  # vain arvosanat yli 0 otetaan huomioon
                        print(f"  {kurssi} {arvosana}")
                keskiarvo = sum(arvosanat) / len(arvosanat)
                print(" keskiarvo", keskiarvo)
            else:
                print(" ei suorituksia")
        else:
            print(" ei suorituksia")
    else:
        print(f"ei löytynyt ketään nimellä {nimi}")


def kooste(opiskelijat: dict):
    print(f"opiskelijoita {len(opiskelijat)}")
    
    eniten_suorituksia = ""
    suurin_maara = 0

    for opiskelija, suoritukset in opiskelijat.items():
        kurssit = set(kurssi for kurssi, arvosana in suoritukset if arvosana > 0)
        if len(kurssit) > suurin_maara:
            suurin_maara = len(kurssit)
            eniten_suorituksia = opiskelija

    print(f"eniten suorituksia {suurin_maara} {eniten_suorituksia}")

    paras = ""
    paras_keskiarvo = 0
    
    for opiskelija, suoritukset in opiskelijat.items():
        if suoritukset:
            arvosanat = [arvosana for kurssi, arvosana in suoritukset if arvosana > 0]
            if arvosanat:  # tarkistetaan, että arvosanoja on enemmän kuin nolla
                keskiarvo = sum(arvosanat) / len(arvosanat)
                if keskiarvo > paras_keskiarvo:
                    paras_keskiarvo = keskiarvo
                    paras = opiskelija

    print(f"paras keskiarvo {paras_keskiarvo} {paras}")


    

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    kooste(opiskelijat)