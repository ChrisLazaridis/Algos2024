# Given an array of positive integers, n elements. Develop an algorithm based on the divide and conquer algorithm
# that will find and return the max(x[j]/x[i]) where i,j in n and i < j.

# Βήματα για τη λύση
# 1. Χωρίζουμε το πίνακα σε 2 μισά
# 2. Βρίσκουμε το max(x[j]/x[i]) για το αριστερό και το δεξί μισό
# 3. Η λύση θα βρίσκεται ή δεξιά ή αριστερά ή στο cross
# 4. Συνδυάζουμε τα αποτελέσματα
# base case: n = 2, επιστρέφουμε το max(x[1]/x[0])
# Όμοια με Maximum SubArray
# T(n) = 2T(n/2) + O(n^2), θεώρημα κυρίαρχων όρων, περίπτωση τρία, χρονική πολυπλοκότητα Θ(n^2)

def max_cross(arr, start, mid, end):
    max_ratio = float('-inf')
    for i in range(start, mid):
        for j in range(mid, end):
            if arr[i] != 0:  # Ensure no division by zero
                max_ratio = max(max_ratio, arr[j] / arr[i])
    return max_ratio


def find_best_ratio(arr, start, end):
    # Base case: if the segment length is less than two
    if end - start < 2:
        return float('-inf')
    # Base case: if there are exactly two elements
    if end - start == 2:
        return arr[start + 1] / arr[start]

    mid = (start + end) // 2

    # Return the maximum of the three results
    return max(find_best_ratio(arr, start, mid), find_best_ratio(arr, mid, end), max_cross(arr, start, mid, end))


# Example Usage
array = [1, 2, 6, 3, 8, 2, 8, 38, 48, 37]
array_length = len(array)
best_ratio = find_best_ratio(array, 0, array_length)
print(f"Best ratio is: {best_ratio}")
