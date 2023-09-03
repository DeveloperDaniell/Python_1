from datetime import datetime

def huijarit():
    aloitukset = {}
    cheaters = []
    with open("tentin_aloitus.csv", "r") as file:
        for row in file:
            parts = row.strip().split(";")
            name = parts[0]
            start_str = parts[1]
            aloitukset[name] = datetime.strptime(start_str, '%H:%M')

    with open("palautus.csv", "r") as file_2:
        for row in file_2:
            parts_2 = row.strip().split(";")
            name_2 = parts_2[0]
            end_str = parts_2[3]
            end = datetime.strptime(end_str, '%H:%M')

            if name_2 in aloitukset:
                start = aloitukset[name_2]
                difference = end - start
                if difference.total_seconds() / 3600 > 3:
                    if name_2 not in cheaters:
                        cheaters.append(name_2)

    return cheaters

def viralliset_pisteet():
    cheaters = huijarit()
    points = {}
    
    with open("palautus.csv", "r") as file:
        for row in file:
            parts = row.strip().split(";")
            name = parts[0]
            if name not in cheaters:
                task_no = int(parts[2])
                task_points = int(parts[4])
                if name in points:
                    if task_no in points[name]:
                        if task_points > points[name][task_no]:
                            points[name][task_no] = task_points
                    else:
                        points[name][task_no] = task_points
                else:
                    points[name] = {task_no: task_points}
    
    for student in points:
        points[student] = sum(points[student].values())
    
    return points

if __name__ == "__main__":
    print(viralliset_pisteet())
