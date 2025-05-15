def factorial_rec(n):
    """
    Calculate the factorial of a number using recursion.

    :param n: The number to calculate the factorial for.
    :return: The factorial of the number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return factorial_rec(n - 1) * n  # Recursive call
    
if __name__ == "__main__":
    num = int(input("Enter a number to calculate factorial: "))
    try:
        result = factorial_rec(num)
        print(f"The factorial of {num} is: {result}")
    except ValueError as e:
        print(e)