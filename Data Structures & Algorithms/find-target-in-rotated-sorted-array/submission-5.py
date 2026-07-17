class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            while l<=r and nums[l]<=nums[r]:
                m=(l+r)//2
                if nums[m]>target:
                    r=m-1
                elif nums[m]<target:
                    l=m+1
                elif nums[m]==target:
                    return m
            if l>r:
                return -1
            m=(l+r)//2
            if nums[m]>nums[l]:
                l=m
            elif nums[m]<nums[l]:
                r=m
            else:
                if nums[0]<=target<=nums[m]:
                    r=m
                    l=0
                else:
                    l=m+1
                    r=len(nums)-1
        return -1