"""
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]


[
    ["cats", "and", "dog"]
]

backtracking ?

word_break():
    result = []
    dfs()
    convert_to_sentence(result)
    return result

dfs(idx, dict, result, cur_iteration_result):
    iterate over word dict
        take current w word, make substr relative to idx
            compare if substr relative to x is equal to current w word
                append w word to list
                dfs(new_idx, dict, result, cur_iteration_result)
                remove w word from list
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}

        def dfs(cur_str):
            result = []
            if cur_str in memo:
                return memo[cur_str]

            if len(cur_str) == 0:
                result.append("")
                return result
            
            for w in wordDict:
                if (cur_str.startswith(w)):
                    substrings = dfs(cur_str[len(w):])

                    for s in substrings:
                        if len(s) == 0:
                            result.append(w)
                        else:
                            result.append(w + " " + s)

            memo[cur_str] = result
            return result

        return dfs(s)