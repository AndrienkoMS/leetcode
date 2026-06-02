import unittest


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        equal_pairs_quantity = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                equal_pairs_quantity += 1
                for k in range(len(grid[0])):
                    if grid[i][k] != grid[k][j]:
                        equal_pairs_quantity -= 1
                        break
        return equal_pairs_quantity

class test_Solution(unittest.TestCase):
    def test_equalPairs(self):
        solution = Solution()
        test_case = [
            ([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 3),
            ([[3, 2, 1], [1, 7, 6], [2, 7, 7]], 1)
        ]
        for grid, expected in test_case:
            with self.subTest(grid=grid, expected=expected):
                self.assertEqual(solution.equalPairs(grid=grid), expected)

if __name__ == '__main__':
    unittest.main()