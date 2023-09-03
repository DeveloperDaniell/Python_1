import math

def points():
    total_points = []

    while True:
        user_input = input("Enter exam score and number of exercise tasks: ")
        if user_input == "":
            break

        input_list = user_input.split()
        if len(input_list) == 2:
            exam_score = int(input_list[0])
            exercise_tasks = int(input_list[1])
            failed = False
            if exam_score < 10:
                failed = True
            total_points.append((exam_score + math.floor(exercise_tasks * 0.1), failed, exam_score))

    return total_points


def calculate_grade(points):
    if points < 10:
        return 0
    elif points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    elif points <= 30:
        return 5


def grade_distribution(total_points):
    grade_counter = [0] * 6  # Grade counters

    for points, failed, dummy in total_points:
        if not failed:
            grade = calculate_grade(points)
        else:
            grade = 0
        grade_counter[grade] += 1

    print("Arvosanajakauma:")
    for i in range(5, -1, -1):
        stars = "*" * grade_counter[i]
        print("  {}: {}".format(i, stars))


def average(total_points):
    avg = sum(points for points, failed, dummy in total_points) / len(total_points)
    return round(avg, 1)


def pass_percentage(total_points):
    passed = [points for points, failed, score in total_points if (not failed and calculate_grade(points) > 0) ]
    pass_percentage = len(passed) / len(total_points) * 100
    return round(pass_percentage, 1)


def main():
    points_list = points()

    if not points_list:
        print("No input. Program ends.")
        return

    print("Tilasto:")
    print("Pisteiden keskiarvo: {:.1f}".format(average(points_list)))
    print("Hyväksymisprosentti: {:.1f}".format(pass_percentage(points_list)))
    grade_distribution(points_list)


main()
