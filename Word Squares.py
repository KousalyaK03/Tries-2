
# Approach:
# 1. Use a Trie (prefix-based lookup) to optimize searching for words with specific prefixes.
# 2. Use backtracking to build valid word squares.
# 3. Each row in the square corresponds to a prefix for the next word.
# 4. If the current word square's length equals the word length, add it to the result.

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # Step 1: Build a prefix dictionary for fast lookup
        def build_prefix_map(words):
            prefix_map = defaultdict(list)
            for word in words:
                for i in range(len(word)):
                    prefix_map[word[:i]].append(word)
            return prefix_map

        # Step 2: Backtracking function to form valid word squares
        def backtrack(step, word_square):
            if step == word_length:
                result.append(word_square[:])  # Found a valid word square
                return

            # Form the prefix for the next word to be added
            prefix = ''.join([word[step] for word in word_square])

            # Check if there are words with the required prefix
            if prefix not in prefix_map:
                return
            
            # Try adding each word with the matching prefix
            for candidate in prefix_map[prefix]:
                backtrack(step + 1, word_square + [candidate])

        # Step 3: Initialize data structures and start the search
        word_length = len(words[0])  # All words are of the same length
        prefix_map = build_prefix_map(words)
        result = []

        for word in words:
            backtrack(1, [word])  # Start forming the word square with each word

        return result

# Time Complexity: O(N * 4^L), where N is the number of words, and L is the word length.
# - The worst-case scenario involves trying all words in every position in a square.

# Space Complexity: O(N * L), as we store prefixes in a dictionary and use recursion.
