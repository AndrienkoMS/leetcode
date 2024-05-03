class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        factors1 = [i for i in range(1, len(str1) + 1) if len(str1) % i == 0]
        factors2 = [i for i in range(1, len(str2) + 1) if len(str2) % i == 0]

        common_factors = sorted(set(factors1) & set(factors2), reverse=True)

        for i in common_factors:
            if (str1.count(str1[:i]) == len(str1)/i) and (str2.count(str1[:i]) == len(str2)/i):
               return str1[:i] if str2.count(str1[:i]) > 0 else ''

        return ''



if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("ABCABC", "ABC"),  # Test case 1
        ('ABABAB', 'ABAB'),  # Test case 2
        ('LEET', 'CODE'),  # Test case 3
        ('BABABA', 'ABAB') # Test case 4
    ]

    # Perform tests
    for i, (word1, word2) in enumerate(test_cases, start=1):
        result = solution.gcdOfStrings(word1, word2)
        print(f"Test case {i}: {word1} + {word2} = {result}")

