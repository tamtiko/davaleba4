class Student:
    university = "Tbilisi State Medical University"

    def __init__(self, name: str, grade: int, age: int):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Grade: {self.grade},Age: {self.age}"

    @property
    def is_passing(self):
        return self.grade > 60

    def increase_grade(self, increase_by):
        self.grade += increase_by
        
stu = Student("Tamta", 70, 25)

print(stu.university)

print(stu.is_passing)

stu.increase_grade(10)

print(stu.grade)
