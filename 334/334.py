import unittest

class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

class TestSolution(unittest.TestCase):
    def test_increasingTriplet(self):
        solution = Solution()
        test_cases = [
            ([1,2,3,4,5], True), # Test case 1
            ([5,4,3,2,1], False), # Test case 2
            ([2,1,5,0,4,6], True), # Test case 3
            ([20,100,10,12,5,13], True), # Test case 4
            ([1,5,0,4,1,3], True), # Test case 5
            ([3,2,4,-2,-3], False),
            ([1,2,2147483647], True),
            ([6, 7, 1, 2], False),
            ([1, 2, 1, 3], True),
            ([0, 4, 1, -1, 2], True)
        ]
        for input, expected in test_cases:
            with self.subTest(s=input, expected=expected):
                self.assertEqual(solution.increasingTriplet(input), expected)


if __name__ == '__main__':
    unittest.main()