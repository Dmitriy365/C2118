class StudySubject:
    def __init__(self, name: str, hours: int, enable: bool):
        self.name = name
        self.hours = hours
        self.enable = enable

    def info_study(self):
        print(f'Study: {self.name} | {self.hours}')
class Student:
    def __init__(self, name: str, surname: str, studies: list):
        self.name = name
        self.surname = surname
        self.studies = studies
    def info_student(self):
        print(f'Student: {self.name} | {self.surname}')
    def info_all(self):
        self.info_student()
        for study in self.studies:
            study.info_study()
class Group:
    def __init__(self, group_name: str, age_category: str):
        self.group_name = group_name
        self.students = []
        self.age_category = age_category

    def add_student(self, student: Student):
        self.students.append(student)
    def info_group(self):
        print(f'Group: {self.group_name} | Age Category: {self.age_category} | Total Students: {len(self.students)}')
        for student in self.students:
            student.info_all()
def main():
    group_name = input("Enter group name: ")
    age_category = input("Enter age category: ")

    group = Group(group_name, age_category)

    while True:
        name = input("Enter student's name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break

        surname = input("Enter student's surname: ")

        studies = []
        while True:
            subject_name = input("Enter subject name (or 'done' to finish): ")
            if subject_name.lower() == 'done':
                break

            hours = int(input("Enter hours for the subject: "))
            enable = input("Is the subject enabled? (yes/no): ").lower() == 'yes'
            studies.append(StudySubject(subject_name, hours, enable))

        student = Student(name, surname, studies)
        group.add_student(student)

    group.info_group()
main()