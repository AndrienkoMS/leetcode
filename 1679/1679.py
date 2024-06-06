import unittest

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        result = 0

        for num in nums:
            if count[k - num] > 0:
                result += 1
                count[k - num] -= 1
            else:
                count[num] += 1

        return result


class TestSolution(unittest.TestCase):
    def test_maxOperations(self):
        solution = Solution()
        test_cases = [
            ([1,2,3,4], 5, 2),
            ([3,1,3,4,3], 6, 1)
        ]
        for input, k, expected in test_cases:
            with self.subTest(input=input, k=k, expected=expected):
                self.assertEqual(solution.maxOperations(input, k), expected)

if __name__ == '__main__':
    unittest.main()