class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixlist=[]
        minlength=min([len(x) for x in strs])
        j=0
        flag=False
        while j<minlength:
            if len(strs)==1:
                return strs[0]
            for i in range(len(strs)-1):
                if (strs[i][j]==strs[i+1][j]):
                    flag=True
                else:
                    prefixstr="".join(prefixlist)
                    return prefixstr
            if flag==True:
                prefixlist.append(strs[0][j])
                j+=1
        prefixstr="".join(prefixlist)
        return prefixstr