from app_logic import set_first_value, get_first_value
from utils import parse_post, render_template
def calc(environ):
    method = environ["REQUEST_METHOD"]
    result = ""
    if method == "POST":
        data = parse_post(environ)
        try:
            num1 = float(data.get("num1", [""])[0])
            num2 = float(data.get("num2", [""])[0])
            operation = data.get("operation", [""])[0]
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "無限大"
            else:
                result = "不明な操作"
        except ValueError:
            result = "無効な入力"

    return render_template("boundaries/calc.html", result=result)