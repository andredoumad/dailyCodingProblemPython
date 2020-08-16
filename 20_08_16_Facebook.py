# Andre Doumad

'''
This problem was asked by Facebook, Google, Amazon.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''
import unittest
class Solution:
    def isValid(self, s):
        brackMap= {'(':')','{':'}','[':']'}
        lefBracks = set(['(','{','['])
        stack = []
        for val in s:
            if val in lefBracks:
                stack.append(val)
            elif stack and val == brackMap[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []


class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        result = solution.isValid(r"()")
        print('result is ', result)
        self.assertEqual(result,True)

        result = solution.isValid(r"()[]{}")
        print('result is ', result)
        self.assertEqual(result,True)

        result = solution.isValid(r"(]")
        print('result is ', result)
        self.assertEqual(result,False)

        result = solution.isValid(r"([)]")
        print('result is ', result)
        self.assertEqual(result,False)

        result = solution.isValid(r"{[]}")
        print('result is ', result)
        self.assertEqual(result,True)

if __name__ == '__main__':
    unittest.main()

'''
result is  True
result is  True
result is  False
result is  False
result is  True
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''