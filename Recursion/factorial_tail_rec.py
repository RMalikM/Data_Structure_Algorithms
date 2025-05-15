def factorial_tail_recursive(n, accumulator=1):
    """
    Calculate the factorial of a number using tail recursion.

    Args:
        n (int): The number for which the factorial is to be calculated.
                 Must be a non-negative integer.
        accumulator (int): The accumulated result of the factorial 
                           calculation. Defaults to 1.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return accumulator
    else:
        return factorial_tail_recursive(n-1, accumulator*n)
    
if __name__=='__main__':
    n = 4
    fact = factorial_tail_recursive(n)
    print(f"Factorial of {n} is: {fact}")