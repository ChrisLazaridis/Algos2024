# Το πρόβλημα της μέγιστης υποσυστοιχίας
# Έστω ένας πίνακας A = [a1, a2, ..., an] ακεραίων. Να βρεθεί η συστοιχία του πίνακα που έχει το μεγαλύτερο άθροισα.
# Διαίρει και Βασίλευε τεχνική
# Η ιδέα είναι η διαίρεση του αρχικού πίνακα σε 2 μισά και η λύση του προβλήματος για τα 2 μισά. Έπειτα συνδυάζονται οι
# λύσεις. Η μέγιστη συστοιχία θα μπορούσε να βρίσκεται σε ένα από τα 3 μέρη:
# 1. Στο αριστερό μισό του πίνακα
# 2. Στο δεξί μισό του πίνακα
# 3. Στο διάστημα που περνάει από το αριστερό μισό στο δεξί μισό του πίνακα
# Βήματα:
# Διαίρεση του πίνακα στα 2 μισά
# Αναδρομικά βρές τη μέγιστη συστοιχία σε κάθε μισό
# Βρες τη μέγιστη συστοιχία που περνάει από το αριστερό μισό στο δεξί μισό (midpoint) και συνδύασε τις λύσεις
# Πολυπλοκότητα: Θ(nlogn)

def max_crossing_sum(a, low, mid, high):
    # Include elements on left of mid
    left_sum = float('-inf')  # -∞
    sum_ = 0
    for i in range(mid, low - 1, -1):
        sum_ += a[i]
        if sum_ > left_sum:
            left_sum = sum_

    # Include elements on right of mid
    right_sum = float('-inf')
    sum_ = 0
    for i in range(mid + 1, high + 1):
        sum_ += a[i]
        if sum_ > right_sum:
            right_sum = sum_

    # Return sum of elements on left and right of mid
    return left_sum + right_sum


def max_subarray_sum(a, low, high):
    # Base case: only one element
    if low == high:
        return a[low]

    # Find middle point
    mid = (low + high) // 2

    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the subarray crosses the midpoint
    return max(max_subarray_sum(a, low, mid),
               max_subarray_sum(a, mid + 1, high),
               max_crossing_sum(a, low, mid, high))


# Test the solution
arr = [2, 3, -4, 5, 7, -8, 9, -3]
n = len(arr)
result = max_subarray_sum(arr, 0, n - 1)
print("Maximum subarray sum is", result)
