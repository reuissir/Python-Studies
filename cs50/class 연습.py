# 객체를 만드는 함수
# 추상화(abstraction): 필요한 요소만을 사용해서 객체를 표현하기
# 복잡한 자료, 모듈, 시스템 등으로부터 핵심적인 개념 또는 기능을 간추려 내는 것을 추상화라고 한다

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return("{} is {}years old and is majoring in {} at Seoul National University!".format(self.name, self.age, self.major))


def main():
    Student = get_student()
    print(Student)

def get_student():
    name = input("What is your name?: ")
    age = input("what is your age?: ")
    major = input("what is your major? ")

if __name__ == "__main__":
    main()