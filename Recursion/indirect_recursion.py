def calculateA(n):
    """
    Demonstrates indirect recursion by calculating and printing the square 
    of the number and then calling calculateB.

    Args:
        n (int): The current number. Must be a positive integer.

    Returns:
        None
    """
    if n > 0:
        k = n**2
        print(k)
        calculateB(n-1)

def calculateB(n):
    """
    Demonstrates indirect recursion by calculating and printing the cube 
    of the number and then calling calculateA.

    Args:
        n (int): The current number. Must be a positive integer.

    Returns:
        None
    """
    if n > 0:
        k = n**3
        print(k)
        calculateA(n-1)

if __name__ == "__main__":
    n = 5
    print("Indirect Recursion")
    calculateA(n)    # or calculateB(n)
    print("End of Indirect Recursion")