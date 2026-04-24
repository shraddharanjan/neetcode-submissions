class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > 26:
            return 0
        answer = 0
        n = len(s)

        left = right = 0
        freq = [0] * 26

        def get_val(ch: str) -> int:
            return ord(ch) - ord("a")

        while right < n:
            freq[get_val(s[right])] += 1
            while freq[get_val(s[right])] > 1:
                freq[get_val(s[left])] -= 1
                left += 1
            if right - left + 1 == k:
                answer += 1
                freq[get_val(s[left])] -= 1
                left += 1
            right += 1

        return answer