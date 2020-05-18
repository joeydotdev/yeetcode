"""
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, idx):
            if idx >= len(word):
                return True 

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]) or board[r][c] == "*":
                return False

            old_char = board[r][c]
            if old_char != word[idx]:
                return False
            board[r][c] = "*"
            found = dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or dfs(r, c-1, idx+1) or dfs(r, c+1, idx+1)
            board[r][c] = old_char
            return found
            

        for r in range(len(board)):
            for c in range(len(board[r])):
                if word[0] == board[r][c] and dfs(r, c, 0):
                    return True
        return False
                    
