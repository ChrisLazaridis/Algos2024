# Θεωρόντας μια επέκταση του προβλήματος του σακιδίου με όγκο V, αξία προϊόντος pi και μέγιστο μεταφερόμενο βαρός W
# Να ευρεθεί ένας αλγόριθμος δυναμικού προγραμματισμού που να βρίσκει το μέγιστο profit και αν αναλυθεί χρονικά
# αναδρομή για απλό πρόβλημα knapsack
def knapsack_recursive(p, w, W_, n):
    # Base case: δεν έχω άλλα αντικείμενα ή χώρο
    if n == 0 or W_ == 0:
        return 0
    # αν το βάρος του nοστού αντικειμένου είναι μεγαλύτερο από αυτό π μπορώ να κουβαλήσω, τότε δεν το παίρνω
    elif w[n - 1] > W_:
        return knapsack_recursive(p, w, W_, n - 1)
    else:
        take_i = knapsack_recursive(p, w, W_ - w[n - 1], n - 1) + p[n - 1]
        skip_i = knapsack_recursive(p, w, W_, n - 1)
        return max(take_i, skip_i)


def knapsack_extended_recursive(p, w, v, W_, V_, n):
    # Base case: δεν έχω άλλα αντικείμενα ή χώρο ή όγκο
    if n == 0 or W_ == 0 or V_ == 0:
        return 0
    # αν το βάρος ή ο όγκος του nοστού αντικειμένου είναι μεγαλύτερος από το παρεχόμενο, δεν μπορώ να το πάρω
    elif w[n - 1] > W_ or v[n - 1] > V_:
        return knapsack_extended_recursive(p, w, v, W_, V_, n - 1)
    else:
        take_i = knapsack_extended_recursive(p, w, v, W_ - w[n - 1], V_ - v[n - 1], n - 1) + p[n - 1]
        skip_i = knapsack_extended_recursive(p, w, v, W_, V_, n - 1)
        return max(take_i, skip_i)


def knapsack_extended_dynamic(p, w, v, W_, V_, n, dp):
    if n == 0 or W_ == 0 or V_ == 0:
        dp[n][W_][V_] = 0
        return 0

    # αν το έχω βρει
    if dp[n][W_][V_] != -1:
        return dp[n][W_][V_]

    # αν το βάρος ή ο όγκος του nοστού αντικειμένου είναι μεγαλύτερος από το παρεχόμενο, δεν μπορώ να το πάρω
    if w[n - 1] > W_ or v[n - 1] > V_:
        dp[n][W_][V_] = knapsack_extended_dynamic(p, w, v, W_, V_, n - 1, dp)
    else:
        take_i = knapsack_extended_dynamic(p, w, v, W_ - w[n - 1], V_ - v[n - 1], n - 1, dp) + p[n - 1]
        skip_i = knapsack_extended_dynamic(p, w, v, W_, V_, n - 1, dp)
        dp[n][W_][V_] = max(take_i, skip_i)

    return dp[n][W_][V_]


def knapsack_extended_helper(p, w, v, W_, V_):
    if len(p) == 0 or len(p) != len(w) != len(v) or W_ == 0 or V_ == 0:
        return 0
    else:
        n = len(p)
        dp = [[[-1] * (V_ + 1) for _ in range(W_ + 1)] for _ in range(n + 1)]
        return knapsack_extended_dynamic(p, w, v, W_, V_, n, dp)


# Example usage
p = [60, 100, 120]
w = [10, 20, 30]
v = [5, 10, 15]
W_ = 30
V_ = 30

result = knapsack_extended_helper(p, w, v, W_, V_)

print(f"result is: {result}")
