def counting_sort(arr):
    max_val = max(arr) if arr else 0  # O(n)
    min_val = min(arr) if arr else 0  # O(n)
    range_of_elements = max_val - min_val + 1

    # Create carr array and barr array
    carr = [0] * range_of_elements  # O(k)
    barr = [0] * len(arr)  # O(n)

    # Store the carr of each element in the carr array
    for num in arr:  # O(n)
        carr[num - min_val] += 1

    # Update the carr array to store the cumulative carr of elements
    for i in range(1, len(carr)):  # O(k)
        carr[i] += carr[i - 1]

    # Build the barr array
    for num in reversed(arr):  # O(n)
        barr[carr[num - min_val] - 1] = num
        carr[num - min_val] -= 1

    return barr


# # Example Usage
# A = [12, 11, 13, 5, 6, 7]
# Sorted = counting_sort(A)
# print(f"Sorted Array: {Sorted}")
