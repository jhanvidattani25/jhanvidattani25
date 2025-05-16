def binary_search(arr, target):
    """
    Performs a binary search on a sorted list to find the index of a target element.

    Args:
        arr: A sorted list of elements.
        target: The element to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found at mid index
        elif arr[mid] < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half
    return -1  # Target not found in the list

# --- Example Usage ---
if __name__ == "__main__":
    my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"Original list: {my_list}")

    # Test cases
    target1 = 12
    result1 = binary_search(my_list, target1)
    if result1 != -1:
        print(f"Element {target1} found at index {result1}")
    else:
        print(f"Element {target1} not found in the list")

    target2 = 23
    result2 = binary_search(my_list, target2)
    if result2 != -1:
        print(f"Element {target2} found at index {result2}")
    else:
        print(f"Element {target2} not found in the list")

    target3 = 7
    result3 = binary_search(my_list, target3)
    if result3 != -1:
        print(f"Element {target3} found at index {result3}")
    else:
        print(f"Element {target3} not found in the list")

    target4 = 91
    result4 = binary_search(my_list, target4)
    if result4 != -1:
        print(f"Element {target4} found at index {result4}")
    else:
        print(f"Element {target4} not found in the list")

    target5 = 2
    result5 = binary_search(my_list, target5)
    if result5 != -1:
        print(f"Element {target5} found at index {result5}")
    else:
        print(f"Element {target5} not found in the list")
