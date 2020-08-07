# Andre Doumad
'''
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''
import unittest
class Solution(object):
    def solve(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = []
        current_level = 0
        res = 0
        for name in input.split('\n'):
            #print stack, current_level
            tabs = name.split('\t')
            if len(tabs) - 1 == current_level:
                if stack:
                    stack.pop()
                stack.append(tabs[-1])
            elif len(tabs) -1 > current_level:
                stack.append(tabs[-1])
            else:
                for _ in range(current_level - len(tabs) + 2):
                    if stack: stack.pop()
                stack.append(tabs[-1])
            if '.' in tabs[-1]:
                res = max(res, len('/'.join(stack)))
            current_level = len(tabs) - 1
        return res


class unitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()
        print('''dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext''')
        result = solution.solve('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext')
        print('RESULT: ' + str(result))

if __name__ == '__main__':
    unittest.main()