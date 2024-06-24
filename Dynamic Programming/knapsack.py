# Πρόβλημα knapsack ακεραίων (0/1)
# Έστω n αντικείμενα, w ο πίνακας με τα βάρη των αντικειμένων και p ο πίνακας με το κέρδος σε χρηματικές μονάδες
# των αντικειμένων, να αναπτυχθεί αλγόριθμος σε δυναμικό προγραμματισμό ο οποίος να βρίσκει το μέγιστο κέρδος το οποίο
# μπορεί να επιτευχθεί, με δεδομένο το βάρος που μπορεί να κουβαληθεί σε μια δεδομένη χρονική στιγμή (W_)
# Αρχικά με αναδρομή:
# Για κάθε αντικείμενο οφείλω να πάρω μια απόφαση, θα το πάρω ή όχι?
# Βασική περίπτωση: n < 0 , δεν μένει άλλο αντικείμενο, άρα επέστρεψε 0
# Αν δεν έχω αρκετό χώρο τότε skipάρω το αντικείμενο
# Αλλιώς παίρνω απόφαση (μπορεί να το πάρω μπορεί και όχι, θα δείξει) (σημείωση, μην ξεχαστεί να μπει το + p[i])
# Σημείωση, το n-1 παντού οφείλεται στο μηδενικό indexing (κάθε πίνακς έχει από 0 μέχρι n - 1 στοιχεία)
# με απλή αναδρομή
def knapsack_recursive(p, w, W_, n):
    if n < 0:
        return 0
    elif w[n - 1] > W_:  # Αν δεν μπορείς να το πάρεις, άστο
        return knapsack_recursive(p, w, W_, n - 1)
    else:
        take_i = knapsack_recursive(p, w, W_ - w[n - 1], n - 1) + p[n - 1]  # Πάρτο
        skip_i = knapsack_recursive(p, w, W_, n - 1)  # Μη το πάρεις
        return max(take_i, skip_i)


# Χρόνος T(n) = 0 if n==0 else T(n-1) + T(n-1) + 2 = 2T(n-1) + 2 = O(2^n)
# ΆΘΛΙΟ
# Με δυναμικό προγραμματισμό memoization
def knapsack_dynamic(p, w, W_, n, dp):
    if n < 0:
        return 0
    if dp[n] != -1 :
        return dp[n]
    if w[n - 1] > W_:
        dp[n] = knapsack_dynamic(p, w, W_, n - 1, dp)
    else:
        take_i = knapsack_dynamic(p, w, W_ - w[n - 1], n - 1, dp) + p[n - 1]
        skip_i = knapsack_dynamic(p, w, W_, n - 1, dp)
        dp[n] = max(take_i, skip_i)
    return dp[n]


def knapsack_helper(p, w, W_):
    if len(p) == 0 or len(p) != len(w) or W_ == 0:
        return 0
    else:
        n = len(p)
        dp = [-1] * (n + 1)
        return knapsack_dynamic(p, w, W_, n, dp)


# Example usage:
p = [60, 100, 120]
w = [10, 20, 30]
W_ = 50
result = knapsack_helper(p, w, W_)
print(f"result is: {result}")
