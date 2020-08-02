# Andre Doumad
'''
This problem was asked by Amazon.

Given an integer k and a string s, 
find the length of the longest 
substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, 
the longest substring with k distinct characters is "bcb".
'''
import unittest
class Solution(object):
    def solve(self, k, s):
        qualifyingSubstrings = {}
        key = 0
        substringStartIndex = 0
        substring = ''
        sUniqueChars = ''
        sUniqueCount = 0
        i = 0
        longestSubstring = ''
        while i < len(s):
            print('----------')
            if sUniqueChars.find(str(s[i])) != -1:
                print('no unique character')
                pass
            else:
                print('found unique character')
                sUniqueChars += (str(s[i]))
                sUniqueCount += 1
                print('sUniqueCount ', sUniqueCount)

            if sUniqueCount > k:
                print('dumping queue to dictionary') 
                qualifyingSubstrings[key] = substring
                if len(longestSubstring) < len(substring):
                    longestSubstring = substring
                substring = ''
                sUniqueChars = ''
                sUniqueCount = 0
                key += 1
                substringStartIndex += 1
                i = substringStartIndex
            else:
                substring += s[i]
                i+=1
            print('substring ', substring)
        
        for k,v in qualifyingSubstrings.items():
            print('k: ' + str(k) + ' v: ' + str(v))
        if longestSubstring == '':
            longestSubstring = substring
        return longestSubstring

class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        print('The longest qualifying string is: ' + str(solution.solve(2, 'abcba')))

if __name__ == '__main__':
    unittest.main()