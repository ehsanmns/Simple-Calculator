def add(x: float, y: float) -> float:
    """Return the sum of two numbers."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Return the difference between two numbers."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Return the product of two numbers."""
    return x * y

def divide(x: float, y: float) -> float:
    """
    Return the quotient of two numbers.
    
    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    if y == 0:
        raise ZeroDivisionError("division by zero")
    return x / y

if __name__ == "__main__":
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            try:
                print(num1, "/", num2, "=", divide(num1, num2))
            except ZeroDivisionError as e:
                print("Error:", str(e))
        else:
            print("Invalid input. Please enter a valid choice.")
