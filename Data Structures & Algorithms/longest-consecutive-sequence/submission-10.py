class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        print(nums)
        count=1
        l=[]

        if len(nums)==0:
            return 0
        for i in range(len(nums)-1):
            if abs(nums[i]-nums[i+1])==1:
                count+=1
            else:
                l.append(count)
                count=1
        l.append(count)
        return max(l)