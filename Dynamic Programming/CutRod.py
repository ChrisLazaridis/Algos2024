# Το πρόβλημα της εύρεσης μέγιστου κέρδους για τη κοπή μιας μπάρας
# Αναδρομικά υπολογίζω το κέρδος
# Ισχύει πως p[i] το κέρδος για τη μια μπάρα μήκους i
# Έσοδο rn = max(pn,r1 + rn-1, r2 + rn-2, ... , rn-1 + r1) <=> rn = max(pi + rn-i)
# Με απλή αναδρομή
def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cut_rod(p, n - i))
    return q


# T(n) = Σ{j = 0, n - 1} (T(j)) + 1 <=> O(2^n)
# Κακό, χρήση δυναμικού προγραμματισμού ως εξής
def dynamic_cut_rod(p, n):
    r = [float('-inf')] * (n + 1)
    return dynamic_cut_rod_aux(p, n, r)


def dynamic_cut_rod_aux(p, n, dp):
    if dp[n] >= 0:
        return dp[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n + 1):
            if i <= len(p):  # Check if i is within the bounds of p
                q = max(q, p[i - 1] + dynamic_cut_rod_aux(p, n - i, dp))
    dp[n] = q
    return q


# example usage
p = [1, 2, 3, 4, 5, 7, 10]
n = 15
result = dynamic_cut_rod(p, n)
print(f"result: {result}")
