import unittest


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        j = 0
        for i in range(len(t)):
            if s[j] == t[i]:
                if j == len(s)-1:
                    return True
                else:
                    j+=1
        return False

class TestSolution(unittest.TestCase):

    def test_isSubsequence(self):
        solution = Solution()
        test_cases = [
            ("abc", "ahbgdc", True),
            ("axc", "ahbgdc", False),
            ("", "ahbgdc", True)
        ]
        for s, t, expected in test_cases:
            with self.subTest(s=s, t=t, expected=expected):
                self.assertEqual(solution.isSubsequence(s, t), expected)

if __name__ == '__main__':
    unittest.main()