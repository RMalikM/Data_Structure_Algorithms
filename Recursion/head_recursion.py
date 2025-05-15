def calculate(n):
    """
    Recursively calculates and prints the square of numbers from 1 to n.

    Args:
        n (int): The starting number. Must be a positive integer.

    Returns:
        None
    """
    if n > 0:
        calculate(n-1)
        k = n**2
        print(k)

if __name__=='__main__':
    n = 4
    calculate(n)