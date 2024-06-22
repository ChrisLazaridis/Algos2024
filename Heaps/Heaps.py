def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Αν το αριστερό παιδί είναι μεγαλύτερο από το root
    if left < n and arr[i] < arr[left]:
        largest = left

    # Αν το δεξί παιδί είναι μεγαλύτερο από το root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Αν ο μεγαλύτερος δεν είναι το root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Κάνε heapify το υποδέντρο
        heapify(arr, n, largest)


def build_heap(arr):
    n = len(arr)

    # Φτιάξε το max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
