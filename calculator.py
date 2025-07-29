class Calculator:
    """Simple calculator class that performs basic operations."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def demo():
    """Demonstrate the calculator's functionality."""
    calc = Calculator()
    print("2 + 3 =", calc.add(2, 3))
    print("5 - 2 =", calc.subtract(5, 2))
    print("4 * 3 =", calc.multiply(4, 3))
    print("10 / 2 =", calc.divide(10, 2))

if __name__ == "__main__":
    demo()
