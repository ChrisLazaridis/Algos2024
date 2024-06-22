# QuickSort (κατά C.A.R. Hoare)
# Το πρόβλημα ταξινόμησης
# Διαίρει και Βασίλευε τεχνική
# για τη λύση
# Επιλογή ενός στοιχείου ως pivot
# Ταξινόμηση των στοιχείων μικρότερα από το pivot
# Ταξινόμηση των στοιχείων μεγαλύτερα από το pivot
# Πολυπλοκότητα: Θ(nlogn) στην καλύτερη περίπτωση, Θ(n^2) στη χειρότερη περίπτωση


def partition(arr, p, q):
    x = arr[p]  # pivot element
    i = p
    for j in range(p + 1, q + 1):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # exchange A[i] and A[j]
    arr[p], arr[i] = arr[i], arr[p]  # exchange A[p] and A[i]
    return i


def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)  # PARTITION(A, p, r) returns the pivot index
        quicksort(arr, p, q - 1)  # sort the left part
        quicksort(arr, q + 1, r)  # sort the right part


# Example usage
A = [10, 7, 8, 9, 1, 5]
n = len(A)
quicksort(A, 0, n - 1)
print("Sorted array is:", A)
