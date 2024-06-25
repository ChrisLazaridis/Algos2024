# Το πρόβλημα: Δοθέντος ενός πίνακας prices για τον οποίο ισχύει ότι prices[i] είναι η τιμή μιας μετοχής την i-οστή μέρα
# Θέλουμε να μεγιστοποιήσουμε το κέρδος αγοράζοντας μια συγκεκριμένη μέρα και πουλώντας σε μια μεταγενέστερη
# Επέστρεψε το μέγιστο κέρδος το οποίο μπορεί να επιτευχθεί από μια τέτοια συναλλαγή
# Λύση: Αρχικά με αναδρομή
# Αν έχω μετοχή στην κατοχή μου τότε: Μπορώ να πουλήσω ή όχι
# Αν δεν έχω μετοχή στην κατοχή μου τότε μπορώ να αγοράσω ή και όχι
# Βασικές περιπτώσεις, αν δεν έχω κατοχή στη κατοχή μου στο τέλος επιστρέφω μηδέν
# αλλιώς επιστρέφω το κέρδος
def max_money_recursive(prices, n=0, bought=-1):
    if n == len(prices):
        if bought != -1:
            return prices[-1] - bought
        else:
            return 0
    else:
        if bought != -1:
            return max(prices[n] - bought, max_money_recursive(prices, n + 1, bought))
        else:
            return max(max_money_recursive(prices, n + 1, prices[n]), max_money_recursive(prices, n + 1, bought))


# Κλασσικά κάκιστο
# Πάμε για δυναμικό
# Προσοχή, 2 πιθανές καταστάσεις, άρα 2 γραμμές στο dp
# Θα χρειαστώ και ένα flag, αν bought == 1 τότε έχω μετοχή


def max_money_dynamic(prices, n, bought_price, dp):
    bought = 1 if bought_price != -1 else 0
    if n == len(prices):
        if bought == 1:
            dp[n][bought] = prices[-1] - bought_price
            return dp[n][bought]
        else:
            dp[n][bought] = 0
            return 0

    if dp[n][bought] != -1:
        return dp[n][bought]

    if bought == 1:
        dp[n][1] = max(prices[n] - bought_price,
                       max_money_dynamic(prices, n + 1, bought_price, dp))
    else:
        dp[n][0] = max(max_money_dynamic(prices, n + 1, prices[n], dp),
                       max_money_dynamic(prices, n + 1, -1, dp))

    return dp[n][bought]


def max_money(prices):
    n = len(prices)

    if n == 0:
        return 0
    else:
        dp = [[-1 for _ in range(2)] for _ in range(n + 1)]
        return max_money_dynamic(prices, 0, -1, dp)


# Example Usage
array = [7, 1, 5, 3, 6, 4]
result = max_money(array)
print(f"result: {result}")

# Χρονική πολυπλοκότητα Ο(n^2) και χωρική O(2n) = O(n) (η στοίβα αναδρομών είναι κατά μέγιστο 2n στη χειρότερη περίπτωση)
