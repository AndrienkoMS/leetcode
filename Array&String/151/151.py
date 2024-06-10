import unittest

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        word_start = -1
        for i in range(len(s)):
            if s[i] == ' ':
                if word_start != -1:
                    words.append(s[word_start:i])
                    word_start = -1
            else:
                if word_start == -1:
                    word_start = i

        if word_start != -1:
            words.append(s[word_start:])

        return ' '.join(reversed(words))

class TestSolution(unittest.TestCase):
    def test_reverseWords(self):
        solution = Solution()
        test_cases = [
            ("the sky is blue", "blue is sky the"),  # Test case 1
            ("  hello world  ", "world hello"),  # Test case 2
            ("a good   example", "example good a"),  # Test case 3
        ]
        for input, expected in test_cases:
            with self.subTest(s=input, expected=expected):
                self.assertEqual(solution.reverseWords(input), expected)

if __name__ == '__main__':
    unittest.main()
