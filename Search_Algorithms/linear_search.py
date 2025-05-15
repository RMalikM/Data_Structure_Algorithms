def LSearch(arr, k):
    """
    Linear Search Algorithm
    :param arr: List/Array of elements to search
    :param k: Element to search for
    :return: Index of the target element (k) if found, otherwise -1
    """
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

if __name__ == "__main__":
    # Example usage
    arr = [22, 56, 99, 100, 32]
    k = 99
    result = LSearch(arr, k)
    if result != -1:
        print(f"Element {k} found at index {result}.")
    else:
        print(f"Element {k} not found in the array.")