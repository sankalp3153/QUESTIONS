class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        
        duplicate = actual_sum - unique_sum
        missing = total_sum - unique_sum

        return [duplicate, missing]
