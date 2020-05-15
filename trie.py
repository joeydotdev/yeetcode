class Node:
    """
        isWord flag
        edges dict
    """
    def __init__(self):
        self.is_word = False
        self.edges = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
    def insert(self, word: str) -> None:
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
        for c in word:
            if c not in cur_node.edges:
                return False
            cur_node = cur_node.edges[c]
        
        return cur_node.is_word

        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for c in prefix:
            if c not in cur_node.edges:
                return False
            cur_node = cur_node.edges[c]
        
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)