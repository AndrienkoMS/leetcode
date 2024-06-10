import unittest

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        greatest = max(candies)
        for i in range(len(candies)):
            result.append(True if (candies[i]+extraCandies >= greatest) else False)
        return result

class TestSolution(unittest.TestCase):
    def test_kidsWithCandies(self):
        solution = Solution()
        test_cases = [
            ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),  # Test case 1
            ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),  # Test case 2
            ([12, 1, 12], 10, [True, False, True])  # Test case 3
        ]
        for candies, extraCandies, expected in test_cases:
            with self.subTest(candies=candies, extraCandies=extraCandies, expected=expected):
                self.assertEqual(solution.kidsWithCandies(candies, extraCandies), expected)

if __name__ == '__main__':
    unittest.main()
