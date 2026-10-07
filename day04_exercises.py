def divide_safely(a: float, b: float) -> float | str:
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
