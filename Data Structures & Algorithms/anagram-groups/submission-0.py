class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=[Counter(x) for x in strs]
        output=[]
        for i in range(len(strs)):
            l=[strs[i]]
            if not any(strs[i] in sublist for sublist in output):
                for j in range(len(strs)):
                    if i!=j and freq[i]==freq[j]:
                        l.append(strs[j])
                output.append(l)
        return output
