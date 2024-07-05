# Δοθέντος ενός πίνακα reward με n rewards, επέστρεψε το μέγιστο reward (x) το οποίο μπορεί να επιτευχθεί αν
# κάθε φορά επιλέγεις ένα μη σημαδεμένο κόμβο και
# αν η αξία του είναι μεγαλύτερη από τη συνολική αξία που έχεις είδη συγκεντρώσει τότε μπορείς
# είτε να προσθέσεις την αξία του στο τελικό ποσό είτε όχι, αν το κάνεις σημαδεύεις το index
from typing import Dict, Tuple


# Αρχικά με αναδρομή
# Βασική περίπτωση: δεν έχω άλλα rewards, επιστρέφω το x
# Αλλιώς δοκιμάζω και τα 2
def maxTotalRewardRec(rewardValues: list[int], x: int, index: int) -> int:
    if index == len(rewardValues):
        return x

    not_take = maxTotalRewardRec(rewardValues, x, index + 1)
    if rewardValues[index] > x:
        take = maxTotalRewardRec(
            rewardValues, x + rewardValues[index], index + 1
        )
        return max(take, not_take)
    return not_take


# O(2^n) κάκιστο
# με δυναμικό
# ΠΡΟΣΟΧΉ!!! Memoization dictionary γιατί κάθε σύνολο index,x αποτελεί διαφορετική περίπτωση
# τελικά πάλι εκθετικός χρόνος... σκατά
def maxTotalReward(rewardValues: list[int]) -> int:
    n = len(rewardValues)
    dp = {}  # Κλειδί: συνδυασμός (tuple στη γλώσσα της python) index και x
    return maxTotalRewardDynamic(rewardValues, 0, 0, dp)


def maxTotalRewardDynamic(rewardValues: list[int], x: int, index: int,
                          dp: Dict[Tuple[int, int], int], ) -> int:
    if index == len(rewardValues):
        return x

    if (index, x) in dp:
        return dp[(index, x)]

    not_take = maxTotalRewardDynamic(rewardValues, x, index + 1, dp)

    take = 0
    if rewardValues[index] > x:
        take = maxTotalRewardDynamic(
            rewardValues, x + rewardValues[index], index + 1, dp
        )

    dp[(index, x)] = max(take, not_take)

    return dp[(index, x)]

