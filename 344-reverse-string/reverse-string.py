class Solution:
    
    def reverseString(self, s: List[str]) -> None:
        
        e=0
        f = len(s)-1
        while e<f:
            s[e],s[f]=s[f],s[e]
            e+=1
            f-=1
