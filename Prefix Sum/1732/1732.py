import unittest

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        largest, current_attitude = 0, 0
        for i in range(len(gain)):
            current_attitude += gain[i]
            largest = max(largest, current_attitude)

        return largest

class test_solution(unittest.TestCase):
    def test_largestAltitude(self):
        solution = Solution()
        test_cases = [
            ([-5,1,5,0,-7], 1),
            ([-4, -3, -2, -1, 4, 3, 2], 0)
        ]
        for s, expected in test_cases:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(solution.largestAltitude(gain=s), expected)


if __name__ == '__main__':
    unittest.main()