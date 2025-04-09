import unittest

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == right_sum - nums[i]:
                return i
            else:
                left_sum += nums[i]
                right_sum -= nums[i]
        return -1
class test_solution(unittest.TestCase):
    def test_pivotIndex(self):
        solution = Solution()
        test_cases = [
            ([1,7,3,6,5,6], 3),
            ([1,2,3],-1),
            ([2,1,-1],0)
        ]
        for s, expected in test_cases:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(solution.pivotIndex(nums=s), expected)

if __name__ == '__main__':
    unittest.main()