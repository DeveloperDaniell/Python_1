name = input("Kenelle teos omistetaan: ")
place = input("Mihin kirjoitetaan: ")

with open(place, "w") as file:
    file.write(f"Hei {name}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi ")