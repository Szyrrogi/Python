class Student:
    students = []

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_student(self, name):
        self.students.append(name)

    def add_grade(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.grades.append(grade)
                break

student1 = Student("Jan")
student1.add_student(student1)
student1.add_grade("Jan", 5)
print(student1.grades)