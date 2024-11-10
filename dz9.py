class Calculator:
    def __init__(self):
        pass

    def str_to_float(self, value):
        try:
            return float(value)
        except ValueError:
            print(f"Помилка: '{value}' не можна конвертувати у float.")
            return None
        finally:
            print("Спроба конвертації завершена.")

    def add(self, a, b):
        a = self.str_to_float(a)
        b = self.str_to_float(b)
        if a is not None and b is not None:
            return a + b

    def subtract(self, a, b):
        a = self.str_to_float(a)
        b = self.str_to_float(b)
        if a is not None and b is not None:
            return a - b

    def multiply(self, a, b):
        a = self.str_to_float(a)
        b = self.str_to_float(b)
        if a is not None and b is not None:
            return a * b

    def divide(self, a, b):
        a = self.str_to_float(a)
        b = self.str_to_float(b)
        try:
            if a is not None and b is not None:
                if b == 0:
                    raise ZeroDivisionError("Помилка: Ділення на нуль недопустиме.")
                return a / b
        except ZeroDivisionError as e:
            print(e)
        finally:
            print("Спроба ділення завершена.")

calc = Calculator()

print(calc.add("10", "5"))  # Виведе: 15.0
print(calc.subtract("10", "abc"))
print(calc.multiply("3.5", "2"))
print(calc.divide("10", "0"))