class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        greatest = max(candies)
        for i in range(len(candies)):
            result.append(True if (candies[i]+extraCandies >= greatest) else False)
            # result.append(candies[i] + extraCandies >= greatest) # no need to add extra if
        return result

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2,3,5,1,3], 3),  # Test case 1
        ([4,2,1,1,2], 1),  # Test case 2
        ([12,1,12], 10)  # Test case 3
        # ('BABABA', 'ABAB') # Test case 4
    ]

    # Perform tests
    for i, (candies, extraCandies) in enumerate(test_cases, start=1):
        result = solution.kidsWithCandies(candies, extraCandies)
        print(f"Test case {i}: {candies} + {extraCandies} = {result}")
