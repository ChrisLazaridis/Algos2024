# Θεωρόντας μια επέκταση του προβλήματος του σακιδίου με όγκο V, αξία προϊόντος pi και μέγιστο μεταφερόμενο βαρός W
# Να ευρεθεί ένας αλγόριθμος δυναμικού προγραμματισμού που να βρίσκει το μέγιστο profit και αν αναλυθεί χρονικά
# αναδρομή για απλό πρόβλημα knapsack
def knapsack_recursive(p, w, W_, n):
    if n < 0:
        return 0
    elif w[n - 1] > W_:  # Αν δεν μπορείς να το πάρεις, άστο
        return knapsack_recursive(p, w, W_, n - 1)
    else:
        take_i = knapsack_recursive(p, w, W_ - w[n - 1], n - 1) + p[n - 1]  # Πάρτο
        skip_i = knapsack_recursive(p, w, W_, n - 1)  # Μη το πάρεις
        return max(take_i, skip_i)


# προφανώς και για αυτό το πρόβλημα δεν κάνει αλλά αποτελεί μια καλή βάση
# Ουσιαστικά θα βάλουμε και άλλο ένα check, κατά τα άλλα έχω ίδιο base case
def knapsack_extended_recursive(p, w, v, W_, V_, n):
    if n < 0:
        return 0
    elif w[n - 1] > W_ or v[n - 1] > V_:
        return knapsack_extended_recursive(p, w, v, W_, V_, n - 1)
    else:
        take_i = knapsack_extended_recursive(p, w, v, W_ - w[n - 1], V_ - v[n - 1], n - 1) + p[n - 1]
        skip_i = knapsack_extended_recursive(p, w, v, W_, V_, n - 1)
        return max(take_i, skip_i)


def knapsack_extended_dynamic(p, w, v, W_, V_, n, dp):
    if n < 0:
        return 0

    if dp[n] != -1:
        return dp[n]

    if w[n - 1] > W_ or v[n - 1] > V_:
        dp[n] = knapsack_extended_dynamic(p, w, v, W_, V_, n - 1, dp)
    else:
        take_i = knapsack_extended_dynamic(p, w, v, W_ - w[n - 1], V_ - v[n - 1], n - 1, dp) + p[n - 1]
        skip_i = knapsack_extended_dynamic(p, w, v, W_, V_, n - 1, dp)
        dp[n] = max(take_i, skip_i)

    return dp[n]


# Time complexity: O(n) όπως κάθε memoization αλγόριθμος (ελπίζω να το δέχεται
# Space complexity: O(n) λόγω του dp array

def knapsack_extended_helper(p, w, v, W_, V_):
    if len(p) == 0 or len(p) != len(w) != len(v) or W_ == 0 or V_ == 0:
        return 0
    else:
        n = len(p)
        dp = [-1] * (n + 1)
        return knapsack_extended_dynamic(p, w, v, W_, V_, n, dp)


# Example usage
p = [60, 100, 120]
w = [10, 20, 30]
v = [5, 10, 15]
W_ = 50
V_ = 30

result = knapsack_extended_helper(p, w, v, W_, V_)

print(f"result is: {result}")