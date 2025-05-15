def calculate(n):
    """
    Demonstrates tree recursion by recursively calculating and printing 
    the square of numbers from n down to 1 in a tree-like structure.

    Args:
        n (int): The starting number. Must be a positive integer.

    Returns:
        None
    """
    if n > 0:
        calculate(n - 1)
        k = n**2
        print(k)
        calculate(n - 1)

if __name__ == "__main__":
    n = 3
    calculate(n)