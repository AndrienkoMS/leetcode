import unittest
from collections import Counter


class Solution(object):

    # Variant 1,
    # Runtime: 1664 ms, Beats: 9.27 %
    # Memory: 15.59 MB, Beats: 74.83 %
    # def equalPairs(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     equal_pairs_quantity = 0
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):
    #             equal_pairs_quantity += 1
    #             for k in range(len(grid[0])):
    #                 if grid[i][k] != grid[k][j]:
    #                     equal_pairs_quantity -= 1
    #                     break
    #     return equal_pairs_quantity

    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        # 1. Рахуємо хеші всіх РЯДКІВ.
        # Перетворюємо кожен рядок на tuple, щоб його можна було захешувати.
        # Counter автоматично підрахує, скільки разів трапляється кожен рядок.
        row_counts = Counter(tuple(row) for row in grid)

        equal_pairs_quantity = 0

        # 2. Ітеруємося по СТОВПЦЯХ
        for j in range(n):
            # Збираємо j-й стовпець у кортеж
            column = tuple(grid[i][j] for i in range(n))

            # Якщо хеш цього стовпця є в нашому словнику рядків,
            # додаємо кількість його появ до результату
            if column in row_counts:
                equal_pairs_quantity += row_counts[column]

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