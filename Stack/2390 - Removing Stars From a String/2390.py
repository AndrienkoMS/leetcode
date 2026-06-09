import unittest
from collections import deque

class Solution(object):

    # Runtime: 345 ms, Beats: 20.82 %
    # Memory: 14.88 MB, Beats: 17.99 %

    # in case "list" is used instead of "deque"
        # stask = list(s) => stack = deque(s)
    # Runtime: 414 ms, Beats: 13.88 %
    # Memory: 14.63 MB, Beats: 19.15 %
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = deque(s)
        result = []
        delete_counter = 0

        while stack:
            current = stack.pop()
            if current == "*":
                delete_counter += 1
                continue
            elif delete_counter > 0:
                delete_counter -= 1
                continue
            result.append(current)

        return "".join(reversed(result))

class Test_Solution(unittest.TestCase):
    def test_removeStars(self):
        solution = Solution()
        test_cases = [
            ("leet**cod*e", "lecoe"),
            ("erase*****", "")
        ]
        for s, expected in test_cases:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(solution.removeStars(s=s), expected)


if __name__ == '__main__':
    unittest.main()