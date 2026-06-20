class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        for j in range(len(nums)):
            if nums==[]:
                return nums
            else:
                x=1
            i=0
            while i<len(nums):
                if i!=j:
                    x*=nums[i]
                i+=1
            l.append(x)
            i=0
        return l