class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        f=sorted(freq.items(), key=lambda item:item[1], reverse=True) #sort by values
        f=list(dict(f).keys())
        return f[0:k]