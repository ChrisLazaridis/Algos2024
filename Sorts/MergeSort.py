# Συγχωνευτική ταξινόμηση (Merge Sort)
# Η συγχωνευτική ταξινόμηση είναι ένας αλγόριθμος ταξινόμησης που χρησιμοποιεί την αρχή της διαίρει και βασίλευε.
# Αρχικά, χωρίζουμε τον κάθε πίνακα σε δύο υποπίνακες μέχρι να φτάσουμε σε υποπίνακες με μέγεθος 1.
# Στη συνέχεια, συγχωνεύουμε τους υποπίνακες με τέτοιο τρόπο ώστε να παράγεται ένας ταξινομημένος πίνακας.
# Η πολυπλοκότητα του αλγορίθμου είναι Θ(nlogn).
# Ο αλγόριθμος αυτός είναι αποδοτικός για μεγάλους πίνακες.
# Από το κώδικα δεν φαίνεται και πολύ καλά ο τρόπος χρήσης, δες  https://www.youtube.com/watch?v=4VqmGXwpLqc

def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2

        # Dividing the elements into two halves
        l = arr[:mid]
        r = arr[mid:]

        # Recursively sort the two halves
        merge_sort(l)
        merge_sort(r)

        # Merging the sorted halves
        i = j = k = 0

        # Copy data to temp arrays l[] and r[]
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        # Checking if any element was left in l[]
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        # Checking if any element was left in r[]
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


# Example usage
A = [12, 11, 13, 5, 6, 7]
merge_sort(A)
print("Sorted array is:", A)
