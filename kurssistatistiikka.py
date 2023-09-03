import urllib.request
import json

def hae_kaikki():
    page = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(page.read().decode())

    results = []
    for course in data:
        if course['enabled']:
            name = course['fullName']
            short_name = course['name']
            year = course['year']
            exercises = sum(course['exercises'])
            results.append((name, short_name, year, exercises))

    print(results)

def hae_kurssi(kurssi: str):
    page = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{kurssi}/stats")
    data_dict = json.loads(page.read().decode())

    weeks = len(data_dict)
    total_students = 0
    total_hours = 0
    total_tasks = 0
    
    for entry in data_dict.values():
        total_students += entry['students']
        total_hours += entry['hour_total']
        total_tasks += entry['exercise_total']

    average_hours = total_hours / weeks
    average_tasks = total_tasks / weeks
    
    result = {
        'viikkoja': weeks,
        'opiskelijoita': total_students,
        'tunteja': total_hours, 
        'tunteja_keskimaarin': average_hours,
        'tehtavia': total_tasks,
        'tehtavia_keskimaarin': average_tasks,
        }
    print(result)


        




if __name__ == "__main__":
    hae_kaikki()
    hae_kurssi("docker2019")    
