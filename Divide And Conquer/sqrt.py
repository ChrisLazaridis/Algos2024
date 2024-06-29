# Να αναπτυχθεί αλγόριθμος που να βρίσκει τη ρίζα ενός μη αρνητικού αριθμού, απλοποιημένο στο πλησιέστερο ακέραιο
# Διαίρει και βασίλευε: δυαδική αναζήτηση
# Η ιδέα είναι πολύ απλή
# αν mid* mid = x τότε το βρήκα
# αλλιώς αλλάζω τα left/right αναλόγως
# αν δεν το βρώ επιστρέφω ένα εκ των left/right της τελευταίας επανάληψης (δεν έχει ιδιαίτερη σημασία)
def sqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x
    left = 1
    right = x // 2
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Χρονική πολυπλοκότητα: O(logx) λόγω της δυαδικής αναζήτησης
# Χωρική πολυπλοκότητα: O(c)
