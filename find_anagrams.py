"""
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


substr is expensive so idk.
O(n*(k+klogk))

sliding window ?
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if s is None:
            return result

        lookup = [0] * 26
        n = len(s)
        k = len(p)
        left = 0
        right = 0

        for c in p:
            lookup[ord(c) - ord('a')] += 1

        while right < k:
            # setup window
            lookup[ord(s[right]) - ord('a')] -= 1
            right += 1 

        while right < n:
            if all(x == 0 for x in lookup):
                result.append(left)
            
            lookup[ord(s[left]) - ord('a')] += 1
            left += 1
            
                        
            lookup[ord(s[right]) - ord('a')] -= 1
            right += 1
        
        return result