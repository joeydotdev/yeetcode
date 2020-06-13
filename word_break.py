"""
    "leet"



    "leet"
    "le"

    dp[len(s) + 1] 


    dp[0] = True

    for i in range(len(dp)):
        if dp[i] == False:
            continue
        for w in word 


[True, False, False, False, False]
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(dp)):
            if not dp[i]:
                continue
            for w in wordDict:
                new_substr_idx = len(w) + i
                if len(s) < new_substr_idx:
                    continue
                cur_substr = s[i:new_substr_idx]
                if cur_substr == w:
                    dp[new_substr_idx] = True
                
            
        return dp[len(s)]