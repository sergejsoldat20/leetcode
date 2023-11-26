class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.searchPrefix(word)
        return node != None and node.is_end_of_word

    def searchPrefix(self, prefix: str):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node != None


trie = Trie()

words = ["alo", "aleksa", "magarac", "majmun", "magarac", "magarac"]
for word in words:
    trie.insert(word)

user_input = "ma"
suggestions = trie.search(user_input)
print(suggestions)


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_word = True

#     def search(self, prefix):
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return []
#             node = node.children[char]
#         return self._collect_suggestions(node, prefix)

#     def _collect_suggestions(self, node: TrieNode, prefix: str):
#         suggestions = []
#         if node.is_end_of_word:
#             suggestions.append(prefix)
#         for char, child_node in node.children.items():
#             suggestions.extend(self._collect_suggestions(
#                 child_node, prefix + char))
#         return suggestions
