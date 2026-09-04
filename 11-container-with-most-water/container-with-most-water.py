class Solution(object):
    def maxArea(self, height):
       
        l,r=0,len(height)-1
        res=0

        while l < r:
            curr= min(height[l],height[r])*(r-l)
            res = max(curr,res)
            if height[l]<height[r]:
                l+=1
            
            else:
                r-=1
        return res
    
