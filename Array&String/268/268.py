import unittest


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        full_summ, actual_sum = 0, 0
        for i in range(len(nums)):
            full_summ += i+1
            actual_sum += nums[i]
        return full_summ-actual_sum


class TestSolution(unittest.TestCase):
    def test_missingNumber(self):
        solution = Solution()
        test_cases = [
            ([3, 0, 1], 2),
            ([0,1], 2),
            ([9,6,4,2,3,5,7,0,1], 8)
        ]
        for input, expected in test_cases:
            with self.subTest(s=input, expected=expected):
                self.assertEqual(solution.missingNumber(input), expected)

if __name__ == '__main__':
    unittest.main()
