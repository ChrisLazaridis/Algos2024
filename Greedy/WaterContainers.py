# Δοθέντος ενός πίνακα height μεγέθους n, κάθε θέση του πίνακα δηλώνει τα υποτιθέμενα άκρα ενός δοχείου που κρατάει νερό
# Η απόσταση μεταξύ των άκρων είναι η διαφορά των indexes αυτών
# Βρές τα 2 άκρα που κρατάνε το περισσότερο νερό σε συνδυασμό με τον άξωνα των χ και επέστρεψε πόσο νερό μπορεί
# να αποθηκευτεί στο κουβά
# Απλή λύση
def maxAreaSimple(height: list[int]) -> int:
    max_water = 0
    for i in range(len(height)):
        for j in range(i, len(height)):
            if (j - i) * min(height[i], height[j]) > max_water:
                max_water = (j - i) * min(height[i], height[j])
    return max_water


# είναι O(n^2)
# Μπορώ και καλύτερα
# Αναδρομή με 2 δείκτες
# Άπληστη λογική, κάθε φορά κρατάω το δείκτη με το μεγαλύτερο ύψος και ξαναδοκιμάζω

def maxArea(height: list[int]) -> int:
    return maxAreaRec(0, len(height) - 1, 0, height)


def maxAreaRec(i, j, max_water, height):
    if i >= j:
        return max_water
    if (j - i) * min(height[i], height[j]) > max_water:
        max_water = (j - i) * min(height[i], height[j])
        return max_water
    if height[i] > height[j]:
        return maxAreaRec(i, j - 1, max_water, height)
    else:
        return maxAreaRec(i + 1, j, max_water, height)


# Χρονική πολυπλοκότητα O(n)
# Τελικά με χρήση επανάληψης
def maxAreaFinal(height: list[int]) -> int:
    i, j = 0, len(height) - 1
    max_water = 0

    while i < j:
        if (j - i) * min(height[i], height[j]) > max_water:
            max_water = (j - i) * min(height[i], height[j])
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_water

# Ίδια χρονική πολυπλοκότητα αλλά τελικά καλύτερη χωρική εξαιτίας της απουσίας στοίβας αναδρομής
# (Προσωπικά μ αρέσει καλύτερα η αναδρομή αλλά δεν έχω άποψη)
