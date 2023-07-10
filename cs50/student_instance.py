class Student():
    #instance method
    #method is a function within a class
    def __init__(self, name, house):
        # customize class objects
        # initialize contents of an object
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student
