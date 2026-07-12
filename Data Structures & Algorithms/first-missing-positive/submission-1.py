class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        print(n)

        for i in range(n):
            if nums[i]<0:
                nums[i]=0
        print(nums)

        for a in nums:
            a=abs(a)
            if a-1 in range(n):
                if nums[a-1]==0:
                    nums[a-1]=-n
                else:
                    nums[a-1]=-abs(nums[a-1])
        print(nums)

        for i in range(1,n+1):
            print(i, nums[i-1])
            if nums[i-1]>=0:
                return i
        return i+1

            


                
