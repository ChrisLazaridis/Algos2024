# Δωθέντος ενός πίνακα θετικών n ακεραίων, να αναπτυχθεί αλγόριθμος βασισμένος στη τεχνική διαίρει και βασίλευε
# o οποίος θα βρει και θα επιστρέψει το max(A[j]/A[i], όπου i,j ∈ n και i < j.

# Βήματα για τη λύση
# 1. Χωρίζουμε το πίνακα σε 2 μισά
# 2. Βρίσκουμε το max(x[j]/x[i]) για το αριστερό και το δεξί μισό
# 3. Η λύση θα βρίσκεται ή δεξιά ή αριστερά ή στο cross
# 4. Συνδυάζουμε τα αποτελέσματα
# base case: n = 2, επιστρέφουμε το max(x[1]/x[0])
# Όμοια με Maximum SubArray
# T(n) = 2T(n/2) + O(n), θεώρημα κυρίαρχων όρων, περίπτωση τρία, χρονική πολυπλοκότητα Θ(n logn)

def max_cross(arr, start, mid, end):
    # Εύρεση ελάχιστου από το start μέχρι το mid
    min_left = float('inf')
    for i in range(start, mid):
        min_left = min(min_left, arr[i])

    # Εύρεση μέγιστου από το mid μέχρι το end
    max_right = float('-inf')
    for j in range(mid, end):
        max_right = max(max_right, arr[j])

    # Υπολογισμός του λόγου εάν ο ελάχιστος αριθμός αριστερά δεν είναι μηδέν
    if min_left != 0:
        return max_right / min_left
    return float('-inf')


def find_best_ratio(arr, start, end):
    # Βασική περίπτωση: αν το μήκος του υποπίνακα είναι μικρότερο από δύο
    if end - start < 2:
        return float('-inf')

    # Βασική περίπτωση: αν υπάρχουν ακριβώς δύο στοιχεία
    if end - start == 2:
        return arr[start + 1] / arr[start]

    mid = (start + end) // 2

    # Εύρεση των καλύτερων λόγων στα αριστερά, στα δεξιά και στο cross
    left_best = find_best_ratio(arr, start, mid)
    right_best = find_best_ratio(arr, mid, end)
    cross_best = max_cross(arr, start, mid, end)

    # Επιστροφή του μέγιστου από τα τρία αποτελέσματα
    return max(left_best, right_best, cross_best)


# Παράδειγμα χρήσης
array = [3, 8, 2, 8, 38, 48, 37]
array_length = len(array)
best_ratio = find_best_ratio(array, 0, array_length)
print(f"Best ratio is: {best_ratio}")
