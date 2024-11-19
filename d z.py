import logging

logging.basicConfig(
    filename='calculation.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.ERROR
)

class Calculation:
    def __call__(self, operation, a, b):
        try:
            a = self.convert_to_number(a)
            b = self.convert_to_number(b)
            if operation == '+':
                return a + b
            elif operation == '-':
                return a - b
            elif operation == '*':
                return a * b
            elif operation == '/':
                return self.divide(a, b)
            else:
                raise ValueError("Невідома помелка")
        except Exception as e:
            logging.error(f"Виникла помилка: {e}")
            return f"Помилка: {e}"

    def convert_to_number(self, value):

        try:
            if isinstance(value, (int, float)):
                return value

            return float(value)
        except ValueError as e:
            logging.error(f"Помилка конвертації: {e} для значення {value}")
            raise

    def divide(self, a, b):

        if b == 0:
            raise ZeroDivisionError("Ділення на нуль не можліво")
        return a / b

calc = Calculation()
result = calc('+', '5', '10')
print(result)
result = calc('/', '10', '0')
print(result)
result = calc('*', '3.2', '2')
print(result)