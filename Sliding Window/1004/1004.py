import unittest

class Solution(object):
    def longestOnes(self, nums, k):
        ans = flipped = start = stop = 0
        while stop < len(nums):
            if nums[stop] == 1:
                stop += 1
            elif nums[stop] == 0 and flipped < k:
                stop += 1
                flipped += 1
            else:
                if nums[start] == 0:
                    flipped -= 1
                start += 1
            ans = max(ans, stop - start)
        return ans

class TestSolution(unittest.TestCase):

    def test_longestOnes(self):
        solution = Solution()
        test_cases = [
            ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
            ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10)
        ]
        for nums, k, expected in test_cases:
            with self.subTest(nums=nums, k=k, expected=expected):
                self.assertEqual(solution.longestOnes(nums, k), expected)

if __name__ == '__main__':
    unittest.main()