class Calculator:
    def convert_to_float(self, value):
        try:
            return float(value)
        except ValueError:
            print(f"Неможливо конвертувати '{value}'float.")
            return None
        finally:
            print("Спроба конвертації завершена.")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("Ділення на нуль не можливе.")
            return a / b
        except ZeroDivisionError as e:
            print(e)
            return None
        finally:
            print("Спроба ділення завершена.")
calc = Calculator()

num1 = calc.convert_to_float("10")
num2 = calc.convert_to_float("0")

result_add = calc.add(num1, num2)
print(f"Результат додавання: {result_add}")


result_subtract = calc.subtract(num1, num2)
print(f"Результат віднімання: {result_subtract}")

result_multiply = calc.multiply(num1, num2)
print(f"Результат множення: {result_multiply}")

result_divide = calc.divide(num1, num2)
print(f"Результат ділення: {result_divide}")