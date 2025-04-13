import unittest

class Solution(object):

    def count_unique_letters_in_word(self, word) -> list:
        """
        Returns a list of sorted values of unique letters appearence in word
        :param word:
        :return:
        """
        result = dict()
        for l in word:
            if l in result.keys():
                result[l] += 1
            else:
                result[l] = 1
        return list(sorted(result.values()))
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if (set(word1) == set(word2)) and (
                self.count_unique_letters_in_word(word1) == self.count_unique_letters_in_word(word2)):
                return True
        return False

class test_solution(unittest.TestCase):
    def test_closeStrings(self):
        solution = Solution()
        test_cases = [
            ("abc", "bca", True),
            ("a","aa", False),
            ("cabbba", "abbccc", True)
        ]
        for word1, word2, expected in test_cases:
            with self.subTest(word1=word1, word2=word2, expected=expected):
                self.assertEqual(solution.closeStrings(word1=word1, word2=word2), expected)


if __name__ == '__main__':
    unittest.main()