class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        freqs = Counter(s)
        max_freq = max(freqs.values()) if freqs else 0

        # Store all the characters with the highest and second highest frequency
        most_chars = set()
        second_chars = set()

        for char, freq in freqs.items():
            if freq == max_freq:
                most_chars.add(char)
            elif freq == max_freq - 1:
                second_chars.add(char)

        # Create max_freq number of different strings
        segments = [[] for _ in range(max_freq)]

        # Insert one instance of characters with frequency max_freq & max_freq - 1 in each segment
        for i in range(max_freq):
            for c in most_chars:
                segments[i].append(c)

            # Skip the last segment as the frequency is only max_freq - 1
            if i < max_freq - 1:
                for c in second_chars:
                    segments[i].append(c)

        segment_id = 0

        # Iterate over the remaining characters and distribute instances over segments
        for char, freq in freqs.items():
            # Skip characters with max_freq or max_freq - 1 frequency
            if char in most_chars or char in second_chars:
                continue

            # Distribute the instances over segments in round-robin manner
            for _ in range(freq):
                segments[segment_id].append(char)
                segment_id = (segment_id + 1) % (max_freq - 1)

        # Each segment except the last should have exactly k elements
        for i in range(max_freq - 1):
            if len(segments[i]) < k:
                return ""

        # Join all segments and return
        return ''.join(''.join(segment) for segment in segments)