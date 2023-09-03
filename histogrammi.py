def histogrammi(merkkijono: str):
    merkit = {}
    for merkki in merkkijono:
        if not merkki in merkit:
            merkit[merkki] = 0
        merkit[merkki] += 1
 
    for merkki, lkm in merkit.items():
        tahdet = "*"*lkm
        print(f"{merkki} {tahdet}")



if __name__ == "__main__":
    ryhmat = histogrammi("abba")

