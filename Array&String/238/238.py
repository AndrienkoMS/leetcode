import unittest


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_multiplication = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                total_multiplication *= num
            else:
                zero_count += 1

        result = []

        if zero_count > 1:
            return [0] * len(nums)

        for num in nums:
            if num != 0:
                if zero_count == 1:
                    result.append(0)
                else:
                    result.append(total_multiplication // num)
            else:
                result.append(total_multiplication)

        return result
class TestSolution(unittest.TestCase):
    def test_productExceptSelf(self):
        solution = Solution()
        test_cases = [
            # ([1,2,3,4], [24,12,8,6]), # Test case 1
            # ([-1,1,0,-3,3], [0,0,9,0,0]), # Test case 2
            ([0,0], [0,0]) # Test case 3
        ]
        for input, expected  in test_cases:
            with self.subTest(s=input, expected=expected):
                self.assertEqual(solution.productExceptSelf(input), expected)

if __name__ == '__main__':
    unittest.main()