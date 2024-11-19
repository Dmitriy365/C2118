class ArithmeticOperations:
    def __init__(self):
        self.add = self.addition
        self.subtract = self.subtraction
        self.multiply = self.multiplication
        self.divide = self.division

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Ділення на нуль не можливе.")
        return a / b

    def _check_type(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return True
        return False

    def perform_operation(self, op, a, b):
        if not self._check_type(a, b):
            raise TypeError("Обидва аргументи мають бути int або flot.")
        return op(a, b)


arithmetic = ArithmeticOperations()

try:
    print("Сума:", arithmetic.perform_operation(arithmetic.add, 5, 3))
    print("Різниця:", arithmetic.perform_operation(arithmetic.subtract, 5, 3))
    print("Добутокr:", arithmetic.perform_operation(arithmetic.multiply, 5, 3))
    print("Ділення:", arithmetic.perform_operation(arithmetic.divide, 5, 0))
except (ValueError, TypeError) as e:
    print("Помилка:", e)
