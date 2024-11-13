class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        pass

    def attend_lecture(self):
        pass

class Worker(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def work(self):
        pass

    def attend_meeting(self):
        pass

def get_attributes(cls):
    return [attr for attr in dir(cls) if not callable(getattr(cls, attr)) and not attr.startswith("__")]
def get_methods(cls):
    return [method for method in dir(cls) if callable(getattr(cls, method)) and not method.startswith("__")]

print("Атрибути класу Student:")
print(get_attributes(Student))

print("\nМетоди класу Student:")
print(get_methods(Student))

print("\nАтрибути класу Worker:")
print(get_attributes(Worker))

print("\nМетоди класу Worker:")
print(get_methods(Worker))