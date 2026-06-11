class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        dp = [0] * n  # words that fit starting from word i

        for i in range(n):
            col = 0
            words = 0
            idx = i
            while col + len(sentence[idx % n]) <= cols:
                col += len(sentence[idx % n]) + 1
                words += 1
                idx += 1
            dp[i] = words

        total_words = 0
        start = 0
        for i in range(rows):
            total_words += dp[start]
            start = (start + dp[start]) % n

        return total_words // n
