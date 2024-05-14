import unittest

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        can_be_planted = 0
        zeros_in_a_raw = 1
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                zeros_in_a_raw += 1
            elif (zeros_in_a_raw > 0):
                can_be_planted += (zeros_in_a_raw - 1) // 2
                zeros_in_a_raw = 0
        # last element
        zeros_in_a_raw +=1
        can_be_planted += (zeros_in_a_raw - 1) // 2
        return n<=can_be_planted


class TestSolution(unittest.TestCase):
    def test_canPlaceFlowers(self):
        solution = Solution()
        test_cases = [
            ([1,0,0,0,1], 1, True),  # Test case 1
            ([1,0,0,0,1], 2, False),  # Test case 2
            ([0,0,1,0,1], 1, True),  # Test case 3
            ([1,0,0,0,1,0,0], 2, True)
        ]
        for candies, extraCandies, expected in test_cases:
            with self.subTest(candies=candies, extraCandies=extraCandies, expected=expected):
                self.assertEqual(solution.canPlaceFlowers(candies, extraCandies), expected)

if __name__ == '__main__':
    unittest.main()