class Solution(object):
    def sum(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        return num1+num2

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (1, 2),  # Test case 1
        (0, 0),  # Test case 2
        (-1, 1),  # Test case 3
        (10, -5)  # Test case 4
    ]

    # Perform tests
    for i, (num1, num2) in enumerate(test_cases, start=1):
        result = solution.sum(num1, num2)
        print(f"Test case {i}: {num1} + {num2} = {result}")