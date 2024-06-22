# Το πρόβλημα της ύψωσης σε δύναμη
# Έστω ότι έχουμε δύο ακέραιους αριθμούς x και n. Να γραφεί αλγόριθμος που υπολογίζει το x^n.
# Ο αλγόριθμος πρέπει να είναι αποδοτικός, δηλαδή να χρειάζεται όσο το δυνατόν λιγότερες πράξεις για να υπολογίσει το x^n.
# για τη λύση
# Βασική περίπτωση: Αν n = 0, τότε το αποτέλεσμα είναι 1.
# Αν n είναι άρτιος, τότε x^n = (x^(n/2))^2
# Αν n είναι περιττός, τότε x^n = x * x^(n-1)
# Πολυπλοκότητα: Θ(logn)

def power(x, n):
    # Base case: x^0 is 1
    if n == 0:
        return 1

    # Recursive case: divide the problem into smaller sub-problems
    half_power = power(x, n // 2)

    # Combine the results of sub-problems
    if n % 2 == 0:
        return half_power * half_power
    else:
        return x * half_power * half_power


# Test the solution
x = 2
n = 10
result = power(x, n)
print(f"{x}^{n} is", result)
