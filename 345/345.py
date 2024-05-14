import unittest


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_position = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowels_position.append(i)

        # Convert the string to a list of characters
        chars = list(s)

        # Iterate through half of the vowels_position list
        for i in range(len(vowels_position) // 2):
            # Get the current and opposite positions
            pos1 = vowels_position[i]
            pos2 = vowels_position[-i - 1]

            # Swap the characters at the positions
            chars[pos1], chars[pos2] = chars[pos2], chars[pos1]

        # Join the characters back into a string
        return ''.join(chars)

# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         n = len(s)
#         i, j = 0, n - 1
#         vowels = 'AEIOUaeiou'
#         sList = list(s)
#         while i < j:
#             leftLetter = sList[i]
#             rightLetter = sList[j]
#             if leftLetter in vowels and rightLetter in vowels:
#                 # swap
#                 temp = leftLetter
#                 sList[i] = rightLetter
#                 sList[j] = temp
#                 i += 1
#                 j -= 1
#             else:
#                 # either left letter is not vowel or right is not vowel
#                 if leftLetter not in vowels:
#                     i += 1
#                 if rightLetter not in vowels:
#                     j -= 1
#         return "".join(sList)


class TestSolution(unittest.TestCase):
    def test_reverseVowels(self):
        solution = Solution()
        test_cases = [
            # ("hello", "holle"), # Test case 1,
            # ("leetcode", "leotcede"), # Test case 2,
            ("aA", "Aa") # Test case 3
        ]
        for input, expected in test_cases:
            with self.subTest(s=input, expected=expected):
                self.assertEqual(solution.reverseVowels(input), expected)

if __name__ == '__main__':
    unittest.main()