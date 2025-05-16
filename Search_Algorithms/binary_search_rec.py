def bianry_search_recursive(arr, k, L, R):
    """
    Perform binary search on a sorted array recursively.

    :param arr: List of sorted elements
    :param k: Element to search for
    :param L: Left index
    :param R: Right index
    :return: Index of the target element if found, otherwise -1
    """
    if L > R:
        return -1

    mid = (L + R) // 2

    if arr[mid] == k:
        return mid
    elif arr[mid] < k:
        return bianry_search_recursive(arr, k, mid + 1, R)
    else:
        return bianry_search_recursive(arr, k, L, mid - 1)
    
if __name__ == "__main__":
    arr = [5, 21, 36, 42, 55, 62, 79, 83, 90]
    k = 83
    result = bianry_search_recursive(arr, k, 0, len(arr) - 1)
    if result != -1:
        print(f"Element {k} found at index {result}.")
    else:
        print(f"Element {k} not found in the array.")