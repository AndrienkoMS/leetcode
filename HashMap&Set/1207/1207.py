import unittest


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        unique_occurences = set()
        unique_numbers=0
        while len(arr) > 0:
            unique_numbers += 1
            count = 0
            element = arr[0]
            while element in arr:
                arr.remove(element)
                count += 1
            unique_occurences.add(count)
            if unique_numbers != len(unique_occurences):
                return False
        return True

class test_solution(unittest.TestCase):
    def test_uniqueOccurances(self):
        solution = Solution()
        test_cases = [
            ([1,2,2,1,1,3], True),
            ([1,2], False),
            ([-3,0,1,-3,1,1,1,-3,10,0], True)
        ]
        for arr, expected in test_cases:
            with self.subTest(arr=arr, expected=expected):
                self.assertEqual(solution.uniqueOccurrences(arr=arr), expected)

if __name__ == '__main__':
    unittest.main()