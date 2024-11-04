class Person:
    name: str
    surname: str
    age: int

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def info_person(self):
        print(f'person:\t{self.name} | {self.surname} | {self.age}')


class Teacher(Person):
    subject: str
    hours: int

    def __init__(self, subject: str, hours: int, name: str, surname: str, age: int):
        self.subject = subject
        self.hours = hours
        super().__init__(name=name, surname=surname, age=age)

    def info_teacher(self):
        print(f'teacher:\t{self.subject} | {self.hours}')

    def info_all(self):
        self.info_person()
        self.info_teacher()


class Group:
    name: str
    student_count: int

    def __init__(self, name: str, student_count: int):
        self.name = name
        self.student_count = student_count

    def info_group(self):
        print(f'group:\t{self.name} | student count: {self.student_count}')


class Student(Person):
    progress: float  # успішність
    group: Group     # група
    pensione: bool   # пенсіонний статус

    def __init__(self, name: str, surname: str, age: int, progress: float, group: Group):
        super().__init__(name=name, surname=surname, age=age)
        self.progress = progress
        self.group = group
        self.set_pensione(age)

    def set_pensione(self, age: int):
        self.pensione = age >= 60

    def info_student(self):
        print(f'student:\t{self.name} | {self.surname} | {self.age} | progress: {self.progress}')
        self.group.info_group()
        print(f'pensione: {self.pensione}')


class Worker(Person):
    position: str    # посада
    duties: str      # обов'язки
    pensione: bool   # пенсіонний статус

    def __init__(self, name: str, surname: str, age: int, position: str, duties: str):
        super().__init__(name=name, surname=surname, age=age)
        self.position = position
        self.duties = duties
        self.set_pensione(age)

    def set_pensione(self, age: int):
        self.pensione = age >= 60

    def info_worker(self):
        print(f'worker:\t{self.name} | {self.surname} | {self.age} | position: {self.position}')
        print(f'duties: {self.duties}')
        print(f'pensione: {self.pensione}')

group_a = Group(name='Group A', student_count=25)
student = Student(name='Ivan', surname='Ivanov', age=22, progress=85.0, group=group_a)
student.info_student()

worker = Worker(name='Oleg', surname='Olegov', age=65, position='Manager', duties='Oversee operations')
worker.info_worker()

teacher = Teacher(subject='Pycharm', hours=24, name='unknown_name', surname='unknown_surname', age=30)
teacher.info_all()