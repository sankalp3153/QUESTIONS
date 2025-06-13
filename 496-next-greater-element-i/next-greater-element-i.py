class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # Build the next greater map for elements in nums2
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # Remaining elements in stack have no next greater
        for num in stack:
            next_greater[num] = -1

        # Build the result for nums1 using the map
        return [next_greater[num] for num in nums1]
