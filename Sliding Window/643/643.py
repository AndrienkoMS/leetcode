import unittest
class Solution(object):

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 1:
            return nums[0]/k

        start = 0
        end = k
        window_summ = sum(nums[start:end])
        biggest_summ = window_summ

        while end < len(nums):
            window_summ -= nums[start]
            window_summ += nums[end]
            biggest_summ = max(biggest_summ, window_summ)
            start += 1
            end += 1

        return float(biggest_summ)/k



    def findMaxAverage_1(self, nums, k):
        """
        First attempt 0 time limit exceeded
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window = nums[:k]
        result = sum(window)
        j = k
        while (j < len(nums)):
            result = sum(window) if sum(window)>result else result
            window.pop(0)
            window.append(nums[j])
            j += 1
        result = sum(window) if sum(window) > result else result
        return float(result)/k


class TestSolution(unittest.TestCase):

    def test_findMaxAverage(self):
        solution = Solution()
        test_cases = [
            ([1,12,-5,-6,50,3], 4, 12.75),
            ([5], 1, 5),
            ([-1], 1, -1),
            ([0,1,1,3,3], 4, 2)
        ]
        for nums, k, expected in test_cases:
            with self.subTest(nums = nums, k=k, expected = expected):
                self.assertEqual(solution.findMaxAverage(nums, k), expected)

if __name__ == '__main__':
    unittest.main()