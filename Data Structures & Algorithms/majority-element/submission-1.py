class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=Counter(nums)
        f=sorted(freq.items(), key=lambda item:item[1], reverse=True) #sort by values
        return list(dict(f).keys())[0]