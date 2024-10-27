class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 50  # рівень щастя от 0 до 100
        self.energy = 50     # рівень енергії от 0 до 100

    def eat(self):
        self.energy += 20
        self.happiness += 10
        print(f"{self.name} Енергія: {self.energy}, Щасливість: {self.happiness}")

    def play(self):
        if self.energy >= 15:
            self.energy -= 15
            self.happiness += 20
            print(f"{self.name} енергія: {self.energy}, Щасливість: {self.happiness}")
        else:
            print(f"{self.name} занадто втомився для гри")

    def sleep(self):
        self.energy += 30
        print(f"{self.name} сон Енергія: {self.energy}")

    def make_sound(self):
        if self.species.lower() == 'cat':
            print(f"{self.name} говорить: Мяу!")
        elif self.species.lower() == 'dog':
            print(f"{self.name} говорить: Гав!")
        else:
            print(f"{self.name} говорить: Неизвестный звук.")
cat = Pet("Сем", "cat")
dog = Pet("Ден", "dog")

cat.eat()
cat.play()
cat.make_sound()

dog.eat()
dog.sleep()
dog.make_sound()