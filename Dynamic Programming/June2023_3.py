# Θεωρόντας μια επέκταση του προβλήματος του σακιδίου με όγκο V, αξία προϊόντος pi και μέγιστο μεταφερόμενο βαρός W
# Να ευρεθεί ένας αλγόριθμος δυναμικού προγραμματισμού που να βρίσκει το μέγιστο profit και αν αναλυθεί χρονικά
# Χρόνος δικής μου (ο θεός να τη κάνει) εκδοχής: O(n * v) = O(n)
def knapsack_mine(p, v, w, V_, W_):
    dp = [[0] * (V_ + 1) for _ in range(len(p) + 1)]
    for i in range(len(p) + 1):
        for j in range(V_ + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j] + p[i] if (v[i - 1] + v[i] < V_ and w[i - 1] + w[i] < W_) else 0)
    return dp[len(p)][V_]


# Σωστή λύση
def knapsack(p, v, w, V_, W_):
    n = len(p)
    dp = [[0] * (V_ + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(V_ + 1):
            if v[i - 1] <= j:  # Check if we can include the i-th item
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v[i - 1]] + p[i - 1] if w[i - 1] <= W_ else dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][V_]


def knapsack_memoization(p, v, w, V_, W_):
    n = len(p)
    memo = {}

    def knapsack_helper(i, remaining_v):
        if i == 0 or remaining_v == 0:
            return 0

        if (i, remaining_v) in memo:
            return memo[(i, remaining_v)]

        if v[i - 1] > remaining_v:
            result = knapsack_helper(i - 1, remaining_v)
        else:
            take_item = p[i - 1] + knapsack_helper(i - 1, remaining_v - v[i - 1]) if w[i - 1] <= W_ else 0
            skip_item = knapsack_helper(i - 1, remaining_v)
            result = max(take_item, skip_item)

        memo[(i, remaining_v)] = result
        return result

    return knapsack_helper(n, V_)
