# Approach:
# 1. Use a helper function to check if a query string follows the CamelCase pattern.
# 2. The pattern must appear in the query in order, but lowercase letters can be inserted.
# 3. Any extra uppercase letters in the query that are not in the pattern will result in a mismatch.
# 4. Iterate through each query and check if it matches the pattern.

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # Helper function to check if a query matches the given pattern
        def is_match(query, pattern):
            i, j = 0, 0  # Two pointers: i for query, j for pattern
            
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:  
                    # If characters match, move both pointers
                    j += 1  
                elif query[i].isupper():  
                    # If an extra uppercase letter is found in query, it's invalid
                    return False
                # Move query pointer
                i += 1  
            
            # Ensure we have matched the entire pattern
            return j == len(pattern)

        # Apply the helper function to all queries
        return [is_match(query, pattern) for query in queries]

# Time Complexity: O(Q * P), where Q is the number of queries and P is the length of the longest query.
# - Each query is processed in O(P), resulting in O(Q * P) overall.

# Space Complexity: O(1), since we only use a few extra variables.