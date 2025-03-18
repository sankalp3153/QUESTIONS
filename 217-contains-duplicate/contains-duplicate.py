class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create a set to store numbers we've encountered
        for num in nums:
            if num in seen:  # If the number is already in the set, it's a duplicate
                return True
            seen.add(num)  # Add the number to the set
        return False  # No duplicates found
