# Βρες το μικρότερο αριθμό operation πάνω σε μια λέξη word1 έτσι ώστε να τη μετατρέψουμε σε μια λέξη word2
# Επιτρεπτές πράξεις: Εισαγωγή χαρακτήρα, Διαγραφή χαρακτήρα, Αντικατάσταση χαρακτήρα
# Λύση με Αναδρομή γιατί είμαι ηλίθιος
# δύο δείκτες i για word1 και j για word2
# Βασική περίπτωση, αν κάποια λέξη είναι μεγαλύτερη, τότε η διαφορά τους θα πρέπει να προστεθεί στην απόσταση μεταξύ τους
# Σε αυτή τη περίπτωση απλά κάνω συνεχή εισαγωγή οπότε και τελειώνω την αναδρομή
# Αν οι 2 λέξεις έχουν τον ίδιο χαρακτήρα στα i,j τότε προχωράω αυξάνοντας και τα 2 αφού δεν χρειάζεται να κάνω κάτι
# για αυτό το χαρακτήρα
# Αν πάλι όχι τότε δοκιμάζω κάθε πιθανό σενάριο
# Κάθε φορά κρατάω το ελάχιστο της μιας εκ των τριών επιλογών
# Η θα αυξήσω τον ένα δείκτη, ή τον άλλον ή και τους 2
# Αν δεν είναι ίδια τα γράμματα στου δείκτες τότε θα προσθέσω και μια διαδικασία στο τελικό counter
# Με memoization έχω 2 indexes άρα n^2 πιθανές λύσεις άρα δισδιάστατο dp


class Solution:
    def __init__(self):
        self.word1 = None
        self.word2 = None
        self.dp = None

    def minDistance(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        self.dp = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        return self.minDistanceDynamic(0, 0)

    def minDistanceRecursive(self, word1, word2, i, j):
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if word1[i] == word2[j]:
            return self.minDistanceRecursive(word1, word2, i + 1, j + 1)
        else:
            choice_1 = 1 + self.minDistanceRecursive(word1, word2, i + 1, j)
            choice_2 = 1 + self.minDistanceRecursive(word1, word2, i, j + 1)
            choice_3 = 1 + self.minDistanceRecursive(word1, word2, i + 1, j + 1)
            return min(choice_1, choice_2, choice_3)

    def minDistanceDynamic(self, i, j):
        if i == len(self.word1):
            return len(self.word2) - j
        if j == len(self.word2):
            return len(self.word1) - i

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        if self.word1[i] == self.word2[j]:
            self.dp[i][j] = self.minDistanceDynamic(i + 1, j + 1)
        else:
            choice_1 = 1 + self.minDistanceDynamic(i, j + 1)
            choice_2 = 1 + self.minDistanceDynamic(i + 1, j)
            choice_3 = 1 + self.minDistanceDynamic(i + 1, j + 1)
            self.dp[i][j] = min(choice_1, choice_2, choice_3)

        return self.dp[i][j]
