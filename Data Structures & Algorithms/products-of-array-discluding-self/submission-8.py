class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums==[]:
            return nums
        
        pr=[nums[0]]
        po=[nums[-1]]

        i=1
        while i<len(nums):
            pr.append(pr[i-1]*nums[i])
            i+=1

        i=1
        nums.reverse()
        while i<len(nums):
            po.append(po[i-1]*nums[i])
            i+=1
        po.reverse()

        l=[po[1]]
        i=1
        while i<len(nums)-1:
            l.append(pr[i-1]*po[i+1])
            i+=1
        l.append(pr[-2])
        return l