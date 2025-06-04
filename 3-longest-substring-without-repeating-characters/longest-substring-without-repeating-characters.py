class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        seen= set()
        max_len= 0
        for end in range(len(s)):
            char = s[end]
            while char in seen:
                seen.remove(s[start])
                start+=1
            seen.add(char)
            max_len=max(max_len,end-start+1)

        return max_len   