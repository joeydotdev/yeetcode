class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 is None or s2 is None:
            return False
        if len(s1) > len(s2):
            return False
        
        k = len(s1)
        lookup = [0] * 26
        for c in s1:
            lookup[ord(c) - ord('a')] += 1

        cur_state = [0] * 26
        for idx, c in enumerate(s2):
            cur_state[ord(c) - ord('a')] += 1
            if idx >= k:
                cur_state[ord(s2[idx - k]) - ord('a')] -= 1
            
            if cur_state == lookup:
                return True

        return False
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     def scan(a, idx):
    #         if len(s1) + idx > len(s2):
    #             return False
    #         for i in range(idx, idx + len(s1)):
    #             c = s2[i]
    #             if a[ord(c) - ord('a')] == 0:
    #                 return False
    #             a[ord(c) - ord('a')] -= 1

    #         return all(x == 0 for x in a)

    #     lookup = [0] * 26
    #     for c in s1:
    #         lookup[ord(c) - ord('a')] += 1
        
    #     for idx, c in enumerate(s2):
    #         if lookup[ord(c) - ord('a')] > 0:
    #             if scan(lookup.copy(), idx):
    #                 return True

    #     return False




"""
afoo

foo


range(1, 4)
"""