class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l=min(len(word1),len(word2))
        result=''

        for i in range(l):
            result += word1[i] + word2[i]

        result += word1[l:] if len(word1) > len(word2) else word2[l:]

        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abc", "pqr"),  # Test case 1
        ('ab', 'pqrs'),  # Test case 2
        ('abcd', 'pq')  # Test case 3
    ]

    # Perform tests
    for i, (word1, word2) in enumerate(test_cases, start=1):
        result = solution.mergeAlternately(word1, word2)
        print(f"Test case {i}: {word1} + {word2} = {result}")

