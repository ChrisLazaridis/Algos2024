# Έστω ένα εργοστάσιο και ένα σύνολο παραγγελιών που πρέπει να εκτελεστούν
# Κάθε παραγγελία k πρέπει να ολοκληρωθεί σε μια συγκεκριμένη χρονική στιγμή f[k]
# και αποφέρει όφελος g[k]. Επίσης προκειμένου να έχει ολοκληρωθεί μια παραγγελία k την απαιτούμενη χρονική στιγμή
# f[k] θα πρέπει να εκκινήσει τη χρονική στιγμή s[k]. Κάθε χρονική στιγμή μπορεί να επεξεργασθεί μόνο μια παραγγελία
# Να βρεθεί το σύνολο των μη επικαλυπτόμενων παραγγελιών με το μέγιστο δυνατό όφελος χρησιμοποιώντας τη τεχνική του
# δυναμικού προγραμματισμού
# Αρχικά με αναδρομή κλασσικά
# base case: μ τελείωσαν οι δουλειές, επιστρέφω το κέρδος
# αν έχω πάρει δουλειά, τότε σκιπάρω μέχρι το σημείο στο οποίο τελειώνει
# αλλιώς μπορώ είτε να πάρω είτε να μην πάρω
# Παραδοχές: Υπάρχουν διακριτές χρονικές στιγμές

def factory_gains_rec(f, g, s, index, gain):
    if index > len(s):  # δεν υπάρχει άλλη δουλειά να πάρω
        return gain
    new_index = index
    while s[new_index] < f[index]:
        new_index += 1
    take = factory_gains_rec(f, g, s, new_index, gain + g[index])
    not_take = factory_gains_rec(f, g, s, index + 1, gain)
    return max(take, not_take)


# με δυναμικό με memoization
# κάθε χρονική στιγμή έχει κάποια τιμή στο πίνακα
# σημείωση, πρέπει να βρεθεί το σύνολο των παραγγελιών

def factory_gains_dynamic(f, g, s, index, gain, dp, orders):
    if dp[index, gain] != []:
        return gain, dp[index, gain]
    if index > len(s):
        dp[index, gain] = orders
        return gain, dp[index, gain]
    new_index = index
    while s[new_index] < f[index]:
        new_index += 1
    new_orders = orders
    new_orders.append(index)
    take, order_list_for_take = factory_gains_dynamic(f, g, s, new_index, gain + g[index], dp, new_orders)
    not_take, order_list_for_no_take = factory_gains_dynamic(f, g, s, index + 1, gain, dp, orders)
    if take > not_take:
        dp[index, take] = order_list_for_take
        return take, order_list_for_take
    else:
        dp[index, not_take] = order_list_for_no_take
        return not_take, order_list_for_no_take


def factory_gains_helper(f, g, s):
    if len(f) != len(g) != len(s):
        return 0
    n = len(f)
    orders = []
    max_gain = sum(g)
    dp = [[[] for _ in range(max_gain + 1)] for _ in range(n + 1)]
    max_gain, orders = factory_gains_dynamic(f, g, s, 0,0, dp, orders)
    return max_gain, orders

# Example usage:
f = [3, 5, 8]
g = [50, 10, 40]
s = [0, 3, 5]
max_gain, orders = factory_gains_helper(f, g, s)
print(f"Max Gain: {max_gain}")
print(f"Order List: {orders}")


# προσπάθησα αλλά είναι λάθος
# θέλει bottom-up somehow