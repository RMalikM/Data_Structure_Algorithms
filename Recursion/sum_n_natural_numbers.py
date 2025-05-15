def sum_N(n):
    """
    Function to calculate the sum of first n natural numbers using recursion.
    :param n: The number up to which the sum is to be calculated.
    :return: The sum of first n natural numbers.
    """
    if n == 0:
        return 0
    else:
        return sum_N(n - 1) + n # Recursive call
    
if __name__ == "__main__":
    n = 10
    result = sum_N(n)
    print(f"The sum of the first {n} natural numbers is: {result}")