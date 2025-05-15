def calculate(n):
    """
    Recursively calculates and prints the square of numbers from n down to 1.

    Args:
        n (int): The starting number. Must be a positive integer.

    Returns:
        None
    """
    if n > 0:
        k = n**2
        print(k)
        calculate(n-1)

if __name__=='__main__':
    n = 4
    calculate(n)