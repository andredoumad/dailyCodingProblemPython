# Andre Doumad
'''
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. 
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and 
the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and 
the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or 
['bedbath', 'and', 'beyond'].
'''
class WordMap(object):
    def __init__(self, word):
        self.start_indexes = []
        self.end_indexes = []
        self.word = word


class Solution(object):
    def solve(self, s):
        string = ''
        words = []
        for k,v in s.items():
            string = k
            words = v
        wordmaps = []
        arrangement = {}

        for i in range(0,len(words)):
            if words[i] in arrangement:
                wmap = arrangement.get(words[i])
            else:
                wmap = arrangement[words[i]] = WordMap(words[i])
            subs = ''
            tempWord = ''
            print('searching for word: ', words[i])
            searchedThrough = ''
            for b in range(0, len(string)):
                print('-----')
                searchedThrough += string[b]
                print(searchedThrough)
                if string[b] in words[i]:
                    print('tempWord = ', tempWord)
                    tempWord += string[b]

                for c in range(0, len(tempWord)):
                    if c >= len(words[i]) or c>= len(tempWord) or tempWord[c] != words[i][c]:
                        print('tempWord canceled')
                        tempWord = string[b]

                if tempWord == words[i]:
                    print('tempWord == ', words[i])
                    starti = (b - (len(words[i])-1))
                    endi = (b)
                    if starti in wmap.start_indexes:
                        # cancel
                        print('start index already accounted for ')
                        tempwWord = string[b]
                    else:
                        wmap.start_indexes.append(starti) 
                        wmap.end_indexes.append(endi)
                        print('tempWord accepted')
                        break

        print(string)
        print(words)
        result = []
        wordSequence = {}
        sequence = []
        for k,v in arrangement.items():
            print(v.word, ' ', ' start ', v.start_indexes, ' end ', v.end_indexes)
            for start in v.start_indexes:
                if start not in wordSequence: 
                    wordSequence[start] = v.word
                    sequence.append(start)
        sequence = sorted(sequence)
        for key in sequence:
            result.append(wordSequence.get(key))

        return result




import unittest
class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        result = solution.solve({'thequickbrownfox': ['quick', 'brown', 'the', 'fox']})
        print('result ', result)
        result = solution.solve({'bedbathandbeyond': ['bed', 'bath', 'bedbath', 'and', 'beyond']})
        print('result ', result)

if __name__ == '__main__':
    unittest.main()

'''
OUTPUT:
searching for word:  quick
-----
t
-----
th
-----
the
-----
theq
tempWord =  
-----
thequ
tempWord =  q
-----
thequi
tempWord =  qu
-----
thequic
tempWord =  qui
-----
thequick
tempWord =  quic
tempWord ==  quick
tempWord accepted
searching for word:  brown
-----
t
-----
th
-----
the
-----
theq
-----
thequ
-----
thequi
-----
thequic
-----
thequick
-----
thequickb
tempWord =  
-----
thequickbr
tempWord =  b
-----
thequickbro
tempWord =  br
-----
thequickbrow
tempWord =  bro
-----
thequickbrown
tempWord =  brow
tempWord ==  brown
tempWord accepted
searching for word:  the
-----
t
tempWord =  
-----
th
tempWord =  t
-----
the
tempWord =  th
tempWord ==  the
tempWord accepted
searching for word:  fox
-----
t
-----
th
-----
the
-----
theq
-----
thequ
-----
thequi
-----
thequic
-----
thequick
-----
thequickb
-----
thequickbr
-----
thequickbro
tempWord =  
tempWord canceled
-----
thequickbrow
tempWord canceled
-----
thequickbrown
tempWord canceled
-----
thequickbrownf
tempWord =  n
tempWord canceled
tempWord canceled
-----
thequickbrownfo
tempWord =  f
-----
thequickbrownfox
tempWord =  fo
tempWord ==  fox
tempWord accepted
thequickbrownfox
['quick', 'brown', 'the', 'fox']
quick    start  [3]  end  [7]
brown    start  [8]  end  [12]
the    start  [0]  end  [2]
fox    start  [13]  end  [15]
result  ['the', 'quick', 'brown', 'fox']
searching for word:  bed
-----
b
tempWord =  
-----
be
tempWord =  b
-----
bed
tempWord =  be
tempWord ==  bed
tempWord accepted
searching for word:  bath
-----
b
tempWord =  
-----
be
-----
bed
-----
bedb
tempWord =  b
tempWord canceled
-----
bedba
tempWord =  b
-----
bedbat
tempWord =  ba
-----
bedbath
tempWord =  bat
tempWord ==  bath
tempWord accepted
searching for word:  bedbath
-----
b
tempWord =  
-----
be
tempWord =  b
-----
bed
tempWord =  be
-----
bedb
tempWord =  bed
-----
bedba
tempWord =  bedb
-----
bedbat
tempWord =  bedba
-----
bedbath
tempWord =  bedbat
tempWord ==  bedbath
tempWord accepted
searching for word:  and
-----
b
-----
be
-----
bed
tempWord =  
tempWord canceled
-----
bedb
tempWord canceled
-----
bedba
tempWord =  b
tempWord canceled
tempWord canceled
-----
bedbat
-----
bedbath
-----
bedbatha
tempWord =  a
tempWord canceled
-----
bedbathan
tempWord =  a
-----
bedbathand
tempWord =  an
tempWord ==  and
tempWord accepted
searching for word:  beyond
-----
b
tempWord =  
-----
be
tempWord =  b
-----
bed
tempWord =  be
tempWord canceled
-----
bedb
tempWord =  d
tempWord canceled
tempWord canceled
-----
bedba
-----
bedbat
-----
bedbath
-----
bedbatha
-----
bedbathan
tempWord =  b
tempWord canceled
-----
bedbathand
tempWord =  n
tempWord canceled
tempWord canceled
-----
bedbathandb
tempWord =  d
tempWord canceled
tempWord canceled
-----
bedbathandbe
tempWord =  b
-----
bedbathandbey
tempWord =  be
-----
bedbathandbeyo
tempWord =  bey
-----
bedbathandbeyon
tempWord =  beyo
-----
bedbathandbeyond
tempWord =  beyon
tempWord ==  beyond
tempWord accepted
bedbathandbeyond
['bed', 'bath', 'bedbath', 'and', 'beyond']
bed    start  [0]  end  [2]
bath    start  [3]  end  [6]
bedbath    start  [0]  end  [6]
and    start  [7]  end  [9]
beyond    start  [10]  end  [15]
result  ['bed', 'bath', 'and', 'beyond']
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
'''