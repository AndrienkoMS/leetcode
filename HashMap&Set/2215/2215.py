import unittest

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        exclusive1, exclusive2 = set(), set()  # only present in nums1 & only present in nums2
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                exclusive2.add(nums2[j])
                j += 1
            else:
                exclusive1.add(nums1[i])
                i += 1

        while j < len(nums2):
            exclusive2.add(nums2[j])
            j += 1

        while i < len(nums1):
            exclusive1.add(nums1[i])
            i += 1

        return [list(exclusive1), list(exclusive2)]


class test_solution(unittest.TestCase):
    def test_findDifference(self):
        solution = Solution()
        test_cases = [
            ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
            ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []])
        ]
        for nums1, nums2, expected in test_cases:
            with self.subTest(nums1=nums1, nums2=nums2, expected=expected):
                self.assertEqual(solution.findDifference(nums1=nums1, nums2=nums2), expected)

if __name__ == '__main__':
    unittest.main()
