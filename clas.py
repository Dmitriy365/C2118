print('Lesson 3: Work with several classes\n')
class StudySubject:
    name: str
    hours: int
    level: str
    def __init__(self, name: str, hours: int, level: str):
        self.name = name
        self.hours = hours
        self.level = level
    def __str__(self):
        return f'{self.name} {self.level}, кількість годин {self.hours}'
class Student:
    first_name: str
    second_name: str
    age: int
    is_offline: bool
    study_subject: StudySubject
    def __init__(self, second_name: str, first_name: str, age: int, study_subject: StudySubject, is_offline=True):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.is_offline = is_offline
        self.study_subject = study_subject
    def __str__(self):
        study_type: str
        if self.is_offline:
            study_type = 'offline'
        else:
            study_type = 'online'
        student_info = f'{self.second_name} {self.first_name}, вік {self.age}, навчається {study_type}'
        return f'{student_info}\n{self.study_subject}'
py_senior = StudySubject('Python', 18, 'Senior')
DushlyukMakar = Student('Дишлюк', "Макар", 13, py_senior)
print(DushlyukMakar)
class Teacher:
    first_name: str
    last_name: str
    subject: StudySubject

    def __init__(self, first_name: str, last_name: str, subject: StudySubject):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject

    def __str__(self):
        return f'Вчитель: {self.last_name} {self.first_name}, викладає {self.subject}'


python_teacher = Teacher('Олександр', 'Іваненко', py_senior)

print(python_teacher)

class Group:
    name: str
    students: list
    teacher: Teacher

    def __init__(self, name: str, teacher: Teacher):
        self.name = name
        self.students = []
        self.teacher = teacher

    def add_student(self, student: Student):
        self.students.append(student)

    def __str__(self):
        student_info = ', '.join(str(student) for student in self.students)
        return f'Група: {self.name}, Викладач: {self.teacher}\nСтуденти: {student_info}'

python_teacher = Teacher('Олександр', 'Іваненко', py_senior)
python_group = Group('Python Група 1', python_teacher)

python_group.add_student(DushlyukMakar)

print(python_group)