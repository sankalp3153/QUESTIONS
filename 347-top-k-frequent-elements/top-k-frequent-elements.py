class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]  # Bucket for frequencies
        
        # Count the frequency of each number
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # Place numbers into the freq array based on their frequencies
        for n, c in count.items():
            freq[c].append(n)
        
        # Collect the top K frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
