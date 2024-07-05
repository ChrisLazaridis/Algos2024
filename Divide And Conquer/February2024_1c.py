# 'Έστω πίνακας Α, Ν διαφορετικών στοιχείων με το χαρακτηριστικό πως υπάρχει i τέτοιο ώστε:
# η ακολουθία A[0] ... A[i] να είναι γνησίως αύξουσα και η ακολουθία A[i+1] .. A[N] να είναι γνησίως φθίνουσα
# Να αναπτυχθεί αλγόριθμος της τεχνικής διαίρει και βασίλευε που να επιστρέφει το i και να αναλυθεί χρονικά
# Βασική περίπτωση: Αν Α[i] > A[i -1] και A[i] < A[i + 1] bingo
def find_i(A: list[int]) -> int:
    left = 0
    right = len(A)
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
            return mid
        if A[mid - 1] < A[mid] < A[mid + 1]:
            return left = mid
        if A[mid - 1] > A[mid] > A[mid + 1]
            right = mid
