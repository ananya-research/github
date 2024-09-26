class Solution:
    def longestWord(self, words: List[str]) -> str:
       
    # Sort words first lexicographically and then by length
        words.sort()
    
    # Initialize a set to store valid prefixes
        valid_prefixes = set([""])
    
    # Initialize a variable to store the result
        longest = ""
    
    # Iterate through the sorted words
        for word in words:
        # Check if the prefix (all but the last character) is in the set
            if word[:-1] in valid_prefixes:
            # Add the current word to the valid set
                valid_prefixes.add(word)
            # Update longest if the current word is longer, or lexicographically smaller if same length
                if len(word) > len(longest):
                    longest = word
    
        return longest

            
            
        