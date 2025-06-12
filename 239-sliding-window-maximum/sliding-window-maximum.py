from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque()  # stores indexes

        for i in range(len(nums)):
            # Remove out-of-window indices
            if q and q[0] <= i - k:
                q.popleft()

            # Remove smaller values in k range as they are useless
            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)

            # Append current max to output (start from index k-1)
            if i >= k - 1:
                output.append(nums[q[0]])

        return output
