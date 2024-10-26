
class Student:
    def __init__(self, first_name, last_name, subject_name, homework_count):
        self.first_name = first_name
        self.last_name = last_name
        self.subject_name = subject_name
        self.homework_count = homework_count

    def describe(self):
        return (f"Студент: {self.first_name} {self.last_name}\n"
                f"Предмет: {self.subject_name}\n"
                f"Кількість домашніх завдань: {self.homework_count}")
student1 = Student("Іван", "Сергійович", "Математика", 5)
print(student1.describe())