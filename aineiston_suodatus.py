def suodata_laskut():
    with open("laskut.csv") as file:
        with open("oikeat.csv", "w") as oikeat, open("vaarat.csv", "w") as vaarat:
            for row in file:
                parts = row.strip().split(";")
                calculation = parts[1]
                given_answer = int(parts[2])

                # Compute the actual answer
                if "+" in calculation:
                    actual_answer = int(calculation.split("+")[0]) + int(calculation.split("+")[1])
                else:  # "-"
                    actual_answer = int(calculation.split("-")[0]) - int(calculation.split("-")[1])

                if actual_answer == given_answer:
                    oikeat.write(row + "\n")
                else:
                    vaarat.write(row + "\n")
