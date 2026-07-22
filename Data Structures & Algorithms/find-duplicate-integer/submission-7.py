class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for x in nums:
            x=abs(x)
            if nums[x-1]>0:
                nums[x-1]=-abs(nums[x-1])
            else:
                return x
        return abs(x)