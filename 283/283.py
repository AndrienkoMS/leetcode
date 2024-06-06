import unittest

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_q_ty = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                zero_q_ty += 1

        # Додаємо нулі в кінець списку
        nums.extend([0] * zero_q_ty)
        return nums

class TestSolution(unittest.TestCase):
    def test_moveZeroes(self):
        solution = Solution()
        test_cases =[
            ([0,1,0,3,12], [1,3,12,0,0]),
            ([0],[0])
        ]
        for input, expected in test_cases:
            with self.subTest(s=input, expected=expected):
                self.assertEqual(solution.moveZeroes(input), expected)

if __name__ == '__main__':
    unittest.main()