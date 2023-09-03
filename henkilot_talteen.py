def tallenna_henkilo(henkilo: tuple):
    with open("henkilot.csv", "a") as file:
        name, age, height = henkilo
        row = f"{name};{age};{height}\n"
        file.write(row)

if __name__ == "__main__":
    tallenna_henkilo(("Kimmo Kimmonen", 37, 175.5))
