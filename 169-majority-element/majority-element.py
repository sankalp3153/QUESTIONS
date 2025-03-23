class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count_map ={}
        for i in nums:
            if i in count_map:
                count_map[i]+=1
            else:
                count_map[i] = 1
        n = len(nums)
        for key,value in count_map.items():
            if value > n//2:
                return key
        
        