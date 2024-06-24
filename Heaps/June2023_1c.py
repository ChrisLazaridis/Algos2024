# Δοθέντος ενός πίνακα n στοιχείων, να αναπτυχθεί αλγόριθμος που θα επιστρέφει τα |√(n)| μικρότερα στοιχεία,
# ταξινομημένα κατά αύξουσα σειρά σε χρόνο O(n) στη χειρότερη περίπτωση
import math
import random
from Sorts.CountingSort import counting_sort


def find_sqrtlen_smallest_elements(arr):
    arr = counting_sort(arr)  # O(n)
    k = int(math.sqrt(len(arr)))
    barr = []
    for i in range(k):  # O(√(n))
        barr.append(arr[i])
    return barr


# Example Usage
array = [random.randint(1, 100) for _ in range(100)]
array = find_sqrtlen_smallest_elements(array)
print(array)
