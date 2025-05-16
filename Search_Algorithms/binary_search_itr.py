def BinarySearchItr(arr, k):
    """
    Perform binary search on a sorted array iteratively.

    :param arr: List of sorted elements
    :param target: Element to search for
    :return: Index of the target element if found, otherwise -1
    """
    L = 0
    R = len(arr) - 1

    while L <= R:
        mid = (L + R) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            L = mid + 1
        else:
            R = mid - 1

    return -1

if __name__ == "__main__":
    arr = [5, 21, 36, 42, 55, 62, 79, 83, 90]
    k = 83
    result = BinarySearchItr(arr, k)
    if result != -1:
        print(f"Element {k} found at index {result}.")
    else:
        print(f"Element {k} not found in the array.")