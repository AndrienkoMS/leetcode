import unittest
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_vovels = 0
        for i in range(len(s[:k])):
            if s[i] in vowels:
                max_vovels+=1

        start = 0
        end = k
        window_vovels = max_vovels

        while end < len(s):
            if (max_vovels == k):
                return max_vovels

            window_vovels += 1 if s[end] in vowels else 0
            if k > 1:
                window_vovels -= 1 if s[start] in vowels else 0

            max_vovels = max(max_vovels, window_vovels)

            start += 1
            end += 1

        return max_vovels


class test_solution(unittest.TestCase):
    def test_maxVowels(self):
        solution = Solution()
        test_cases = [
            ("aabcdefg", 3, 2),
            # ("abciiidef", 3, 3),
            # ("aeiou", 2, 2),
            # ("leetcode", 3, 2),
            # ("tryhard", 4, 1),
            # ("novowels", 1, 1),
            ("tnfazcwrryitgacaabwm", 4, 3)
        ]

        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k, expected=expected):
                self.assertEqual(solution.maxVowels(s, k), expected)

if __name__ == '__main__':
    unittest.main()