"""
    if lookup table contains any element > 1, shrink window until all elements in table <= 1

    if all elements in lookup <= 1, we can expand and update the local/global running max
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        left = 0
        right = 0
        global_max = 0
        lookup = [0] * 256

        while right < len(s):
            if lookup[ord(s[right])] == 1:
                lookup[ord(s[left])] -= 1
                left += 1
            else:
                lookup[ord(s[right])] += 1
                right += 1
                global_max = max(global_max, right - left)

        return global_max
        
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if s is None or len(s) == 0:
    #         return 0
    #     if len(s) == 1:
    #         return 1
        
    #     left = 0
    #     right = 0
    #     lookup = [0] * 256
    #     global_max = 0
    #     local_max = 0
    #     lookup[ord(s[0])] += 1

    #     while right < len(s) - 1:
    #         if all(x <= 1 for x in lookup):
    #             # lookup only contains unique elements. update maxs
    #             local_max += 1
    #             global_max = max(local_max, global_max)
    #             right += 1
    #             lookup[ord(s[right])] += 1
    #         else:
    #             # lookup contains duplicate, we should lower our current window
    #             # no point in trying to update global max since we are shrinking.
    #             while any(x > 1 for x in lookup):
    #                 lookup[ord(s[left])] -= 1
    #                 left += 1
    #                 local_max -= 1

    #     # edge case, if last char in string sets a new global max.        
    #     if all(x <= 1 for x in lookup):
    #         local_max += 1
    #         global_max = max(local_max, global_max)
        
    #     return global_max