# Problem: Find the Second Largest Element in a List
# Category: Arrays (Lists in Python)
# Approach: Single-pass comparison
# Complexity: O(n) time, O(1) space
# Example:
#   Input: [10, 5, 8, 20]
#   Output: 10

def second_largest_element(numbers):
    """
    Returns the second largest number in the given list.
    :param numbers: List of integers
    :return: Integer (second largest element)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")

    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    if second_largest == float('-inf'):
        raise ValueError("No second largest element found (all elements might be equal).")

    return second_largest


if _name_ == "_main_":
    try:
        # Input as comma-separated integers
        nums = list(map(int, input("Enter the numbers (comma-separated): ").split(',')))
        result = second_largest_element(nums)
        print(f"Second Largest Element: {result}")
    except ValueError as e:
        print("Error:", e)
