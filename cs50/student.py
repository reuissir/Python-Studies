import csv

# with open("students.csv") as file:
    # for line in file:
        # name, house = line.rstrip().split(",")
        # print(f"{name} is in {house}")

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

    # for line in file:
        # name, home = line.rstrip().split(",")
        # student = {"name": name, "home": home}
        # ->
        # student["name"] = name
        # student["house"] = house

        # students.append(student)

# def get_name(student):
    # return student["name"]

# def get_house(student):
    # return student["house"]

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")

