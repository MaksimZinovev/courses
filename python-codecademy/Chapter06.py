# ========= Dictionaries and loops=========
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]
for student in students:
    print(student['name'])
    print(student['homework'])
    print(student['quizzes'])
    print(student['tests'])


def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)


# print "Average: %s" % average(tyler["tests"])
def get_average(stdnt):
    homework = average(stdnt["homework"])
    quizzes = average(stdnt["quizzes"])
    tests = average(stdnt["tests"])
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6


person = alice
print("Average weights for %s: %s" % (person["name"], get_average(person)))


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


person = lloyd
print("--------------")
print("Grade for %s: %s" % (person["name"], get_letter_grade(get_average(lloyd))))


def get_class_average(class_list):
    results = []
    for student in class_list:
        results.append(get_average(student))
    return average(results)


avg=get_class_average(students)
print("")
print("----Class Average------")
print("Class average %s:" % avg)
print("Which is %s:" % get_letter_grade(avg))
