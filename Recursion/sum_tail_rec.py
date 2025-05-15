def sum_tail_recursive(lst, accumulator=0):
    """
    Computes the sum of a list of numbers using tail recursion.

    This function uses an accumulator to keep track of the running total,
    allowing the recursion to be tail-recursive.

    Args:
        lst (list): A list of numbers to sum.
        accumulator (int, optional): The running total of the sum. Defaults to 0.

    Returns:
        int: The sum of the numbers in the list.

    Example:
        >>> sum_tail_recursive([1, 2, 3, 4])
        10
        >>> sum_tail_recursive([])
        0
    """
    if not lst:
        return accumulator
    else:
        return sum_tail_recursive(lst[1:], accumulator+lst[0])
    
if __name__=='__main__':
    lst = [1,2,3,4]
    res = sum_tail_recursive(lst)
    print(f"Sum of the elements of {lst} is: {res}")