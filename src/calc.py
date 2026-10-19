
class Calculator:
    def add(self, a, b):
        return a + b

    def calculate(self, a, b):
        return a - b


class AdvancedCalculator(Calculator):
    def add(self, a, b):
        return a * b

    def calculate(self, a, b):
        return a / b if b != 0 else "Error: division by zero"


class PowerCalculator(Calculator):
    def add(self, a, b):
        return a ** b

    def calculate(self, a, b):
        return a % b if b != 0 else "Error: division by zero"


calc = Calculator()
advanced = AdvancedCalculator()
power = PowerCalculator()

print("Parent:", calc.add(5, 3), calc.calculate(5, 3))
print("Advanced:", advanced.add(5, 3), advanced.calculate(5, 3))
print("Power:", power.add(5, 3), power.calculate(5, 3))
