import unittest

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea=0
        left = 0
        right = len(height)-1
        while left<right:
            area = min(height[left], height[right]) * (right-left)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
            maxArea = area if area > maxArea else maxArea
        return maxArea


class TestSolution(unittest.TestCase):

    def test_maxArea(self):
        solution = Solution()
        test_cases = [
            ([1,8,6,2,5,4,8,3,7], 49),
            ([1,1], 1)
        ]
        for height, expected in test_cases:
            with self.subTest(height=height, expected=expected):
                self.assertEqual(solution.maxArea(height), expected)

if __name__ == '__main__':
    unittest.main()