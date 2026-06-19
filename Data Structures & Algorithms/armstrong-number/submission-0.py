class Solution:
    def isArmstrong(self, n: int) -> bool:
        def getSumOfKthPowerOfDigits(num, k):
            result = 0

            while num != 0:
                result += (num % 10) ** k
                num //= 10

            return result

        length = 0
        temp_n = n

        while temp_n != 0:
            length += 1
            temp_n //= 10

        return getSumOfKthPowerOfDigits(n, length) == n