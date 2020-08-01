# Andre Doumad

'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

# Andre Doumad

class Node(): 
    def __init__(self):
        self.children = {} 
        self.last = False

class Trie(): 
    def __init__(self): 
        self.root = Node() 
        self.words = []

    def makeTrie(self, keys): 
        for key in keys: 
            self.insert(key) 

    def insert(self, key): 
        node = self.root
        for a in list(key):
            if not node.children.get(a): 
                node.children[a] = Node() 
            node = node.children[a]
        node.last = True

    def search(self, key): 
        node = self.root 
        found = True

        for a in list(key): 
            if not node.children.get(a): 
                found = False
                break
            node = node.children[a]
        return node and node.last and found 

    def recursiveWordSolver(self, node, word):
        if node.last: 
            self.words.append(word) 
        for a,n in node.children.items(): 
            self.recursiveWordSolver(n, word + a) 

    def search(self, key, dictionary): 
        self.makeTrie(dictionary)
        node = self.root 
        not_found = False
        temp_word = '' 
        for a in list(key): 
            if not node.children.get(a): 
                not_found = True
                break
            temp_word += a 
            node = node.children[a] 
        if not_found: 
            return 0
        elif node.last and not node.children: 
            return -1
        self.recursiveWordSolver(node, temp_word) 
        return self.words

def solution(key, keys):
    t = Trie()
    result = t.search(key, keys) 
    return result

print(solution('de', ['dog', 'deer', 'deal']))

'''
OUTPUT:
['deer', 'deal']
'''