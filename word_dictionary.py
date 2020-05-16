class Node:
    """
        isWord flag
        edges dict
    """
    def __init__(self):
        self.is_word = False
        self.edges = {}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root

        for c in word:
            if c not in cur_node.edges:
                cur_node.edges[c] = Node()
            cur_node = cur_node.edges[c]
        
        cur_node.is_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for idx, c in enumerate(word):
            if c == ".":
                for k in cur_node.edges:
                    if self.match(word, idx+1, cur_node[k]):
                        return True
                return False
            if c not in cur_node.edges:
                return False
            cur_node = cur_node.edges[c]
        
        return cur_node.is_word

        

    def backtrack(self, word: str, idx: int, cur_node: Node) -> bool:
        if idx >= len(word):
            return cur_node.is_word
        c = word[idx]            
        if c == ".":
            for k in cur_node.edges:
                if backtrack(word, idx+1, cur_node[k]):
                    return True
            return False
        else:
            if c not in cur_node.edges:
                return False
            for k in cur_node.edges:
                if backtrack(word, idx+1, cur_node[k]):
                    return True
            return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)