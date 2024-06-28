# Να γραφτεί ένας αλγόριθμος που να επιστρέφει τους διαφορετικούς τρόπους με τους οποίους μπορούμε να ανεβούμε
# μια σκάλα παίρνοντας ή 1 ή 2 βήματα (σκαλοπάτια) τη φορά
# Ya know the drill by now
# Είναι copy and pasted από leetcode hence the class layout, ignore it
class Solution:
    def __init__(self):
        self.dp = None

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.dp = [-1] * (n + 1)
        return self.climbStairsDynamic(n)

    def climbStairsRec(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairsRec(n - 1) + self.climbStairsRec(n - 2)

    def climbStairsDynamic(self, n: int) -> int:
        if self.dp[n] != -1:
            return self.dp[n]
        if n == 0:
            return 0
        if n == 1:
            self.dp[n] = 1
            return 1
        if n == 2:
            self.dp[n] = 2
            return 2
        self.dp[n] = self.climbStairsDynamic(n - 1) + self.climbStairsDynamic(n - 2)
        return self.dp[n]
