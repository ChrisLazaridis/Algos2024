# Δοθέντος ενός πίνακα Α n στοιχείων να σχεδιαστεί αλγόριθμος ο οποίος να επιστρέφει ένα πίνακα less n στοιχείων
# ο οποίος θα έχει στη θέση less[i] το πλήθος των στοιχείων που βρίσκονται δεξιά του A[i] στο πίνακα Α και ταυτόχρονα
# θα είναι μικρότερά του, σε χρόνο O(n log(n)) στη χειρότερη περίπτωση.
# Αναδρομική λύση brute force
# για κάθε i θα ελέγξω όλα τα δεξιά στοιχεία του πίνακα
# αν είναι μικρότερα του A[i] θα αυξήσω την θέση i στο πίνακα less
# Για κάθε i θα κάνω n - i συγκρίσεις
# T(n) = Σ{i = 1, n} (n - i) = n(n-1)/2 = O(n^2)
def find_elements(arr, less, index, index2):
    # αν και τα 2 indexes Βρίσκονται στο n τότε τελείωσα
    if index == len(arr) and index2 == len(arr):
        return less
    # αν μόνο το index2 βρίσκεται στο n τότε τελείωσα με το αντίστοιχο i
    if index2 == len(arr) and index < len(arr):
        return find_elements(arr, less, index + 1, index + 2)
    if arr[index2] < arr[index]:
        less[index] += 1
    return find_elements(arr, less, index, index2 + 1)


def find_elements_helper(arr):
    # αρχικοποίηση πίνακα less με μηδενικά
    less = [0] * len(arr)
    return find_elements(arr, less, 0, 1)


# Δεν επαρκεί
# Νεα ιδέα, διαίρει και βασίλευε: Merge sort. (GPT'ed λύση)
# Τροποποίηση της merge sort έτσι ώστε να μετράει τα στοιχεία που είναι μικρότερα από ένα i
def merge_and_count(arr, start, mid, end, less):
    left = arr[start:mid]
    right = arr[mid:end]
    i = 0  # Δείκτης για τον αριστερό πίνακα
    j = 0  # Δείκτης για τον δεξιό πίνακα
    k = start  # Δείκτης για τον αρχικό πίνακα

    # Μέχρι να τελειώσουμε με ένα πίνακα μετράμε
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # αν κάνω merge κάτι από το αριστερό partition, αυξάνω τον αντίστοιχο counter
            # δεν έχω ιδέα γιατί
            arr[k] = left[i]
            less[left[i][1]] += j  # Αυξάνουμε τον μετρητή του i (left [i][1] γιατί θέλουμε το δείκτη του αντίστοιχου στοιχείου)
            # κατά j (δεν έχω ιδεά γιατί)
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Αντιγράφουμε όλα τα στοιχεία του άλλου πίνακα που μας έμειναν
    while i < len(left):
        arr[k] = left[i]
        less[left[i][1]] += j
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort_and_count(arr, start, end, less):
    # απλή αναδρομή για τη merge sort με την υπορουτίνα merge and count αντί για merge
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort_and_count(arr, start, mid, less)
        merge_sort_and_count(arr, mid, end, less)
        merge_and_count(arr, start, mid, end, less)


def count_smaller(arr):
    less = [0] * len(arr)
    # ένας πίνακας δεικτών για να διατηρήσουμε τις αρχικές θέσεις των δεικτών
    # 2 διαστάσεις, στο indexed_nums[i][0] είναι τα νούμερα π κάνουμε sort και μετράμε και στα [i][1] το αρχικό index
    indexed_nums = [(num, idx) for idx, num in enumerate(arr)]
    merge_sort_and_count(indexed_nums, 0, len(indexed_nums), less)
    return less


# Example Usage
arr = [5, 2, 6, 1]
result = count_smaller(arr)
print(result)

# Προφανώς O(n log(n)) λόγω merge sort
# Θα έγραφα το πρώτο σε χρόνο O(n^2) με την ελπίδα να έπαιρνα έστω μισή μονάδα
