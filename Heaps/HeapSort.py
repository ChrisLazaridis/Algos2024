# Ταξινόμηση με χρήση σωρού μεγίστων (HeapSort)
# Το πρώτο στοιχείο του σωρού θα είναι πάντα και το μεγαλύτερο, αφάιρεσε το
# Έπειτα το εναλλάσσεις με το τελευταίο στοιχείο του σωρού και κάνεις heapify
# Επανάλαβε μέχρι το σωρός να είναι άδειος
# Η πολυπλοκότητα του αλγορίθμου είναι O(n log n)
from Heaps import build_heap, heapify


def heap_sort(arr):
    n = len(arr)

    build_heap(arr)

    # Ένας - ένας αφαίρεσε τα στοιχεία από το heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Test the solution
a = [12, 11, 13, 5, 6, 7]
heap_sort(a)
print("Sorted array is", a)
