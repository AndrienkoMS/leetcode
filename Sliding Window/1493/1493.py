import unittest
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest=0
        prev_l=0    # previous len of subarray
        cur_l=0     # current len of subarray
        deleted=1
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_l+=1
            else:
                deleted=0
                longest = max((prev_l + cur_l), longest)
                prev_l = cur_l
                cur_l = 0

        return max((prev_l + cur_l), longest) - deleted



class Test_Solution(unittest.TestCase):

    def test_longestSubarray(self):
        solution = Solution()
        test_cases = [
            ([1,1,0,1], 3),
            ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
            ([1,1,1], 2)
        ]
        for s, expected in test_cases:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(solution.longestSubarray(nums=s), expected)

if __name__ == '__main__':
    unittest.main()