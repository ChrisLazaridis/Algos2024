# Ταξινόμηση ένθεσης
# Αλγόριθμος ταξινόμησης που διατηρεί μια υπολίστα από ταξινομημένα στοιχεία
# και εισάγει το επόμενο στοιχείο στη σωστή θέση.
# Εξωτερικό loop: Επεξεργάζεται το κάθε στοιχείο της λίστας από το δεύτερο μέχρι το τέλος.
# Το στοιχείο στο οποίο βρίσκεται είναι το key που θα μπει στη σωστή θέση.
# Εσωτερικό loop: Συγκρίνει το key με τα στοιχεία της υπολίστας από το τέλος προς την αρχή.
# Όσο το στοιχείο της υπολίστας είναι μεγαλύτερο από το key, το μετακινεί μια θέση δεξιά.
# Όταν βρει τη θέση που πρέπει να μπει το key, το εισάγει στη θέση αυτή.
# Χρονική πολυπλοκότητα: O(n^2).
# Κακή ταξινόμηση εκτός αν η λίστα είναι σχεδόν ταξινομημένη.


def insertion_sort(arr):
    n = len(arr)
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


# Example usage
A = [12, 11, 13, 5, 6]
insertion_sort(A)
print("Sorted array is:", A)
