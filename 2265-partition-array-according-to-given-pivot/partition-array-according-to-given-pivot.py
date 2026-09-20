class Solution(object):
    def pivotArray(self, nums, pivot):
        small=[]
        piv=[]
        great=[]
        for i in nums:
            if i< pivot:
                small.append(i)
            elif i==pivot:
                piv.append(i)
            else:
                great.append(i)
        return small+piv+great