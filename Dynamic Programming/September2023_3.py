# Έστω ακολουθία από n νομίσματα με μη αρνητικές αλλά όχι απαραίτητα διαφορετικές αξίες. Να αναπτυχθεί αλγόριθμος σε
# δυναμικό προγραμματισμό ο οποίος θα υπολογίζει το μέγιστο χρηματικό ποσό το οποίο και μπορούμε να μαζέψουμε με τη
# προϋπόθεση πως δεν μπορούμε να πάρουμε 2 γειτονικά νομίσματα.
# Αρχική αναδρομή με backtracking
# Βασική περίπτωση: n-2 <= 0, με 3 υποπεριπτώσεις, επέστρεψε ή 0, ή carr[0] ή το max των 2 τελευταίων
# Απόφαση αναδρομής, είτε παίρνω ένα νόμισμα είτε παίρνω το επόμενο του
# Επιστρέφω το μέγιστο
# T(n) = 1, n<=2 else T(n-1) + T(n-2) + 1 <=> O(2^n) (αναμενόμενο)
# ΛΆΑΑΑΑΑΑΘΟΣ

def max_money_recursive(carr, n, current):
    if n == 0:
        return 0
    if n == 1:
        return carr[0]
    if n == 2:
        return max(carr[0], carr[1])
    current = max_money_recursive(carr, n - 2, current) + carr[n - 1]
    new_current = max_money_recursive(carr, n - 1, current)
    return max(current, new_current)


# Με δυναμικό προγραμματισμό

def max_money_dynamic(carr, n, rd):
    if rd[n] != -1:
        return rd[n]
    if n == 0:
        rd[n] = 0
    elif n == 1:
        rd[n] = carr[0]
    elif n == 2:
        rd[n] = max(carr[0], carr[1])
    else:
        current = max_money_dynamic(carr, n - 2, rd) + carr[n - 1]
        new_result = max_money_dynamic(carr, n - 1, rd)
        rd[n] = max(current, new_result)
    return rd[n]


def max_money_helper(carr):
    n = len(carr)
    if n == 0:
        return 0
    r = [-1] * (n + 1)
    return max_money_dynamic(carr, n, r)


# Χρονική πολυπλοκότητα: Ο(n) και χωρική πολυπλοκότητα O(n)
# Example usage
array = [0, 4, 2, 2, 2, 2, 2, 7, 8, 2, 1, 0, 4, 9]
# result = max_money_recursive(array, len(array), 0)
result = max_money_helper(array)
print(f"result: {result}")
