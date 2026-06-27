class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_indices = {}
        # Get the index for each key.
        for i in range(len(keyboard)):
            key_indices[keyboard[i]] = i
            
        # Initialize previous index as starting index = 0.
        prev = 0
        result = 0
        
        # Calculate the total time.
        for c in word:
            # Add the distance from previous index
            # to current letter's index to the result.
            result += abs(prev - key_indices[c])
            
            # Update the previous index to current index for next iteration.
            prev = key_indices[c]
            
        return result