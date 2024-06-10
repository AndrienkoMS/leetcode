import unittest

class Solution(object):

    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        n = len(chars)
        while i < n-1:
            if chars[i][0] == chars[i+1]:
                chars[i] += chars[i+1]
                chars.pop(i+1)
                n -= 1
            else:
                i += 1
        i=0
        # n=len(chars)
        while i < n:
            if len(chars[i]) > 1:
                l = str(len(chars[i]))
                while len(l) > 0:
                    chars.insert(i+1, l[-1])
                    n += 1
                    l = l[:-1]
                chars[i] = chars[i][0]
            i += 1
        return n


class TestSolution(unittest.TestCase):
    def test_compress(self):
        solution = Solution()
        test_cases = [
            (["a","a","b","b","c","c","c"], ["a","2","b","2","c","3"]),
            (["a"], ["a"]),
            (["a","b","b","b","b","b","b","b","b","b","b","b","b"], ["a","b","1","2"])

        ]
        for input, expected in test_cases:
            with self.subTest(s=input, expected=expected):
                self.assertEqual(solution.compress(input), expected)


if __name__ == '__main__':
    unittest.main()