class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        mod_map = {0: 1}  # Initial prefix sum mod k = 0 appears once

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            # Handle negative mods
            if mod < 0:
                mod += k
            if mod in mod_map:
                count += mod_map[mod]
            mod_map[mod] = mod_map.get(mod, 0) + 1

        return count
