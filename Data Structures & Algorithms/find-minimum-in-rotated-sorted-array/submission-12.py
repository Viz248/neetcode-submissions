class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l]<nums[r]:
                return nums[0]
                
            m=(l+r)//2

            if nums[m]>nums[l]:
                l=m
            elif nums[m]<nums[l]:
                r=m
            else:
                if 1<=m+1<=len(nums)-1:
                    return nums[m+1]
                return nums[m]
