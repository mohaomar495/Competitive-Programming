class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x, y = 1, 0
        if n <= 0:
            return False
        while x <= n:
            if x == n:
                return True
            y += 1
            x = 3 ** y
        return False
