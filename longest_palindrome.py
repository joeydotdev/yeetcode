class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_length(i: int, j: int) -> int:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            return s[i+1:j]

        if s is None or len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        
        best_str = ""
        for i in range(len(s)):
            first = get_length(i, i)
            second = get_length(i, i+1)
            if len(first) > len(best_str):
                best_str = first
            if len(second) > len(best_str):
                best_str = second

        return best_str