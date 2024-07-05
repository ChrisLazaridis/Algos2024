# Ένας κάνει n ταξίδια με κόστος c1,c2,..,cn και μπορεί να αγοράσει ενα κουπόνι με κόστος r να του δώσει e% έκπτωση
# Ο πίνακας d περιέχει τις ημερομηνίες και τα κουπόνια έχουν ισχύει ένα χρόνο αλλά μπορεί να πάρει μόνο 1 τη φορά
# Να επιστραφούν οι ημερομηνίες στις οποίες πρέπει να αγοράσει κουπόνια έτσι ώστε να ελαχιστοποιηθεί το κόστος
import math


# τα γνωστά με αναδρομή
# Αν έχω κουπόνι τότε έχω έκπτωση και συνεχίζω την αναδρομή
# Αν οχι τότε δοκιμάζω τι θα γίνει αν αγοράσω και αν όχι
# Αν πάλι τελειώσουν τα ταξίδια επιστρέφω τα ανάλογα
def findBestDates(d, c, r, cost, arr, index, bought_date):
    if index >= len(d):
        return cost, arr

    if d[index] - bought_date < 365:
        new_cost = cost + c[index] * (1 - math.e / 100)
        return findBestDates(d, c, r, new_cost, arr, index + 1, bought_date)
    else:
        arr_with_coupon = arr + [d[index]]
        cost_with_coupon = cost + r + c[index] * (1 - math.e / 100)
        total_cost_with_coupon, final_arr_with_coupon = findBestDates(d, c, r, cost_with_coupon, arr_with_coupon,
                                                                      index + 1, d[index])

        total_cost_without_coupon, final_arr_without_coupon = findBestDates(d, c, r, cost + c[index], arr, index + 1,
                                                                            bought_date)
        if total_cost_with_coupon < total_cost_without_coupon:
            return total_cost_with_coupon, final_arr_with_coupon
        else:
            return total_cost_without_coupon, final_arr_without_coupon


# Με δυναμικό memoization, εδώ για ευκολία χρησιμοποιώ dictionary, key ένα tuple, ο συνδυασμός Index και ημερομηνίας
# και value ένα άλλο tuple, ο συνδυασμός αποτελέσματος και array στο οποίο αποθηκεύονται οι ημερομηνίες αγοράς
# ΥΓ: ΑΓΑΠΆΩ ΤΗ PYTHON
dp = {}


def findBestDatesHelper(d, c, r):
    arr = []
    cost = 0
    bought_date = -float('inf')
    total_cost, best_dates = findBestDatesDynamic(d, c, r, cost, arr, 0, bought_date, dp)
    return best_dates, total_cost


def findBestDatesDynamic(d, c, r, cost, arr, index, bought_date):
    if index >= len(d):
        return cost, arr
    key = (index, bought_date)

    if key in dp:
        return dp[key]

    if d[index] - bought_date < 365:
        new_cost = cost + c[index] * (1 - math.e / 100)
        result = findBestDates(d, c, r, new_cost, arr, index + 1, bought_date)
    else:
        arr_with_coupon = arr + [d[index]]
        cost_with_coupon = cost + r + c[index] * (1 - math.e / 100)
        total_cost_with_coupon, final_arr_with_coupon = findBestDates(d, c, r, cost_with_coupon, arr_with_coupon,
                                                                      index + 1, d[index])

        total_cost_without_coupon, final_arr_without_coupon = findBestDates(d, c, r, cost + c[index], arr, index + 1,
                                                                            bought_date)

        if total_cost_with_coupon < total_cost_without_coupon:
            result = (total_cost_with_coupon, final_arr_with_coupon)
        else:
            result = (total_cost_without_coupon, final_arr_without_coupon)

    dp[key] = result
    return result

# ΥΓ1: δεν έχω ίδεα για χρονικές πολυπλοκότητες, θα μάντευα O(n^2) διότι κάθε index έχει n πιθανές τιμές στο πίνακα
# ΥΓ2: να τα σκεφτείς όλα αυτά σε ψευδοκώδικα καληνύχτα
# ΥΓ3: να του αποδείξεις πως λειτουργούν όλα αυτά καληνύχτα
# ΥΓ4: Θέμα 1β καληνύχτα
# ΥΓ5: καληνύχτα
# ΥΓ6: η δική μ αναδρομή ήταν ένα μαύρο χάλι και μου την έφτιαξε το chat gpt
# ΥΓ7: είναι 5 και 22 το πρωί
