from flask import Flask
from calculator import Calculator

app = Flask(__name__)

@app.route('/')
def index():
    calc = Calculator()
    results = [
        f"2 + 3 = {calc.add(2, 3)}",
        f"5 - 2 = {calc.subtract(5, 2)}",
        f"4 * 3 = {calc.multiply(4, 3)}",
        f"10 / 2 = {calc.divide(10, 2)}",
    ]
    # Return results as simple HTML
    return '<br>'.join(results)

if __name__ == '__main__':
    # Run the Flask development server
    app.run()
